import os
import streamlit as st
import pickle
import numpy as np

# ─── Load your model once ──────────────────────────────────────────
@st.cache_resource
def load_model():
    path = os.path.join(os.getcwd(), "Re_Model.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)

model = load_model()

# ─── App header ──────────────────────────────────────────────────
st.title("🏠 Real-Estate Price Predictor")
st.markdown("Adjust the property features below and click **Predict**.")

# ─── Dynamically build inputs from your model’s feature names ─────
try:
    feature_names = list(model.feature_names_in_)
except AttributeError:
    # fallback: manually list your columns here if feature_names_in_ isn’t available
    feature_names = [
        "sqft", "bedrooms", "bathrooms", "age",  # example placeholders
        # … add the rest of your features …
    ]

inputs = {}
for feat in feature_names:
    # you can switch to slider/text_input depending on your feature
    inputs[feat] = st.number_input(feat, value=0.0)

# ─── Prediction ──────────────────────────────────────────────────
if st.button("Predict Price"):
    X = np.array([list(inputs.values())])
    price = model.predict(X)[0]
    st.success(f"Estimated market price: ₹ {price:,.2f}")
