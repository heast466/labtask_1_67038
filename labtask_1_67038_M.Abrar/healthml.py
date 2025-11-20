import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
#Step 1: Create dataset
data = {
    'PatientID': [101, 102, 103, 104, 105],
    'AppointmentAttendance': [88, 72, 96, 58, 82],
    'MedicationAdherence': [9, 5, 10, 3, 8],
    'ExerciseFrequency': [8, 4, 10, 2, 7],
    'Blood_Pressure': ['140/90', '130/85', '135/93', '160/100', '125/80'],  # Added comma and 5th value
    'HealthScore': [87, 62, 95, 45, 75],
    'HealthRisk': ['No', 'Yes', 'No', 'Yes', 'No']
}
df = pd.DataFrame(data)
X = df[['AppointmentAttendance', 'MedicationAdherence', 'ExerciseFrequency']]
y = df['HealthRisk']
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.3, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
new_patient_df = pd.DataFrame([[72, 5, 4]], columns=['AppointmentAttendance', 'MedicationAdherence', 'ExerciseFrequency'])
prediction = model.predict(new_patient_df)
print("Prediction for new patient:", prediction[0])