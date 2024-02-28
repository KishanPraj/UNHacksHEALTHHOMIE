import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load data from the CSV file
csv_file = 'diabetes1.csv'  # Replace with the path to your CSV file
data = pd.read_csv(csv_file)
total_data = data.shape[0]

# Displaying the coun
print("Total number of data:", total_data)

#filtered_data = data[(data['SkinThickness'] > 0) & (data['DiabetesPedigreeFunction'] > 0) & (data['Glucose'] > 0) & (data['BloodPressure'] > 0) & (data['Insulin'] > 0) & (data['BMI'] > 0) & (data['Age'] > 0)]
filtered_data = data[(data['Insulin'] > 0) & (data['Pregnancies'] <=4)  & (data['Glucose'] > 70) ]

total_filtered_data = filtered_data.shape[0]
print("Total number of filtered data:", total_filtered_data)

data=filtered_data

 # Split the data into features (symptoms) and target (disease labels)
columns_to_drop = ["Outcome", "SkinThickness","DiabetesPedigreeFunction"]
#columns_to_drop = ["Outcome", "SkinThickness","DiabetesPedigreeFunction","Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age","Outcome"]

X = data.drop(columns=columns_to_drop)


y = data['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.12, random_state=42)

# Create a Decision Tree Classifier
clf = DecisionTreeClassifier()

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on test data
y_pred = clf.predict(X_test)

from joblib import dump, load

# Save the model to a file
model_filename = 'diabetes_decision_tree_model.joblib'
dump(clf, model_filename)
print(f"Model saved to {model_filename}")

# Calculate accuracy (for evaluation)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}%")
#
# def recieve_syms():
#     all=[]
#     for item in ["age","sex","chest_pain_type","resting_bp","cholestoral","fasting_blood_sugar","restecg","max_hr","exang","oldpeak","slope","num_major_vessels","thal"]:
#         if item!="oldpeak" or "":
#             single=int(input(f"What is your {item}?: "))
#             all.append(single)
#         else:
#             single = float(input(f"What is your {item}?: "))
#             all.append(single)
#     return all
#
# real = recieve_syms()
# def prediction(stuff):
#     predicted_disease = clf.predict([stuff])
#     if predicted_disease[0]==1:
#         print("You most likely have diabetes")
#     else:
#         print("You most likely do not have diabetes")
#
#
# prediction(real)


