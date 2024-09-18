import pandas as pd
from sqlalchemy import create_engine

# Step 1: Define the connection string to the remote MySQL database
DATABASE_URL = 'mysql+pymysql://your_username:your_password@your_remote_host:3306/your_database'

# Step 2: Create the engine to connect to the database
engine = create_engine(DATABASE_URL)

# Step 3: Slightly complex SQL query
query = """
    SELECT 
        age, 
        AVG(salary) as avg_salary, 
        COUNT(*) as num_users 
    FROM users
    WHERE age > 25
    GROUP BY age
    ORDER BY avg_salary DESC;
"""

# Step 4: Use Pandas to execute the SQL query and fetch the result into a DataFrame
result_df = pd.read_sql(query, engine)

# Step 5: Display the result DataFrame
print(result_df)
