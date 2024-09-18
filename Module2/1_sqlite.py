import pandas as pd
import sqlite3

# Step 1: Create a connection to SQLite database
conn = sqlite3.connect('test_database.db')

# Step 2: Create a Pandas DataFrame
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [30, 25, 35]
}
df = pd.DataFrame(data)

# Step 3: Save the DataFrame to the SQLite database
df.to_sql('users', conn, if_exists='replace', index=False)

# Step 4: Query the table to verify the data
query = 'SELECT * FROM users'
result_df = pd.read_sql(query, conn)

# Step 5: Display the result
print(result_df)

# Close the connection
conn.close()
