# Real_Estate

This project predicts housing prices based on features like location, size, and number of bedrooms. It uses a trained machine learning model and provides a Streamlit app for user-friendly predictions.

**What It Does**

- Accepts input details like square footage, number of bedrooms/bathrooms, and location

- Predicts the estimated price using a trained model

- Displays the result via a Streamlit web interface

**Tools Used**

- Python

- Pandas, NumPy, scikit-learn

- Streamlit

- Pickle (for model storage)

**How It Works**

- Data is cleaned and preprocessed

- Model is trained on the real estate dataset

- Model and scaler are saved

- Streamlit app allows user input and real-time prediction

- App is deployed for access via web browser

**Files**

- app.py — Streamlit frontend

- realestate_model.pkl — Trained ML model

- requirements.txt — Dependencies list

**How to Run**

- Clone the repository

- Install dependencies: pip install -r requirements.txt

- Launch the app: streamlit run app.py

**Note**

This project is for demonstration and learning purposes, not intended for real-world financial decisions.
