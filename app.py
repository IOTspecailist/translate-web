from flask import Flask, request, jsonify
from googletrans import Translator
import re

app = Flask(__name__)
translator = Translator()
#note1

def is_valid_email(email: str) -> bool:
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None
@app.route('/')
def index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '')
    translated = translator.translate(text, src='ko', dest='en')
    return jsonify({'translated': translated.text})


@app.route('/check_email', methods=['POST'])
def check_email():
    data = request.get_json()
    email = data.get('email', '')
    result = '적합' if is_valid_email(email) else '부적합'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
