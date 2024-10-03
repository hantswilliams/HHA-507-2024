import pandas as pd 
import time 

## change default to not display exponential notation but float
pd.set_option('display.float_format', lambda x: '%.3f' % x)

start_time = time.time()
df = pd.read_csv('./Module3/sparcs/sparcs_2022.csv')
end_time = time.time()
load_time = end_time - start_time
print(f"Time to load data: {load_time} seconds")

### First step: cleaning column names
## remove all white space, lower case, replace space with underscore
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '_')
df_len = len(df)

## remove commas from total_charges and total_costs
df.total_charges = df.total_charges.apply(lambda x : x.replace(',',''))
df.total_costs = df.total_costs.apply(lambda x : x.replace(',',''))

## convert total_charges and total_costs to numeric
df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')
df['total_costs'] = pd.to_numeric(df['total_costs'], errors='coerce')

## count nan for total_charges and total_costs
df['total_charges'].isna().sum()
df['total_costs'].isna().sum()


### Second step: keep only data that we want 
## filter so we only look at Suffolk and Nassau county 
df_suffolk_nassau = df[(df.hospital_county == 'Suffolk') | (df.hospital_county == 'Nassau')]
len(df_suffolk_nassau)
df_len_suf_nas = len(df_suffolk_nassau)

suffolk = df_suffolk_nassau[df_suffolk_nassau.hospital_county == 'Suffolk']
nassau = df_suffolk_nassau[df_suffolk_nassau.hospital_county == 'Nassau']

## now delete df
del(df)

## ratio of suff/nas to total
(df_len_suf_nas / df_len) * 100

## proportion of suffolk to nassau
(len(suffolk) / (len(nassau) + len(suffolk)))

## hospitals 
suffolk['facility_name'].value_counts()
nassau['facility_name'].value_counts()

## apr_drg_code
suffolk['apr_drg_description'].value_counts().head(10)
nassau['apr_drg_description'].value_counts()

## total_charges
suffolk['total_charges'].describe()
nassau['total_charges'].describe()
