import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

# Load data
df = pd.read_csv("Housing.csv")

# Select features
X = df[['bedrooms', 'bathrooms', 'floors', 'sqft_living']]
y = df['price']

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train
model = LinearRegression()
model.fit(X_scaled, y)

# Save model and scaler
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))

print("Model and scaler saved.")