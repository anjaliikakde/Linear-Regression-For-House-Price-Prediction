# House Price Prediction Using Linear Regression 

This project is a beginner-friendly, end-to-end **House Price Prediction Web App** built using **Machine Learning (Linear Regression)** and **Streamlit**. It demonstrates the full lifecycle of a machine learning project, from data analysis to model training and web app deployment using Docker.

Ideal for students, hobbyists, or anyone curious about how real-world machine learning applications are built and deployed.

---

## Table of Contents

- [Project Structure](#project-structure)  
- [Requirements](#requirements)  
- [What is Linear Regression?](#what-is-linear-regression)  
- [How It Works](#how-it-works)  
- [How to Run the App Locally](#how-to-run-the-app-locally)  
- [How to Run Using Docker](#how-to-run-using-docker)  
- [Deploying to Render (Cloud Hosting)](#deploying-to-render-cloud-hosting)  

---

## Project Structure

```
house-price-app/
│
├── app.py               → Streamlit app for interactive predictions  
├── train_model.py       → Script for data cleaning, EDA, training, and saving the model  
├── model.pkl            → Trained Linear Regression model  
├── scaler.pkl           → Feature scaler for consistent input  
├── Housing.csv          → Dataset used for training  
├── requirements.txt     → Python packages required  
├── Dockerfile           → Docker setup for containerized deployment  
└── README.md            → Project documentation (this file)
```

---

## Requirements

- Python 3.10.10  
- pip (Python package manager)  
- Git  
- Docker (optional, for container deployment)  

---

## What is Linear Regression

**Linear Regression** is one of the most fundamental machine learning algorithms used for predicting a continuous numeric value. It works by drawing a straight line (called the regression line) that best fits the data points.

The model tries to learn the relationship between input features (such as number of rooms, location, area) and the target variable (house price). Once trained, it can predict house prices for new data.

In simple terms:  
If you know the size of a house, the model helps you **predict its price** based on what it learned from past data.

---

## How It Works

1. **Data Preprocessing and EDA**  
   - Handles missing values  
   - Scales numerical features  
   - Analyzes distributions, outliers, and correlations  

2. **Model Training**  
   - Uses Linear Regression to train on housing data  
   - Saves the trained model (`model.pkl`) and scaler (`scaler.pkl`)  

3. **Interactive Web App**  
   - Built using Streamlit  
   - Users input property details and get real-time price predictions  

4. **Deployment with Docker**  
   - Easily containerize the app for consistent deployment  
   - Run it anywhere without worrying about environment setup  

---

## How to Run the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/anjaliikakde/house-price-app.git
cd house-price-app
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# Or use source venv/bin/activate on macOS/Linux
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Train the Model

```bash
python train_model.py
```

### 5. Launch the Web App

```bash
streamlit run app.py
```

---

## How to Run Using Docker

### 1. Build the Docker Image

```bash
docker build -t house-price-streamlit .
```

### 2. Run the Docker Container

```bash
docker run -p 8501:8501 house-price-streamlit
```

Visit your app at `http://localhost:8501` in your browser.

---

## Deploying to Render (Cloud Hosting)

1. Push your code to GitHub  
2. Go to [render.com](https://render.com)  
3. Create a **New Web Service**  
4. Connect your GitHub repository  
5. Set environment to: **Docker**  
6. Port: **8501**  
7. Click **Deploy**  

Your app will be live at:

```
https://your-app-name.onrender.com
```
