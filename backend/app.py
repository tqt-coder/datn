from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)


@app.route('/answer', methods=['POST'])
def answer():
    data = request.form
    f = request.files
    # load request with 2 parameters: questions and contexts
    question = data['questions']
    # context = 'Hello'
    # context = data['contexts']
    context = f['file']
    # context = f.filename
    question_answerer = pipeline(
        "question-answering", model="../model/train_bert_transformer/checkpoint-3000")
    response = question_answerer(question=question, context=context)
    # return response['answer']
    return render_template("./index.html", question=question, context=context, answer=response['answer'], name = context.filename)

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(f.filename)  
        return render_template("index.html", name = f.filename)
    

@app.route('/')
def upload():
    return render_template('upload.html')

# @app.route('/')
# def index():
#     return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
