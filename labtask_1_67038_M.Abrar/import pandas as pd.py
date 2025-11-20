import pandas as pd

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
