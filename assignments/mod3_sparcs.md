# Python Assignment: Descriptive Analytics on SPARCS 2022 Data

## Project Title: SPARCS Descriptive 2022

**Due Date:** [Insert Due Date]

---

### Objective:

In this assignment, you will load a portion of the 2022 SPARCS (Statewide Planning and Research Cooperative System) de-identified data. You will perform basic descriptive statistics and create visualizations based on the data. This will allow you to explore healthcare trends, patient demographics, and hospital performance metrics. 

By the end of this assignment, you will have uploaded your Python notebook and analysis to a GitHub repository named **"sparcs_descriptive_2022"**.

---

### Data Source:
The dataset can be found at: [Hospital Inpatient Discharges - SPARCS De-Identified 2022](https://health.data.ny.gov/Health/Hospital-Inpatient-Discharges-SPARCS-De-Identified/5dtw-tffi/about_data).

- We will use a subset of this dataset focusing on key fields, including:
  - Age Group
  - Gender
  - Length of Stay
  - Type of Admission
  - Total Charges
  - Total Costs
  - Discharge Year
  - Ethnicity
  - Race
  
A data dictionary explaining the fields is provided [here](https://health.data.ny.gov/api/views/5dtw-tffi/files/e6d93a8d-6ecd-419f-a282-f7c3e3537b17?download=true&filename=NYSDOH_SPARCS_De-Identified_Data_Dictionary_2022.pdf).

---

### Instructions:

1. **Setup your GitHub Repository**:
   - Create a GitHub repository named **sparcs_descriptive_2022**.
   - Your repository should include a `README.md` file explaining the analysis.

2. **Loading the Data**:
   - Use the dataset available from the link above, or download the file and load a subset of it into your Python environment using **Pandas**.
   - Ensure that the data includes the fields **Age Group**, **Gender**, **Length of Stay**, **Total Charges**, **Total Costs**, and **Type of Admission**.

3. **Basic Descriptive Statistics**:
   - Calculate the following basic statistics for **Length of Stay**, **Total Charges**, and **Total Costs**:
     - Mean
     - Median
     - Standard Deviation
     - Min/Max
     - Percentiles (25th, 50th, 75th)
     - Quartiles

4. **Exploring Categorical Variables**:
   - Count the distribution of **Age Group**, **Gender**, and **Type of Admission**.
   - Create a bar plot to visualize the counts of each category.

5. **Visualizations**:
   - Create at least 3 visualizations to summarize the dataset:
     - Histogram of **Length of Stay** to show its distribution.
     - Boxplot for **Total Charges** to identify outliers.
     - Bar plot for **Type of Admission** to analyze admission trends (e.g., Emergency, Elective, Trauma).

6. **Handling Missing Data**:
   - Check for missing data in the selected fields and handle it appropriately (e.g., drop rows with missing data or fill with the mean/median).

7. **Summary Report**:
   - Write a brief summary of your findings in the notebook:
     - What is the average length of stay?
     - How does the total cost vary by age group or type of admission?
     - Any noticeable trends in admissions or charges?

---

### Deliverables:
- A Python notebook (`.ipynb` or `.py` file) uploaded to a GitHub repository called **sparcs_descriptive_2022**.
- Your notebook should contain:
  - Data loading steps
  - Basic descriptive statistics
  - Visualizations
  - Summary of findings
- Include a `README.md` file explaining the project and how to run the notebook.
  
---

### Optional Extensions (Extra Credit):
- Analyze the **Ethnicity** and **Race** fields to explore healthcare disparities in total charges or length of stay.
- Use **seaborn** to create more advanced visualizations (e.g., heatmaps or pairplots).

---

### Submission:
- Submit the link to your GitHub repository.
- Ensure that all code, visualizations, and your final report are included.

---

### Resources:
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)

