import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# Create a new synthetic dataset for proportions and ratios
np.random.seed(42)

"""

Male-to-Female Ratio
C-Section Rate
Mortality Rate
HAI Proportion
Patient-to-Nurse Ratio

"""

# Generate synthetic data for 30 days
data_proportions = {
    'Date': pd.date_range(start='2024-01-01', periods=30, freq='D'),
    'Total_Patients': np.random.randint(50, 100, size=30),
    'Male_Patients': np.random.randint(20, 50, size=30),
    'Female_Patients': np.random.randint(20, 50, size=30),
    'C_Sections': np.random.randint(5, 20, size=30),
    'Total_Deliveries': np.random.randint(20, 50, size=30),
    'Deaths': np.random.randint(1, 5, size=30),
    'HAIs': np.random.randint(1, 10, size=30),
    'Total_Nurses': np.random.randint(10, 20, size=30)
}

df_proportions = pd.DataFrame(data_proportions)

# Display the first few rows of the dataset
df_proportions.head()


# Function to calculate Male to Female Ratio
def calculate_male_to_female_ratio(male_patients, female_patients):
    return male_patients / female_patients

# Function to calculate C-Section Rate (as a proportion of total deliveries)
def calculate_c_section_rate(c_sections, total_deliveries):
    return (c_sections / total_deliveries) * 100

# Function to calculate Mortality Rate (as a proportion of total patients)
def calculate_mortality_rate(deaths, total_patients):
    return (deaths / total_patients) * 100

# Function to calculate Proportion of Hospital-Acquired Infections (HAIs)
def calculate_hai_proportion(hai, total_patients):
    return (hai / total_patients) * 100

# Function to calculate Patient-to-Nurse Ratio
def calculate_patient_to_nurse_ratio(total_patients, total_nurses):
    return total_patients / total_nurses


# Apply the functions to calculate various proportions and ratios
df_proportions['Male_to_Female_Ratio'] = calculate_male_to_female_ratio(df_proportions['Male_Patients'], df_proportions['Female_Patients'])
df_proportions['C_Section_Rate'] = calculate_c_section_rate(df_proportions['C_Sections'], df_proportions['Total_Deliveries'])
df_proportions['Mortality_Rate'] = calculate_mortality_rate(df_proportions['Deaths'], df_proportions['Total_Patients'])
df_proportions['HAI_Proportion'] = calculate_hai_proportion(df_proportions['HAIs'], df_proportions['Total_Patients'])
df_proportions['Patient_to_Nurse_Ratio'] = calculate_patient_to_nurse_ratio(df_proportions['Total_Patients'], df_proportions['Total_Nurses'])

# Display the updated dataset with calculated proportions and ratios
df_proportions[['Date', 'Male_to_Female_Ratio', 'C_Section_Rate', 'Mortality_Rate', 'HAI_Proportion', 'Patient_to_Nurse_Ratio']].head()






# Plot C-Section Rate and Mortality Rate over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='C_Section_Rate', data=df_proportions, label='C-Section Rate')
sns.lineplot(x='Date', y='Mortality_Rate', data=df_proportions, label='Mortality Rate')
plt.title('C-Section Rate and Mortality Rate Over Time')
plt.ylabel('Rate (%)')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.legend()
plt.show()
