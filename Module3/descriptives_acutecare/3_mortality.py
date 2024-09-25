import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Create a new synthetic dataset for mortality-related rates
np.random.seed(42)

# Generate synthetic data for 30 days
data_mortality = {
    'Date': pd.date_range(start='2024-01-01', periods=30, freq='D'),
    'Total_Discharges': np.random.randint(50, 100, size=30),    # Total discharges per day
    'Total_Deaths': np.random.randint(1, 5, size=30),           # Total deaths per day
    'Deaths_within_48_hours': np.random.randint(0, 2, size=30), # Deaths within 48 hours of admission
    'Inpatient_Autopsies': np.random.randint(0, 3, size=30)     # Number of inpatient autopsies
}

df_mortality = pd.DataFrame(data_mortality)

# Display the first few rows of the dataset
df_mortality.head()

# Function to calculate Gross Death Rate (deaths over total discharges)
def calculate_gross_death_rate(total_deaths, total_discharges):
    return (total_deaths / total_discharges) * 100

# Function to calculate Net Death Rate (excludes deaths within 48 hours)
def calculate_net_death_rate(total_deaths, deaths_within_48_hours, total_discharges):
    return ((total_deaths - deaths_within_48_hours) / total_discharges) * 100

# Function to calculate Autopsy Rate (autopsies over total deaths)
def calculate_autopsy_rate(inpatient_autopsies, total_deaths):
    return (inpatient_autopsies / total_deaths) * 100


# Apply the functions to calculate the mortality-related rates
df_mortality['Gross_Death_Rate'] = calculate_gross_death_rate(df_mortality['Total_Deaths'], df_mortality['Total_Discharges'])
df_mortality['Net_Death_Rate'] = calculate_net_death_rate(df_mortality['Total_Deaths'], df_mortality['Deaths_within_48_hours'], df_mortality['Total_Discharges'])
df_mortality['Autopsy_Rate'] = calculate_autopsy_rate(df_mortality['Inpatient_Autopsies'], df_mortality['Total_Deaths'])

# Display the updated dataset with calculated rates
df_mortality[['Date', 'Gross_Death_Rate', 'Net_Death_Rate', 'Autopsy_Rate']].head()







# Plot Gross and Net Death Rates over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Gross_Death_Rate', data=df_mortality, label='Gross Death Rate')
sns.lineplot(x='Date', y='Net_Death_Rate', data=df_mortality, label='Net Death Rate')
plt.title('Gross and Net Death Rates Over Time')
plt.ylabel('Rate (%)')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.legend()
plt.show()
