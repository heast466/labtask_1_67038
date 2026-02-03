import pandas as pd
from scipy.stats import ttest_1samp

# 1. Load the dataset
data = pd.read_csv("ACCIDENTS_GU_BCN_2013.csv", encoding="latin1")

# 2. Create 'Date' column with dummy year
data['Date'] = data['Dia de mes'].astype(str) + '-' + data['Mes de any'].astype(str) + '-2013'
data['Date'] = pd.to_datetime(data['Date'], format="%d-%m-%Y")

# 3. Count accidents per day
daily_accidents = data.groupby('Date').size()

# 4. Take a sample of 100 daily accident counts
sample = daily_accidents.sample(n=100, random_state=1)

# 5. One-sample Hypothesis Test
data_for_test = sample

# H0: mean daily accidents = test_value
test_value = 50

t_stat, p_value = ttest_1samp(data_for_test, test_value)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# Decision Rule
alpha = 0.05
if p_value < alpha:
    print("Reject H0: Mean accidents is NOT equal to", test_value)
else:
    print("Fail to Reject H0: Mean accidents may be", test_value)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp


# 0. Load dataset
data = pd.read_csv("ACCIDENTS_GU_BCN_2013.csv", encoding="latin1")
data.columns = data.columns.str.strip()

# Create 'Date' column with dummy year 2013
data['Date'] = data['Dia de mes'].astype(str) + '-' + data['Mes de any'].astype(str) + '-2013'
data['Date'] = pd.to_datetime(data['Date'], format="%d-%m-%Y")

# Count accidents per day
daily_accidents = data.groupby('Date').size()


# 1. Describe daily accidents

print("Descriptive statistics for daily accidents:")
print(daily_accidents.describe())

plt.hist(daily_accidents, bins=20, edgecolor='black')
plt.title("Histogram of Daily Traffic Accidents in Barcelona 2013")
plt.xlabel("Number of Accidents")
plt.ylabel("Frequency")
plt.show()


# 2. Empirical sample distribution of the mean

s = 1000  # number of samples
n = 500   # sample size
sample_means = []

for _ in range(s):
    sample = daily_accidents.sample(n, replace=True)  # sampling with replacement
    sample_means.append(sample.mean())

sample_means = np.array(sample_means)

plt.hist(sample_means, bins=30, edgecolor='black')
plt.title("Empirical Sampling Distribution of Mean (s=1000, n=500)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()


# 3. Standard Error (SE)

one_sample = daily_accidents.sample(n, replace=True, random_state=1)
se_direct = one_sample.std() / np.sqrt(n)

# 3b. SE from 1000 simulated samples
se_simulated = np.std(sample_means, ddof=1)

print("Direct estimate of SE from one sample:", se_direct)
print("Estimated SE from 1000 samples:", se_simulated)

# 4. Bootstrap

B = 1000  # number of bootstrap resamples
bootstrap_means = []

for _ in range(B):
    bootstrap_sample = daily_accidents.sample(n, replace=True)
    bootstrap_means.append(bootstrap_sample.mean())

bootstrap_means = np.array(bootstrap_means)

plt.hist(bootstrap_means, bins=30, edgecolor='black')
plt.title("Bootstrap Sampling Distribution of Mean")
plt.xlabel("Bootstrap Sample Mean")
plt.ylabel("Frequency")
plt.show()

bootstrap_se = np.std(bootstrap_means, ddof=1)
print("Bootstrap estimate of SE:", bootstrap_se)
