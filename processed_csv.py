import pandas as pd  # type: ignore

# reading the source file
data = pd.read_csv(
    'https://.../online-file.csv',  # online EURPLN rate file that will be processed
    encoding='latin1',
    sep=';'
)

# working on a copy
df = data.copy()

# keeping selected columns only
df = df[['data', '1EUR']]

# renaming the columns
df = df.rename(
    columns={
        df.columns[0]: 'Date', df.columns[1]: 'EUR'
    }
)

# filtering the Date column to only contain rows with dates
df = df[df['Date'].str.contains('202', na=False)].reset_index(drop=True)

# converting values
df['EUR'] = df['EUR'].str.replace(',', '.')
df['EUR'] = pd.to_numeric(df['EUR'])    # converting exchange rates to numbers
df['Date'] = pd.to_datetime(df['Date']).dt.normalize()  # converting to date but keeping the datetime type by normalizing

print(df.dtypes)  # to double-check the data types
print(f'\nDate range: {df.Date.min()}/{ df.Date.max()}')    # to view the current date range

# saving as a csv file to the same directory with some parameters specified
df.to_csv(
    "EUR_exchange_rates_2024.csv",
    float_format='%.2f',  # keeping only two decimals for the numeric column
    index_label='Index'
)

# viewing the processed data
processed_csv = pd.read_csv("EUR_exchange_rates_2024.csv")
print(processed_csv.head())