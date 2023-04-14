from flask import Flask, render_template, request
from transformers import pipeline
app = Flask(__name__)


@app.route('/answer', methods=['POST'])
def answer():
    data = request.form
    # load request with 2 parameters: questions and contexts
    question = data['questions']
    context = data['contexts']
    question_answerer = pipeline(
        "question-answering", model="../model/train_bert_transformer/checkpoint-3000")  # change url when run
    response = question_answerer(question=question, context=context)
    # return response['answer']
    return render_template("./index.html", question=question, context=context, answer=response['answer'])


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
