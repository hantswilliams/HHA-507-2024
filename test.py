import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate synthetic data for medical treatment response time with a left-skewed distribution
np.random.seed(42)
fake_response_times = np.random.beta(a=4, b=-1, size=1000) * 10  # Left-skewed data for treatment response times (in days)

# Create a histogram to visualize the left-skewed distribution of medical treatment response times
plt.figure(figsize=(10, 6))
sns.histplot(fake_response_times, bins=30, kde=True, color='red')
plt.title('Left-Skewed Distribution of Medical Treatment Response Times')
plt.xlabel('Response Time (Days)')
plt.ylabel('Frequency')
plt.show()





