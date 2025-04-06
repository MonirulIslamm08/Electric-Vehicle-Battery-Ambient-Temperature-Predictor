
# 🔋 Electric Vehicle Battery Ambient Temperature Predictor

This project predicts the **ambient temperature** affecting electric vehicle (EV) batteries using machine learning and deep learning models. Accurate prediction can help improve battery performance, safety, and longevity.

---

## 🚀 Project Highlights

- 📊 **Data Preprocessing**: Cleaned and encoded battery test metadata (discharge, charge, impedance).
- ⚙️ **Feature Engineering**: Selected relevant features including battery capacity, internal resistance (Re, Rct), and test type.
- 🧠 **Model**: Built a deep learning regression model using TensorFlow/Keras.
- 📈 **Performance Evaluation**: Tracked MAE and MSE across training epochs and tested with unseen data.
- 🔍 **Prediction Function**: Implemented a reusable function to predict ambient temperature based on input features.

---

## 📁 Dataset

- Source: Internal dataset with 7,500+ battery test samples.
- Features: `type`, `ambient_temperature`, `Capacity`, `Re`, `Rct`

---

## 🧪 Model Architecture

- Dense(64) → Dropout(0.2) → Dense(32) → Dropout(0.2) → Dense(1)
- Activation: ReLU (hidden layers), Linear (output)
- Optimizer: Adam | Loss: Mean Squared Error

---

## 🛠️ Tech Stack

- Python 🐍
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn
- TensorFlow / Keras

---

## 🔮 Prediction Example

```python
predict_battery_life(
    type_discharge='discharge',
    Capacity=1.674305,
    Re=-4.976500e+11,
    Rct=1.055903e+12,
    label_encoder=label_encoder,
    scaler=scaler,
    model=model
)
```

---

## 💾 Model Saving

Models and encoders are saved as:

- `battery_life_model.pkl`
- `scaler.pkl`
- `label_encoder.pkl`

---

## 📊 Training Performance

Loss and validation loss are plotted to monitor overfitting and convergence. The model achieved a validation MAE around **7.0**.

---

## 📌 Future Improvements

- Hyperparameter tuning  
- Integration with live IoT battery systems  
- Model deployment via Flask or FastAPI  

---

## 🔗 GitHub Repository

[👉 View the Project on GitHub](https://github.com/MonirulIslamm08/Electric-Vehicle-Battery-Ambient-Temperature-Predictor)

---

## 🤝 Let's Connect

Feel free to reach out on [LinkedIn](https://www.linkedin.com/in/monirul-m08/) or open an issue/pull request!
