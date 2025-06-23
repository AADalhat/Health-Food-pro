# Health-Food-pro
An AI powered food classification system that keeps you healthy
# 🍲 HoodHealth Pro+

HoodHealth Pro+ is an AI-powered food recognition and health advisory web app designed to identify Nigerian local dishes and provide personalized nutrition and health insights. Built with TensorFlow and Streamlit, this app supports health-conscious decisions based on visual food input.

---

## 🚀 Features

- 📸 Upload a photo of Nigerian food
- 🧠 Classify into 10 local dishes using MobileNetV2
- 📊 View ingredients, calories, and nutrients
- ❤️ Get personalized advice for:
  - Diabetes
  - Hypertension
  - Weight loss

---

## 🧰 Tech Stack

- `Streamlit` for frontend UI
- `TensorFlow` (MobileNetV2) for food classification
- `Pillow`, `NumPy` for image preprocessing
- `Python` for health risk logic
- `JSON` metadata for nutritional data

---

## 📁 Files

| File                         | Description                                |
|------------------------------|--------------------------------------------|
| `app.py`                     | Main Streamlit app                         |
| `mobilenet_model_finetuned.h5` | Trained model file                        |
| `food_info.json`             | Metadata with nutrition and advice         |
| `requirements.txt`           | Dependencies for deployment                |

---

## 🧪 Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py


👨‍💻 Author
Abdullahi Abdussalam Dalhat
Machine Learning Enthusiast | AI for Local Problems
🔗 LinkedIn
🌐 EJAZTECH.AI
