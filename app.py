from flask import Flask, request, jsonify
from googletrans import Translator
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)
@app.route('/translate', methods=['POST'])
@cross_origin(supports_credentials=True)
def translate():
    try:
        data = request.get_json()
        text = data['text']
        target_language = data['target_language']

        translator = Translator()
        translated_text = translator.translate(text, dest=target_language).text

        response = {'translatedText': translated_text}
        return jsonify(response), 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
