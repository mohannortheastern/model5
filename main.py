import os
from tensorflow.keras.models import load_model
from flask import Flask, jsonify, request

app = Flask(__name__)

# Update this path to reflect the location of the model file in the Cloud Storage bucket
model_path = "gs://spokendigitmodel/model"

# Load the model
model = load_model(model_path)

# Define a route for the microservice
@app.route('/predict', methods=['POST'])
def predict():
    # Get the audio data from the request
    audio_data = request.files['audio'].read()

    # Preprocess the audio data (e.g., convert to spectrogram)
    preprocessed_data = preprocess(audio_data)

    # Make a prediction with the model
    prediction = model.predict(preprocessed_data)

    # Convert the prediction to a JSON response
    response = {'prediction': str(prediction)}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
