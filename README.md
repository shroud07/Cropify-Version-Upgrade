<div align="center">
  
# 🌱 CROPIFY
**An Intelligent, AI-Powered Agricultural Advisory Platform**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-black?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=flat-square&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

*Empowering farmers to maximize their yield through Machine Learning and Deep Learning.*

</div>

---

## 💡 Motivation

Agriculture is the backbone of the economy, especially in countries like India where it sustains the majority of the population. Despite its importance, many farmers still rely on traditional, intuition-based methods rather than data-driven strategies. 

**Cropify** bridges the gap between traditional farming and modern artificial intelligence. By leveraging state-of-the-art Machine Learning and Deep Learning models, this platform provides actionable insights to help farmers optimize their crop selection, manage soil nutrients, and quickly identify and treat plant diseases. 

---

## 🚀 Key Features

### 🌾 1. Crop Recommendation Engine
Takes the guesswork out of farming. By analyzing soil parameters (Nitrogen, Phosphorous, Potassium, pH) and real-time weather data (temperature, humidity, rainfall) based on the user's location, the system recommends the most profitable and suitable crop to cultivate.

### 🧪 2. Fertilizer Suggestion System
A diagnostic tool for your soil. Users input their soil's current nutrient levels and their target crop. The algorithm evaluates the data to identify nutrient deficiencies or excesses, providing specific, actionable advice on which fertilizers to apply for optimal growth.

### 🐛 3. Plant Disease Detection (Deep Learning)
An instant, vision-based diagnostic tool. Users simply upload a clear image of a plant leaf. The underlying neural network identifies whether the plant is healthy or diseased. If a disease is detected, the system provides a brief background on the pathogen and actionable steps to cure it.
*(Currently supports 14 different crops including Apple, Corn, Grape, Potato, Tomato, and more).*

---

## 📊 Data Sources

The models powering Cropify were trained on robust, specialized datasets:
* **[Crop Recommendation Dataset](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset)** *(Custom built)*
* **[Fertilizer Suggestion Dataset](https://github.com/shroud07/Cropify/blob/training/Data-raw/Fertilizer.csv)** *(Custom built)*
* **[Plant Disease Detection Dataset](https://www.kaggle.com/vipoooool/new-plant-diseases-dataset)**

---

## 🛠️ Technology Stack

* **Frontend:** HTML5, CSS3, JavaScript, Tailwind CSS (Modernized)  
* **Backend:** Python, Flask  
* **Machine Learning:** Scikit-Learn, NumPy, Pandas, Matplotlib  
* **Deep Learning:** PyTorch, Torchvision  
* **APIs:** OpenWeatherMap API  

---

## 💻 Local Installation & Setup

Follow these steps to get the project running on your local machine:

**1. Prerequisites**
Ensure you have Git and Anaconda / Miniconda installed.

**2. Setup Instructions**
Clone the repository from GitHub
```bash
git clone [https://github.com/shroud07/Cropify.git](https://github.com/shroud07/Cropify.git)
```
Navigate into the newly cloned
```bash
cd Cropify
```
Create a new Conda environment named `cropify` using Python 3.6.12.
```bash
conda create -n cropify python=3.6.12
```
Activate the `cropify` environment.
```bash
conda activate cropify
```
Install all necessary dependencies listed in the `requirements.txt` file.
```bash
pip install -r requirements.txt
```
Run the `app.py` script to start the server.
```bash
python app.py
```

Once the server starts successfully, open the generated localhost URL in your browser to access the Cropify platform and explore its intelligent agricultural solutions.

---

## 📖 Usage Guide

### 🌱 Crop Recommendation System
Enter the required soil nutrient values:
* Nitrogen (N)
* Phosphorous (P)
* Potassium (K)

Along with environmental parameters such as temperature, humidity, rainfall, and pH level. The system analyzes these inputs and recommends the most suitable crop for cultivation.

### 🧪 Fertilizer Recommendation System
Provide soil nutrient values and crop details to receive personalized fertilizer suggestions that help optimize crop growth and improve yield.

### 🍃 Plant Disease Detection
Upload a clear image of a plant leaf. The deep learning model will analyze the image and predict the disease affecting the crop, along with recommended precautions and treatment measures.

---

## 📍 Input Guidelines

### Location Input
The crop recommendation module uses real-time weather information from the OpenWeatherMap API. For accurate results:
* Use standard and commonly recognized city names.
* Avoid entering very small villages or remote locations that may not be available in the weather database.
* Verify spelling before submitting.

### ⚠️ NPK Value Guidelines
Ensure that the entered Nitrogen (N), Phosphorous (P), and Potassium (K) values accurately represent your soil test report. Correct nutrient values significantly improve recommendation accuracy for both crop and fertilizer prediction modules.

---

## 🎥 Application Demonstrations

### 🌾 Crop Recommendation
<p align="center"> 
  <img src="assets/demo/crop_recommendation.gif" alt="Crop Recommendation Demo" width="800"/> 
</p>

### 🧪 Fertilizer Recommendation
<p align="center"> 
  <img src="assets/demo/fertilizer_recommendation.gif" alt="Fertilizer Recommendation Demo" width="800"/> 
</p>

### 🍃 Disease Detection
<p align="center"> 
  <img src="assets/demo/disease_detection.gif" alt="Disease Detection Demo" width="800"/> 
</p>

*(Note: Ensure the GIF paths point to your actual demo files or hosted links.)*

---

## 📈 Future Enhancements

The current version of Cropify provides a strong foundation for AI-powered smart farming. Future developments may include:

* 🌿 Expanding disease detection to support more crops, pests, and plant disorders.
* 🌍 Multi-language support for regional and local languages to improve accessibility for farmers.
* 📊 Crop market price forecasting using machine learning and historical market trends.
* 🛰️ Satellite and IoT-based farm monitoring for precision agriculture.
* 🤖 AI-powered farming assistant for personalized agricultural guidance.
* ☁️ Cloud deployment with user accounts and farm history tracking.
* 📱 Dedicated Android and iOS applications for wider adoption.

---

## 🙏 Credits & Acknowledgements

This project was developed as part of an effort to leverage Artificial Intelligence and Machine Learning for modern agriculture. Special thanks to:

* ⭐ **Harvestify by Gladiator07** for inspiration and reference architecture. [HERE](https://github.com/Gladiator07/Harvestify)
* 🎓 **Krish Naik** for educational resources and machine learning guidance.
* 🌐 **OpenWeatherMap API** for real-time weather information.
* 🧠 **The open-source community** for providing datasets, frameworks, and development tools that made this project possible.

<div align="center">
  <br>
  
  **🌱 Cropify — Smart Agriculture Powered by AI**
  
  *Empowering farmers with intelligent crop recommendations, fertilizer suggestions, and disease detection solutions.*

</div>