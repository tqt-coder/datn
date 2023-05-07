from flask import Flask, render_template, request
import docx2txt
import torch
from transformers import AutoModel, AutoTokenizer
from transformers import RobertaForQuestionAnswering, RobertaConfig, WEIGHTS_NAME

# --------- Constant ----------------------
MAX_SIZE = 256
DEVICE = torch.device('cpu')
FILE_NAME = "CONTEXT.docx"
# ----------- Load models --------------
phobert = AutoModel.from_pretrained("vinai/phobert-large")
tokenizer_2 = AutoTokenizer.from_pretrained("vinai/phobert-large")
model_2 = RobertaForQuestionAnswering(phobert.config).from_pretrained(
    "../model/phobert_model").to(DEVICE)


app = Flask(__name__)

def split_text(text, max_length):
    sentences = text.split(', ')  # Chia đoạn thành các câu
    segments = []
    current_segment = ""

    for sentence in sentences:
        if len(current_segment) + len(sentence) + 2 <= max_length:  # Kiểm tra độ dài của đoạn văn bản
            current_segment += sentence + '. '  # Thêm câu vào đoạn văn bản hiện tại
        else:
            # Thêm đoạn văn bản vào danh sách các đoạn
            segments.append(current_segment.strip())
            current_segment = sentence + '. '  # Bắt đầu một đoạn mới

    if current_segment:
        # Thêm đoạn văn bản cuối cùng vào danh sách các đoạn
        segments.append(current_segment.strip())

    return segments


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        FILE_NAME = f.filename
        # print(FILE_NAME)
        f.save(f.filename)
        return render_template("index.html", name=FILE_NAME)


@app.route('/')
def upload():
    return render_template('upload.html')


@app.route('/answer', methods=['POST'])
def answer():
    data = request.form
    question = data['questions']
    file_name = data['filename']
    context = docx2txt.process(file_name)
    segments = split_text(context, MAX_SIZE)

    answers = []
    for segment in segments:
        # Tokenize inputs
        inputs = tokenizer_2.encode_plus(
            question, segment, add_special_tokens=True, return_tensors="pt")

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
    return render_template("./index.html", question=question, context=context, answer=final_answer)


if __name__ == '__main__':
    app.run
