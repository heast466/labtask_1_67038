# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Step 1: Create dataset
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7],
    'WeeklyVisits': [2, 1, 3, 4, 1, 2, 5],
    'AvgSpend': [45, 120, 75, 35, 150, 90, 25],
    'LoyaltyScore': [3, 8, 5, 2, 9, 6, 1],
    'PreferredTime': ['Morning', 'Evening', 'Afternoon', 'Morning', 'Evening', 'Afternoon', 'Morning'],
    'HighValue': ['No', 'Yes', 'No', 'No', 'Yes', 'No', 'No']
}

df = pd.DataFrame(data)

df['HighValueEncoded'] = df['HighValue'].map({'No': 0, 'Yes': 1})

X = df[['WeeklyVisits', 'AvgSpend', 'LoyaltyScore']]  # Only use numerical columns
y = df['HighValueEncoded']  # Use the encoded numbers, not text


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

print("Model trained successfully!")
print(f"Training set size: {len(X_train)}")
print(f"Test set size: {len(X_test)}")