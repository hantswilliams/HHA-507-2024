# Homework Assignment: Healthcare Data Exploration with SQLite and Pandas

## Objective: 
In this assignment, you will explore a publicly available healthcare dataset, load it into a local SQLite database, and apply SQL queries using Python with Pandas. You will practice using SQLite, SQL queries, and Pandas for simple data exploration and analysis.

### Step 1: Find a Public Healthcare Dataset
- Find a publicly available healthcare dataset that interests you. You can use resources like Kaggle, data.gov, CMS, CDC, WHO, etc.
- Download the dataset in CSV format. Ensure that the dataset contains columns you can use for meaningful analysis

### Step 2: Set Up a Local SQLite Database
- Create a new SQLite database file (e.g., `healthcare.db`) using the Python `sqlite3` library.
- Use Pandas to load your dataset into the SQLite database. Use the pd.to_sql() method to create the table in the database.

### Step 3: Perform SQL Queries Using SQLite and Pandas
- Write SQL queries to explore and analyze the data in your SQLite database:
    - Query 1: Select all records based on a specific filter of your choice (e.g., a particular value in one of the columns).
    - Query 2: Count the number of records that meet a certain condition (e.g., count the number of entries for a specific category).
    - Query 3: Group the data by a specific column and calculate a summary statistic (e.g., average, sum, count) for each group.
    - Query 4: Sort the records based on a numerical or categorical field and return a limited set of results (e.g., top 5 records).

### Step 4: Submit Your Work
- Create a new GitHub repository called `sqlite_dataexploration` to store your project.
- Push your Jupyter Notebook or Python script that contains the SQL queries and Pandas code.
- Do NOT upload the healthcare dataset to the repository. Instead, provide a link to the original dataset in your README file.
- Add a `.gitignore` file to ensure the dataset (CSV) and SQLite database file are excluded from your repository.
- Example .gitignore file:
    ```
    *.csv
    *.db
    ```
- Submit the link to your GitHub repository through the course's Brightspace assignment page.


