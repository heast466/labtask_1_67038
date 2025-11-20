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

df['HighValueEncoded'] = df['HighValue'].map({'No': 0, 'Yes': 1})

# Correlation analysis
print("Correlation Matrix:")
print(df[['WeeklyVisits', 'AvgSpend', 'LoyaltyScore', 'HighValueEncoded']].corr())


high_spenders = df[df["AvgSpend"] > 100]
print("\nHigh Spenders (>$100):")
print(high_spenders[['CustomerID', 'AvgSpend', 'LoyaltyScore']])

frequent_buyers = df[df["WeeklyVisits"] >= 3]
print("\nFrequent Buyers (3+ visits/week):")
print(frequent_buyers[['CustomerID', 'WeeklyVisits', 'AvgSpend']])

low_loyalty = df[df["LoyaltyScore"] < 3]
print("\nLow Loyalty Customers:")
print(low_loyalty[['CustomerID', 'LoyaltyScore', 'AvgSpend']])