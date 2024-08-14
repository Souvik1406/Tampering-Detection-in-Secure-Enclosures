import joblib

# Load the trained model
model = joblib.load('tampering_detection_model.pkl')

def predict_tampering(sensor_data):
    """
    Predicts if the provided sensor data indicates tampering.

    Parameters:
    sensor_data (list or np.array): Sensor readings [accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z]

    Returns:
    str: Result of prediction - "Tampering detected!" or "System is secure."
    """
    prediction = model.predict([sensor_data])
    return "Tampering detected!" if prediction[0] == 1 else "System is secure."

# Example usage
sensor_data = [0.01, 0.02, 0.03, 0.1, 0.2, 0.3]  # Replace with actual sensor data
result = predict_tampering(sensor_data)
print(result)
