from flask import Flask, render_template
from transformers import pipeline
app = Flask(__name__)


@app.route('/')
def index():
    question = '''Quốc Tuấn học trường gì?'''
    context = '''Quốc Tuấn sinh ngày 31/01/2001, học trường SPKT tại Hồ Chí Minh. Quê anh ấy ở Củ Chi'''
    question_answerer = pipeline(
        "question-answering", model="../model/DistilBERT")
    response = question_answerer(question=question, context=context)
    return response['answer']


if __name__ == '__main__':
    app.run(debug=True)
