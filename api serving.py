from flask import Flask, request, jsonify
import trainer
app = Flask(__name__)

model = trainer.trainer()
model.load('model')

@app.route('/translate', methods = ['POST'])
def translate():
    data = request.json
    input_text = data['input_text']
    # output_text = model_inference(input_text)
    return jsonify({'output_text': output_text})