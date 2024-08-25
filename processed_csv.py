import pandas as pd
import numpy as np

# reading the first source file - current year's data, updated online
current = pd.read_csv(
    'https://.../online-file.csv',  # path to the online EURPLN rates file
    encoding='latin1',
    sep=';'
)

# reading the second source file - last year's data (historical), stored locally
historical = pd.read_csv(
    'C:/.../historical-data.csv',  # path to the local file
    encoding='latin1',
    sep=';'
)

# keeping selected columns only; df.copy() not needed here as filtering already creates a new df
filtered_current = current[['data', '1EUR']]
filtered_historical = historical[['data', '1EUR']]

# combining the dataframes
data = pd.concat([filtered_historical, filtered_current], ignore_index=True)

# additional checks if needed:
# print(data.head()) # to make sure the date values start with last year
# print(data.tail()) # to make sure the date values end with current year

# renaming the columns
df = data.rename(
    columns={
        data.columns[0]: 'Date',
        data.columns[1]: 'EUR'
    }
)

# filtering the Date column to only contain rows with dates
df = df[df['Date'].str.startswith('202', na=False)]

# adding index values starting from 1 (for index starting from 0: adding .reset_index(drop=True) to the previous step would suffice)
df.index = np.arange(1, len(df)+1)

# converting values
df['EUR'] = df['EUR'].str.replace(',', '.')
df['EUR'] = pd.to_numeric(df['EUR'], errors='coerce')    # converting exchange rates to numbers
df['Date'] = pd.to_datetime(df['Date']).dt.date     # converting to date

# additional checks if needed:
# print(df[df['EUR'].isnull()])   # to double-check any potential nulls during conversion to numeric values
# print(df.dtypes)      # to double-check the data types

print(f'\nDate range: {df.Date.min()}/{ df.Date.max()}')    # to view the current date range

# saving as a csv file to the same directory with some parameters specified
output_file = "EUR_exchange_rates.csv"
df.to_csv(
    output_file,
    float_format='%.2f',  # keeping only two decimals for the numeric column
    index_label='Index'
)

# viewing the processed data
processed_csv = pd.read_csv("EUR_exchange_rates.csv")
print(processed_csv.head())