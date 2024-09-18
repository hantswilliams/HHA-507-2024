import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = 'mysql+pymysql://your_username:your_password@your_remote_host:3306/your_database'

engine = create_engine(DATABASE_URL)

## Without f-string
age_threshold = 30
query = "SELECT * FROM users WHERE age > %s;"
result_df = pd.read_sql(query, engine, params=[age_threshold])
print(result_df)

## With f-string
age_threshold = 30
query = f"SELECT * FROM users WHERE age > {age_threshold};"
result_df = pd.read_sql(query, engine)
print(result_df)

## Using f-string with multiple variables
age_threshold = 30
name = 'Alice'
query = f"SELECT * FROM users WHERE age > {age_threshold} AND name = '{name}';"
result_df = pd.read_sql(query, engine)
print(result_df)

## Looping through a list of values
age_thresholds = [25, 30, 35]
for age_threshold in age_thresholds:
    query = f"SELECT * FROM users WHERE age > {age_threshold};"
    result_df = pd.read_sql(query, engine)
    print(result_df)

## Using f-string with a complex query
age_threshold = 30
query = f"""
    SELECT 
        age, 
        AVG(salary) as avg_salary, 
        COUNT(*) as num_users 
    FROM users
    WHERE age > {age_threshold}
    GROUP BY age
    ORDER BY avg_salary DESC;
"""
result_df = pd.read_sql(query, engine)

