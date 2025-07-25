
# 🍽️ FoodHealth Pro — AI-Powered Food Classification & Health Advisory System

![FoodHealth Pro Logo]("C:\Users\Abdullahi Abdussalam\Pictures\Screenshots\Screenshot 2025-07-25 100210.png")

FoodHealth Pro+ is an intelligent food recognition and personalized dietary advisory system tailored for local African meals. It leverages computer vision and nutrition science to support individuals with health conditions like **diabetes, hypertension, malnutrition, weight management, pregnancy**, and more.

---

## 🧠 Problem Statement

> *Unhealthy diets contribute to more deaths globally than tobacco, and in Africa, poor dietary knowledge is a growing health threat.*  
> **— Global Burden of Disease Study (Lancet, 2019)**

Africa faces a silent crisis of unbalanced diets, with rising cases of **diabetes, hypertension, obesity**, and **malnutrition**. Local meals often lack clear nutritional guidelines, and millions have no access to reliable dietary education.

---

## ✅ Solution: FoodHealth Pro+

FoodHealth Pro+ uses **AI** to classify local foods from images and instantly provide:

- ✅ Nutritional breakdown
- ✅ Risk scores (e.g. for diabetics, hypertensives)
- ✅ Tailored health advice
- ✅ Multi-language support (English, Hausa, Yoruba, Igbo)
- ✅ Audio feedback (Text-to-Speech)
- ✅ Downloadable PDF dietary reports


---

## 🛠️ Key Features

| Feature | Description |
|--------|-------------|
| 🍲 Food Image Classification | Classifies local meals using EfficientNet-based model |
| 💊 Personalized Health Advisory | Advice for diabetics, hypertensive, pregnant, etc. |
| 🧾 Nutrition Facts | Shows calories, protein, fat, carbs |
| 🔉 Text-to-Speech (TTS) | Audio support in English (others coming soon) |
| 📥 PDF Report Generator | Download full dietary and health report |
| 🌍 Multi-language UI | Supports Hausa, Yoruba, Igbo (text) |
| 🧠 AI-powered | Uses TensorFlow + Transfer Learning (EfficientNet) |

---

## 📦 Classes Supported

```python
["akara", "banga_soup", "egusi_soup", "jollof_rice", "moi_moi", 
 "nkwobi", "okpa", "suya", "tuwo", "yam_porridge"]
```

---

## 🚀 How It Works

1. **Upload** or capture an image of food  
2. AI model predicts the food class  
3. Based on selected health conditions (e.g. Diabetic), the app:
   - Fetches ingredients
   - Analyzes nutritional data
   - Returns advice, risk score, and voice-over  
4. You can **download** a PDF health report

---

## 🎬 Demo

👉 [Watch Demo Video](https://www.linkedin.com/posts/abdullahi-abdussalam-dalhat_3mttlearningcommunity-my3mtt-3mttlearningcommunity-activity-7344047880837476355-AL6M?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEctOPQBeBwKIdQILVpmdU_ZJcDW-klX1s0)  
👉 [Try Live App](https://huggingface.co/spaces/AADalhat/FoodHealth-pro)

---

## 🏗️ Tech Stack

- **Frontend**: Gradio
- **Backend**: Python, TensorFlow
- **Model**: EfficientNet (fine-tuned on 10-class local food dataset)
- **Other Tools**: gTTS, ReportLab (PDF), NumPy, Pillow
- **Deployment**: Hugging Face Spaces

---

## 🔁 Model Architecture

- Base model: `EfficientNetB0`
- Input shape: `(224, 224, 3)`
- Training: Transfer learning (frozen + fine-tuned phases)
- Optimizer: `Adam`, Loss: `categorical_crossentropy`
- Accuracy: ~92% on test set

---

## 📂 Project Structure

```bash
📁 FoodHealthPro/
├── app.py               # Main Streamlit/Gradio app
├── model/
│   └── food_model.h5    # Trained EfficientNet model
├── utils/
│   ├── health_logic.py  # Health advice & risk logic
│   ├── pdf_generator.py # PDF report builder
├── data/
│   └── food_labels.json # Label mappings, nutrition data
├── assets/
│   └── logo.png         # Logo and image assets
└── requirements.txt
```

---

## 💡 Use Cases

- ✅ Hospitals & clinics for patient dietary management
- ✅ Personal nutrition assistant (mobile)
- ✅ Educational tool for diet awareness in schools
- ✅ Public health intervention

---

## 🌐 Multilingual Support

- [x] English
- [x] Hausa (Text advice only)
- [x] Yoruba (Text advice only)
- [x] Igbo (Text advice only)
> **Voice/audio for local languages coming soon!**

---

## 🧑‍💻 Author & Contributors

- **👨‍🔬 Abdullahi Abdussalam Dalhat**  
  AI Engineer | EJAZTECH AI & 3MTT Showcase Winner  
  [GitHub](https://github.com/AADalhat/) | [LinkedIn](www.linkedin.com/in/abdullahi-abdussalam-dalhat)

---

## 🏆 Awards

- 🥇 **3MTT Knowledge Showcase (May Edition)** — *Best Health AI Project Winner*  

---

## 📃 License

This project is open-source under the **MIT License**.

---

## 📢 Showcase & Media

> #My3MTT #3MTTLearningCommunity #HoodHealthAI #NutridietAI #AIForAfrica  
Tag us on [LinkedIn](https://linkedin.com/in/abdulabdull), Twitter @aAADalhat and mention your use case!
