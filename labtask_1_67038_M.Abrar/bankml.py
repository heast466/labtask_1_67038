import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
#Step 1: Create dataset
data = {
    'CustomerID': [201, 202, 203, 204, 205],
    'AccountBalance': [5000, 1200, 8500, 300, 4200],
    'CreditScore': [750, 580, 820, 450, 680],
    'TransactionFrequency': [15, 5, 25, 2, 12],
    'LoanAmount': [20000, 5000, 35000, 1000, 15000],
    'DefaultRisk': ['No', 'Yes', 'No', 'Yes', 'No']
}
df = pd.DataFrame(data)
X = df[['AccountBalance', 'CreditScore', 'TransactionFrequency']]
y = df['DefaultRisk']
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.3, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
new_student_df = pd.DataFrame([[1200, 580, 5]], columns=['AccountBalance', 'CreditScore', 'TransactionFrequency'])
prediction = model.predict(new_student_df)
print("Prediction for new customer:", prediction[0])