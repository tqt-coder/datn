from flask import Flask, render_template, request
import docx2txt
import torch
from transformers import AutoModel, AutoTokenizer
from transformers import RobertaForQuestionAnswering, RobertaConfig, WEIGHTS_NAME
from PyPDF2 import PdfFileReader

# --------- Constant ----------------------
MAX_SIZE = 300
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# ----------- Load models --------------
phobert = AutoModel.from_pretrained("vinai/phobert-large")
tokenizer_2 = AutoTokenizer.from_pretrained("vinai/phobert-large")
model_2 = RobertaForQuestionAnswering(phobert.config).from_pretrained(
    "../model/phobert_model").to(DEVICE)

app = Flask(__name__)


def read_file(filename):
    if filename.endswith(".docx"):
        return docx2txt.process(filename)
    elif filename.endswith(".pdf"):
        with open(filename, 'rb') as pdf_file:
            pdf = PdfFileReader(pdf_file)
            pages = []
            for page in pdf.pages:
                text = page.extract_text()
                pages.append(text)
            return '\n'.join(pages)
    else:
        return "Unsupported file format."


@app.route('/success', methods=['POST', 'GET'])
def success():
    if request.method == 'POST':
        data = request.form
        context_input = data['text-context']
        f = request.files['file']
        file_name = f.filename
        if (context_input == '' and file_name == ''):
            return render_template("upload.html",  error='Vui lòng điền vào ô văn bản của bạn hoặc tải lên một file')
        if (file_name == ''):
            return render_template("index.html",  context=context_input)
        else:
            f.save(f.filename)
            context = read_file(file_name)
            return render_template("index.html", name=file_name, context=context)
    else:
        file_name = request.args.get('file')
        context = read_file(file_name)
        return render_template("index.html", name=file_name, context=context)


@app.route('/')
def upload():
    return render_template('upload.html')


def split_text(text, max_length):
    words = text.split()  # Tách các từ trong đoạn văn thành danh sách
    segments = []
    current_segment = ""

    for word in words:
        if len(current_segment) + len(word) + 1 <= max_length:  # Kiểm tra độ dài của đoạn văn bản
            current_segment += word + ' '  # Thêm từ vào đoạn văn bản hiện tại
        else:
            # Thêm đoạn văn bản vào danh sách các đoạn
            segments.append(current_segment.strip())
            current_segment = word + ' '  # Bắt đầu một đoạn mới

    if current_segment:
        # Thêm đoạn văn bản cuối cùng vào danh sách các đoạn
        segments.append(current_segment.strip())

    return segments


@app.route('/answer', methods=['POST'])
def answer():
    data = request.form
    question = data['questions']
    file_name = data['filename']
    context_input = data['text-context']
    context = context_input

    if (file_name != ''):
        context = read_file(file_name)

    segments = split_text(context, MAX_SIZE)

    answers = []
    for segment in segments:
        # Tokenize inputs
        inputs = tokenizer_2.encode_plus(
            question, segment, add_special_tokens=True, return_tensors="pt", truncation=True, max_length=MAX_SIZE)

        # Move inputs tensor to device
        inputs = {key: value.to(DEVICE)
                  for key, value in inputs.items()}

        # get start and end logits for answer
        start_logits, end_logits = model_2(**inputs, return_dict=False)

        # find the answer
        start_idx = torch.argmax(start_logits) + 1
        end_idx = torch.argmax(end_logits) + 2
        answer = tokenizer_2.convert_tokens_to_string(
            tokenizer_2.convert_ids_to_tokens(inputs["input_ids"][0][start_idx:end_idx]))

        answers.append(answer)

    # take final answer
    final_answer = max(answers, key=len)
    return render_template("./index.html", question=question, context=context, answer=final_answer, name=file_name)


if __name__ == '__main__':
    app.run
