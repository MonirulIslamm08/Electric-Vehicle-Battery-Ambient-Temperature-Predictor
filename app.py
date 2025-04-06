from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle
from tensorflow.keras.models import load_model


app = Flask(__name__)

# Load model and encoders
model = load_model('model/battery_life_model.h5')
scaler = pickle.load(open('model/scaler.pkl', 'rb'))
label_encoder = pickle.load(open('model/label_encoder.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    type_discharge = request.form['type']
    Capacity = float(request.form['Capacity'])
    Re = float(request.form['Re'])
    Rct = float(request.form['Rct'])

    # Process inputs
    type_encoded = label_encoder.transform([type_discharge])[0]
    input_array = np.array([[type_encoded, Capacity, Re, Rct]])
    input_scaled = scaler.transform(input_array)

    # Predict
    prediction = model.predict(input_scaled)
    predicted_value = round(prediction[0][0], 2)

    return render_template('index.html', prediction_text=f"🔋 Predicted Ambient Temperature: {predicted_value}°C")

if __name__ == '__main__':
    app.run(debug=True)
