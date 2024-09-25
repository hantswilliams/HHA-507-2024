import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a new synthetic dataset for admissions and discharge rates
np.random.seed(42)

# Generate synthetic data for 30 days
data = {
    'Date': pd.date_range(start='2024-01-01', periods=30, freq='D'),
    'Total_Beds': np.random.randint(150, 200, size=30),
    'Admissions': np.random.randint(10, 50, size=30),   # Admissions per day
    'Discharges': np.random.randint(10, 50, size=30),   # Discharges per day
    'Readmissions': np.random.randint(1, 5, size=30),   # Readmissions per day
    'Inpatient_Service_Days': np.random.randint(100, 250, size=30),  # Total inpatient service days per day
    'LOS': np.random.randint(1, 10, size=30)  # Length of Stay in days for each patient
}

df_ad_dis = pd.DataFrame(data)

# Display the first few rows of the dataset
df_ad_dis.head()

# Function to calculate Admission Rate (admissions over total beds)
def calculate_admission_rate(admissions, total_beds):
    return (admissions / total_beds) * 100

# Function to calculate Discharge Rate (discharges over total beds)
def calculate_discharge_rate(discharges, total_beds):
    return (discharges / total_beds) * 100

# Function to calculate Readmission Rate (readmissions over admissions)
def calculate_readmission_rate(readmissions, admissions):
    return (readmissions / admissions) * 100

# Function to calculate Average Length of Stay (ALOS) over the period
def calculate_alos(inpatient_service_days, discharges):
    return inpatient_service_days / discharges


# Apply the functions to calculate various rates
df_ad_dis['Admission_Rate'] = calculate_admission_rate(df_ad_dis['Admissions'], df_ad_dis['Total_Beds'])
df_ad_dis['Discharge_Rate'] = calculate_discharge_rate(df_ad_dis['Discharges'], df_ad_dis['Total_Beds'])
df_ad_dis['Readmission_Rate'] = calculate_readmission_rate(df_ad_dis['Readmissions'], df_ad_dis['Admissions'])
df_ad_dis['ALOS'] = calculate_alos(df_ad_dis['Inpatient_Service_Days'], df_ad_dis['Discharges'])

# Display the updated dataset with calculated rates
df_ad_dis[['Date', 'Admission_Rate', 'Discharge_Rate', 'Readmission_Rate', 'ALOS']].head()





# Plot Admission and Discharge Rates over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Admission_Rate', data=df_ad_dis, label='Admission Rate')
sns.lineplot(x='Date', y='Discharge_Rate', data=df_ad_dis, label='Discharge Rate')
plt.title('Admission and Discharge Rates Over Time')
plt.ylabel('Rate (%)')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.legend()
plt.show()
