import pandas as pd
#Sample dataset
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
df['HealthRiskEncoded'] = df['HealthRisk'].map({'No': 0, 'Yes': 1})
print("Correlation Matrix:")
print(df.corr(numeric_only=True))
at_risk_pattern = df[df["AppointmentAttendance"] < 70]
print("\nPatients with low appointment attendance (<70):")
print(at_risk_pattern)