import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load data from the CSV file
csv_file = 'heart2.csv'  # Replace with the path to your CSV file
data = pd.read_csv(csv_file)

# Split the data into features (symptoms) and target (disease labels)
X = data.drop(columns="target")

y = data['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=42)

# Create a Decision Tree Classifier
clf = DecisionTreeClassifier()

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on test data
y_pred = clf.predict(X_test)

# Calculate accuracy (for evaluation)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}%")

from joblib import dump, load

# Save the model to a file
model_filename = 'heart_decision_tree_model.joblib'
dump(clf, model_filename)
print(f"Model saved to {model_filename}")




'''def recieve_syms():
    all=[]
    for item in ["age","sex","chest_pain_type","resting_bp","cholestoral","fasting_blood_sugar","restecg","max_hr","exang","oldpeak","slope","num_major_vessels","thal"]:
        if item!="oldpeak":
            single=int(input(f"What is your {item}?: "))
            all.append(single)
        else:
            single = float(input(f"What is your {item}?: "))
            all.append(single)
    return all

real = recieve_syms()
print(real)
def prediction(stuff):
    predicted_disease = clf.predict([stuff])
    print(predicted_disease[0])
prediction(real)'''
