# CSV file update

This solution was created for financial tracking purposes. I needed to have an updated local version of an online file with information on exchange rates (updated online every business day). However, I did not need the update for ym local file to happen daily or automatically in the background - I needed it to happen when I specifically checked or updated my tracker, and only when triggered (VBA macro assigned to trigger the execution of the specified Python script).

## Option 1: triggered download with full transformation in Power Query
Python script for downloading and replacing the file: [csv_download.py](https://github.com/alchrt/triggered_download/blob/main/csv_download.py)  
VBA macro to run the Python script: [run_python_macro.vb](https://github.com/alchrt/triggered_download/blob/main/run_python_macro.vb)  

Basic transformations done in Power Query: row filtering, column renaming, punctuation change, column type change. This was done for both historical data in a separate file as well as the updated local file with current year's data. The data was then appended into a single table with an additional index added.  

## Option 2: triggered download with full transformation in Python, then load in Power Query
Python script with transformations: [processed_csv.py](https://github.com/alchrt/triggered_download/blob/main/processed_csv.py)  
VBA macro to run the Python script: [run_python_macro.vb](https://github.com/alchrt/triggered_download/blob/main/run_python_macro.vb)

The processing in Python mirrors the transformations done in Power Query in Option 1.
