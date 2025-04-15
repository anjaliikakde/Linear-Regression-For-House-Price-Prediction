# House Price Prediction App

This project is a beginner-friendly, end-to-end **House Price Prediction Web App** built using **Machine Learning (Linear Regression)** and **Streamlit**. It demonstrates the full lifecycle of an ML project, from data analysis to model training and web app deployment using Docker.

This project is ideal for students, hobbyists, or anyone curious about how real-world machine learning applications are built and deployed.

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

## Requirements

- Python 3.10.10
- pip (Python package manager)
- Git
- Docker (Optional, for container deployment)


## How It Works

1. **Data Preprocessing & EDA**  
   - Handles missing values  
   - Scales features  
   - Analyzes distributions, outliers, and correlations  

2. **Model Training**  
   - Linear Regression model trained on cleaned housing data  
   - Saves the model (`model.pkl`) and scaler (`scaler.pkl`)  

3. **Interactive Web App**  
   - Streamlit turns the trained model into a user interface  
   - Users input features and receive real-time predictions  

4. **Deployment with Docker**  
   - Easily containerize the app  
   - Share and run anywhere without worrying about dependencies  

## How to Run the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/house-price-app.git
cd house-price-app
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
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

## How to Run Using Docker

### 1. Build Docker Image

```bash
docker build -t house-price-streamlit .
```

### 2. Run Docker Container

```bash
docker run -p 8501:8501 house-price-streamlit
```

Visit `http://localhost:8501` in your browser.


## Deploying to Render (Cloud Hosting)

1. Push your code to GitHub  
2. Go to [render.com](https://render.com)  
3. Create a **New Web Service**  
4. Connect your GitHub repository  
5. Set Environment to: **Docker**  
6. Port: **8501**  
7. Click **Deploy**

Your app will be live at:

```
https://your-app-name.onrender.com
```
