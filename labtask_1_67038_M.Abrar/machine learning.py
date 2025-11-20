#Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
#Step 1: Create dataset
# Sample grocery dataset
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7],
    'WeeklyVisits': [2, 1, 3, 4, 1, 2, 5],
    'AvgSpend': [45, 120, 75, 35, 150, 90, 25],
    'LoyaltyScore': [3, 8, 5, 2, 9, 6, 1],
    'PreferredTime': ['Morning', 'Evening', 'Afternoon', 'Morning', 'Evening', 'Afternoon', 'Morning'],
    'HighValue': ['No', 'Yes', 'No', 'No', 'Yes', 'No', 'No']
}
df = pd.DataFrame(data)
#Define features (X) and target (y)
X = df[['CustomerID', 'AvgSpend', 'HighValue']]
y = df['HighValue']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)