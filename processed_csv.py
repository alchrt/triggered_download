import pandas as pd
import numpy as np

# reading the source file
data = pd.read_csv(
    'https://static.nbp.pl/dane/kursy/Archiwum/archiwum_tab_a_2024.csv',  # online EURPLN rate file that will be processed
    encoding='latin1',
    sep=';'
)

# keeping selected columns only; df.copy() not needed here as filtering already creates a new df
df = data[['data', '1EUR']]

# renaming the columns
df = df.rename(
    columns={
        df.columns[0]: 'Date',
        df.columns[1]: 'EUR'
    }
)

# filtering the Date column to only contain rows with dates
df = df[df['Date'].str.startswith('202', na=False)]

# adding an index value starting from 1 (for index starting from 0: adding .reset_index(drop=True) to the previous step would suffice)
df.index = np.arange(1, len(df)+1)

# converting values
df['EUR'] = df['EUR'].str.replace(',', '.')
df['EUR'] = pd.to_numeric(df['EUR'], errors='coerce')    # converting exchange rates to numbers
df['Date'] = pd.to_datetime(df['Date']).dt.date     # converting to date

print(df.dtypes)  # to double-check the data types
print(f'\nDate range: {df.Date.min()}/{ df.Date.max()}')    # to view the current date range

# saving as a csv file to the same directory with some parameters specified
output_file = "EUR_exchange_rates_2024.csv"
df.to_csv(
    output_file,
    float_format='%.2f',  # keeping only two decimals for the numeric column
    index_label='Index'
)

# viewing the processed data
processed_csv = pd.read_csv("EUR_exchange_rates_2024.csv")
print(processed_csv.head())