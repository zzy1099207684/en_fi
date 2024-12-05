from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from transformers import pipeline

app = Flask(__name__)
app.secret_key = 'en-fi'
# model
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fi")

@app.route('/en_fi')
def index():
    return render_template('index.html')

# 定义路由和视图函数
@app.route('/translater', methods=['POST'])
def translater():
    first = datetime.now()
    content = request.json.get("content")
    if content is not None:
        translation = translator(content)
        result = translation[0]['translation_text']
        return {"translation_res": str(result)}


if __name__ == '__main__':
    app.run('0.0.0.0', debug=False)
