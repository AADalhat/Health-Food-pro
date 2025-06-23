pip install streamlit tensorflow pillow

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import json

# Load model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(mobilenet_model.h5.keras)
    return model

model = load_model()

# Load food metadata
@st.cache_data
def load_metadata():
    with open(food_info.json, "r") as f:
        return json.load(f)

food_info = load_metadata()
class_names = list(food_info.keys())

# Set page config
st.set_page_config(page_title="HoodHealth Pro+", layout="centered")

# Title
st.title("🍲 HoodHealth Pro+ - Know Your Food, Know Your Risk")

# Upload image
uploaded_file = st.file_uploader("Upload a food image", type=["jpg", "jpeg", "png"])

# Select health condition (optional)
condition = st.selectbox("Do you have any of the following health conditions?", ["None", "Diabetes", "Hypertension", "Weight Loss"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB").resize((224, 224))
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess image
    img_array = tf.keras.preprocessing.image.img_to_array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions)
    predicted_class = class_names[predicted_index]

    # Show result
    st.subheader(f"🍽️ Predicted Food: **{predicted_class}**")
    info = food_info[predicted_class]

    # Display metadata
    st.markdown(f"🌍 **Ethnicity/Region**: {info['ethnicity']}")
    st.markdown(f"🥦 **Ingredients**: {', '.join(info['ingredients'])}")
    st.markdown(f"🔥 **Calories**: {info['calories']} kcal")
    st.markdown(f"🍚 **Carbs**: {info['carbs']}g | 🥩 Protein: {info['protein']}g | 🧈 Fat: {info['fat']}g")
    st.markdown(f"🌱 **Diet Type**: {info['diet_type']}")
    st.markdown(f"❤️ **Health Advice**: {info['advice']}")

    # Risk condition logic
    if condition != "None":
        st.warning(f"⚠️ Based on your selected condition (**{condition}**), please consider the following:")
        if condition == "Diabetes" and info['carbs'] > 50:
            st.write("🍬 This food is high in carbs and may not be suitable for diabetic individuals.")
        elif condition == "Hypertension" and "salt" in [i.lower() for i in info['ingredients']]:
            st.write("🧂 This food may contain salt; limit intake if you have hypertension.")
        elif condition == "Weight Loss" and info['calories'] > 500:
            st.write("⚖️ This food is high in calories; consider a smaller portion or a lighter option.")
        else:
            st.success("✅ This food is generally okay for your condition.")
