import pandas as pd
#Sample dataset
data = {
    'CustomerID': [201, 202, 203, 204, 205],
    'AccountBalance': [5000, 1200, 8500, 300, 4200],
    'CreditScore': [750, 580, 820, 450, 680],
    'TransactionFrequency': [15, 5, 25, 2, 12],
    'LoanAmount': [20000, 5000, 35000, 1000, 15000],
    'DefaultRisk': ['No', 'Yes', 'No', 'Yes', 'No']
}
df = pd.DataFrame(data)
df['DefaultRiskEncoded'] = df['DefaultRisk'].map({'No': 0, 'Yes': 1})
print("Correlation Matrix:")
print(df.corr(numeric_only=True))
at_risk_pattern = df[df["AccountBalance"] < 1000]
print(at_risk_pattern)