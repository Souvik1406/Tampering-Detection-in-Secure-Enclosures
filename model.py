import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load and preprocess data
data = pd.read_csv('sensor_data.csv')  # Replace with your dataset path
X = data[['accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z']]
y = data['label']  # Label indicating normal (0) or tampered (1)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
print("Model Performance:")
print(classification_report(y_test, predictions))

# Save the model
joblib.dump(model, 'tampering_detection_model.pkl')
print("Model saved as 'tampering_detection_model.pkl'")
