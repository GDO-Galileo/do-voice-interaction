from flask import Flask, request
import json
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

@app.route("/grammar-correction", methods=['POST'])
def perform_grammar_correcection():
    receivedData = json.loads(request.data)
    text_data = receivedData['transcript']

    # perform parts of speech tagging
    doc = tag_parts_of_speech(text_data)

    pos = []
    for token in doc:
        pos.append(token.pos_)

    # do cool bert stuff here

    data = {'status': 'ok', 'service': 'grammar correction service', 'response': pos}
    
    response = app.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )

    return response

def tag_parts_of_speech(text_data):
    doc = nlp(text_data)

    # do stuff here that will manipulate the Doc object and return useful info
    
    return doc

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False) # set debug=False for production