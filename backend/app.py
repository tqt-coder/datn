from flask import Flask, render_template, request
from transformers import pipeline
app = Flask(__name__)


@app.route('/answer', methods=['POST'])
def answer():
    data = request.json
    # load request with 2 parameters: questions and contexts
    question = data['questions']
    context = data['contexts']
    question_answerer = pipeline(
        "question-answering", model="../model/DistilBERT")
    response = question_answerer(question=question, context=context)
    return response['answer']


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
