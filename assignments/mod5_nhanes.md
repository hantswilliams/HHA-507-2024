# NHANES 2021-2023 Inferential Analytics Assignment

## Objective

In this assignment, you will use NHANES data to perform basic inferential statistics using Python in Google Colab. You will explore relationships and differences in health metrics and demographic variables, utilizing the skills learned in class to answer key questions about the dataset. Your final analysis should be saved as a Google Colab notebook and uploaded to a GitHub repository.

- NHANES Data: [NHANES 2021-2023](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2021-2023)

## Data Preparation

To start, you’ll use the following NHANES variables for analysis:

- **Marital Status** (`DMDMARTZ`) - categorical, needs recoding (married or not married).
- **Education Level** (`DMDEDUC2`) - categorical, needs recoding (bachelor’s or higher vs. less than bachelor’s).
- **Age in Years** (`RIDAGEYR`) - continuous.
- **Systolic Blood Pressure** (`BPXOSY3`) - continuous.
- **Diastolic Blood Pressure** (`BPXODI3`) - continuous.
- **Vitamin D Lab Interpretation** (`LBDVD2LC`) - categorical, two levels.
- **Hepatitis B Lab Antibodies** (`LBXHBS`) - categorical, needs recoding to two levels.
- **Weak/Failing Kidneys** (`KIQ022`) - categorical, can be treated as two levels.
- **Minutes of Sedentary Behavior** (`PAD680`) - continuous, needs cleaning (remove values `7777`, `9999`, and null).
- **Current Self-Reported Weight** (`WHD020`) - continuous, needs cleaning (remove values `7777`, `9999`, and null).

> **Note**: Ensure you clean the data before performing analyses. For **categorical variables**, check and document frequency counts to confirm data consistency. For **continuous variables**, be mindful of placeholder values (`7777`, `9999`) and handle these as appropriate (e.g., by removing or imputing).

## Instructions

1. **Create Your GitHub Repository**
   - Create a new GitHub repository titled `nhanes_inferential_2023`.
   - Include a `README.md` file that briefly describes the project and the analysis you are performing.

2. **Complete the Analysis in Google Colab**
   - Use Google Colab to conduct your analysis. Your notebook should be well-documented with explanations of each step just as like we have done in the class notebooks.

3. **Questions for Analysis**

   Use the questions below to guide your analysis. Remember to transform or recode variables where needed as specified, but determine the appropriate statistical tests on your own.

   - **Question 1**: "Is there an association between marital status (married or not married) and education level (bachelor’s degree or higher vs. less than a bachelor’s degree)?"  
     - Variables: `DMDMARTZ` (marital status) and `DMDEDUC2` (education level). Recode as specified.

   - **Question 2**: "Is there a difference in the mean sedentary behavior time between those who are married and those who are not married?"  
     - Variables: `DMDMARTZ` (marital status, recoded) and `PAD680` (sedentary behavior time, cleaned).

   - **Question 3**: "How do age and marital status affect systolic blood pressure?"  
     - Variables: `RIDAGEYR` (age), `DMDMARTZ` (marital status, recoded), and `BPXOSY3` (systolic blood pressure).

   - **Question 4**: "Is there a correlation between self-reported weight and minutes of sedentary behavior?"  
     - Variables: `WHD020` (self-reported weight, cleaned) and `PAD680` (sedentary behavior time, cleaned).

   - **Question 5 (Creative Analysis)**: Develop your own unique question using at least one of the variables listed above. Ensure that your question can be answered using one of the following tests: chi-square, t-test, ANOVA, or correlation. Clearly state your question, explain why you chose the test, and document your findings.

4. **Deliverables**

   - A completed Google Colab notebook (`.ipynb` file) with:
     - Data loading and preparation steps
     - Analysis and any transformations
     - Visualizations of descriptives/results (if relevant)
     - Brief summaries of your findings for each question
   - Submit the link to your GitHub repository titled `nhanes_inferential_2023`.

---

Ensure your repository is public or accessible by link, and confirm that all code, results, and any explanations are documented clearly within your notebook.

If you have any issues or run into errors, please be sure to screen shot the error message and include it in your notebook. This will help us understand the problem and provide guidance on how to resolve it. Do not NOT submit because of errors. 
