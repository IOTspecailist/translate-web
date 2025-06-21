from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()
#note
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

if __name__ == '__main__':
    app.run(debug=True)
