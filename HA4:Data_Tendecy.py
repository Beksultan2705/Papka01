//Explain the major central and variance of data (like Percentiles, Standard Deviation, Variance, Correlation, Correlation Matrix, Correlation vs Causality) with python code and submit the python practice file.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

//Generate sample data
np.random.seed(0)
data = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])

//Percentiles
percentiles = np.percentile(data, [25, 50, 75])
print("Percentiles:")
print(percentiles)

//Standard deviation
std_dev = data.std()
print("\nStandard Deviation:")
print(std_dev)

//Variance
variance = data.var()
print("\nVariance:")
print(variance)

//Correlation
correlation = data.corr()
print("\nCorrelation Matrix:")
print(correlation)

//Visualization of Correlation Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

//Correlation vs Causality
print("\nCorrelation does not imply causation.")
