import pandas as pd
import numpy as np

# Generate a synthetic dataset
np.random.seed(42)

"""

This generates 30 days of synthetic data for:

Total beds, occupied beds
Total rooms, occupied rooms
Outpatient visits, admissions, discharges, and inpatient service days

"""

# Number of beds and rooms available over a period of time (e.g., a month)
data = {
    'Date': pd.date_range(start='2024-01-01', periods=30, freq='D'),
    'Total_Beds': np.random.randint(150, 200, size=30),
    'Occupied_Beds': np.random.randint(100, 180, size=30),
    'Total_Rooms': np.random.randint(100, 120, size=30),
    'Occupied_Rooms': np.random.randint(80, 110, size=30),
    'Outpatient_Visits': np.random.randint(50, 100, size=30),  # Outpatient visits to be used for Adjusted Occupancy Rate
    'Admissions': np.random.randint(5, 20, size=30),
    'Discharges': np.random.randint(5, 20, size=30),
    'Inpatient_Service_Days': np.random.randint(100, 250, size=30)
}

df = pd.DataFrame(data)

# Display the first few rows of the dataset
df.head()

# Function to calculate Inpatient Bed Occupancy Rate
def calculate_bed_occupancy_rate(occupied_beds, total_beds):
    return (occupied_beds / total_beds) * 100

# Function to calculate Room Occupancy Rate
def calculate_room_occupancy_rate(occupied_rooms, total_rooms):
    return (occupied_rooms / total_rooms) * 100

# Function to calculate Adjusted Occupancy Rate (includes outpatient visits)
def calculate_adjusted_occupancy_rate(occupied_beds, total_beds, outpatient_visits):
    total_occupancy = occupied_beds + outpatient_visits
    return (total_occupancy / total_beds) * 100

# Function to calculate Bed Turnover Rate
def calculate_bed_turnover_rate(discharges, total_beds):
    return discharges / total_beds


# Create a blank reporting dataframe
reporting_df = pd.DataFrame()

# Add in date column
reporting_df['Date'] = df['Date']

# Apply the functions to calculate different occupancy rates
reporting_df['Bed_Occupancy_Rate'] = calculate_bed_occupancy_rate(df['Occupied_Beds'], df['Total_Beds'])
reporting_df['Room_Occupancy_Rate'] = calculate_room_occupancy_rate(df['Occupied_Rooms'], df['Total_Rooms'])
reporting_df['Adjusted_Occupancy_Rate'] = calculate_adjusted_occupancy_rate(df['Occupied_Beds'], df['Total_Beds'], df['Outpatient_Visits'])
reporting_df['Bed_Turnover_Rate'] = calculate_bed_turnover_rate(df['Discharges'], df['Total_Beds'])

# Display the updated dataset with occupancy rates
reporting_df[['Date', 'Bed_Occupancy_Rate', 'Room_Occupancy_Rate', 'Adjusted_Occupancy_Rate', 'Bed_Turnover_Rate']].head()
