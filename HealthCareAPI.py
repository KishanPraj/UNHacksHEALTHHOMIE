from flask import Flask, request, jsonify
from joblib import load
import numpy as np
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Load your trained model
model = load('diabetes_decision_tree_model.joblib')

heartModel = load('heart_decision_tree_model.joblib')


@app.route('/predictdiabetes', methods=['POST'])
def predictdiabetes():
    # Get data from the POST request.
    data = request.get_json(force=True)

    # Extract features from the JSON. Adjust the names as per your model's features.
    features_names = ['Pregnancies','Glucose','BloodPressure','Insulin','BMI','Age']  # Example feature names
    features_values = [data.get(feature, None) for feature in features_names]

    # Check if all features are provided
    if None in features_values:
        return jsonify({'error': 'Missing features'}), 400

    # Make prediction using the loaded model
    prediction = model.predict([features_values])

    # Return the prediction

    if int(prediction[0]) ==1:
        return jsonify({'prediction': 'Please consult doctor...!'})
    if int(prediction[0]) ==0:
        return jsonify({'prediction': 'You are in Good Health Condition...!'})

@app.route('/predictheartdisease', methods=['POST'])
def predictheartdisease():
    # Get data from the POST request.
    data = request.get_json(force=True)

    print("aaa")

    # Extract features from the JSON. Adjust the names as per your model's features.
    features_names = ['age','sex','chest_pain_type','resting_bp','cholestoral','fasting_blood_sugar','restecg','max_hr','exang','oldpeak','slope','num_major_vessels','thal']  # Example feature names
    features_values = [data.get(feature, None) for feature in features_names]

    # Check if all features are provided
    if None in features_values:
        return jsonify({'error': 'Missing features'}), 400

    # Make prediction using the loaded model
    prediction = heartModel.predict([features_values])

    # Return the prediction

    if int(prediction[0]) ==1:
        return jsonify({'prediction': 'Please consult doctor...!'})
    if int(prediction[0]) ==0:
        return jsonify({'prediction': 'You are in Good Health Condition...!'})

if __name__ == '__main__':
    app.run(debug=True)



# sathiskumar@SathisKumars-MacBook-Pro healthcare-app % curl -X POST -H "Content-Type: application/json" \
#      -d '{"Pregnancies":4, "Glucose": 148,"BloodPressure": 72,"Insulin": 90.6, "BMI": 33.6,"Age": 47}' \
#      http://localhost:5000/predict
# {
#   "prediction": 0
# }
# sathiskumar@SathisKumars-MacBook-Pro healthcare-app % curl -X POST -H "Content-Type: application/json" \
#      -d '{"Pregnancies":4, "Glucose": 500,"BloodPressure": 72,"Insulin": 90.6, "BMI": 33.6,"Age": 47}' \
#      http://localhost:5000/predictdiabetes
# {
#   "prediction": 1
# }