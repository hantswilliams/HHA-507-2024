# Module 1 Homework Assignment: Discovering Medical Codexes within Synthetic Medicare Fee-for-Service Claims Data 

## Objective:
This assignment will help you gain hands-on experience in working with real-world-like (synthetic) healthcare data, focusing on the 'inpatient' Medicare fee-for-service claims dataset from CMS. You will learn how to load, analyze, and interpret medical codex data using Python.

## Instructions:

### 1. Create a GitHub Repository:
- Create a new GitHub repository. Name it `module1-codexes-claims-analysis`.

### 2. Loading the Data:
- Download the 'inpatient' Medicare fee-for-service claims data from the CMS Synthetic Data Collection: https://data.cms.gov/collection/synthetic-medicare-enrollment-fee-for-service-claims-and-prescription-drug-event (select the 'inpatient' dataset).
- The dataset is available in CSV format and contains information about Medicare fee-for-service claims, including patient demographics, diagnoses, procedures, and other relevant details.
- Write a Python script (either `analysis.py` or `analysis.ipynb` if you want to do it in a notebook) that loads this dataset into a Pandas DataFrame. 
- Explore the dataset to identify columns related to medical codexes (e.g., ICD codes, DRG codes, HCPCS codes).

### 3. Analyzing Medical Codex Data:
- Identify the different types of medical codexes present in the dataset.
- For each type of medical codex, calculate the frequency of each unique value.
- Determine if there are any missing or null values in the codex-related columns and handle them appropriately (e.g., filling them with a placeholder, excluding them from analysis).

### 4. Additional Analysis:
- Provide a summary of the most common codes found in the dataset.
- Analyze and report on any patterns or insights you observe in the codex data (e.g., are certain codes more prevalent in specific regions, times, or patient groups?).

### 5. Documenting Your Work:
- Create a `report.md` file in your GitHub repository.
- In `report.md`, explain:
  - The steps you took in your analysis.
  - The purpose of each part of your code.
  - Key findings from your analysis, including any patterns or anomalies you discovered.
  - Any challenges you faced and how you overcame them.
  - Reflect on the implications of your findings for healthcare providers and policy makers.

### 6. Submission:
- Push your `analysis.py` script and `report.md` to your GitHub repository.
- Submit the link to your GitHub repository through the course’s Brightspace assignment page.

### Errors and Exceptions:
- If you encounter any errors or exceptions during the analysis, document them in your `report.md` file and explain how you resolved them.
- If you are unable to complete any part of the assignment, document the reasons in your `report.md` file.
- You are graded not based on completion but on the effort, and understanding demonstrated in your work.

