import pandas as pd 
import polars as pl
import time

datafile_location = 'Module3/sparcs/sparcs_2022.csv'

## with pandas 
start = time.time()
df = pd.read_csv(datafile_location)
end = time.time()
print(f"Time taken to read data with pandas: {end-start}")
df

## with polars
start = time.time()
### schema for Length of Stay should be string
df = pl.read_csv(datafile_location, schema={
    "Length of Stay": pl.Categorical
})
end = time.time()
print(f"Time taken to read data with polars: {end-start}")
df
