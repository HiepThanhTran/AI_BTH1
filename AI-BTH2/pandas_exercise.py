import pandas as pd

filename = 'data.tsv'

# 1. Show the first 5 lines of the TSV file
try:
    with open(filename, 'r') as f:
        for i in range(5):
            line = f.readline()
            print(line.strip())
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# 2. Find the number of rows and columns using read_csv with a sample
try:
    df = pd.read_csv(filename, nrows=1, delimiter='\t')  # Read only 1 row for efficiency
    num_rows, num_cols = df.shape
    print(f"Number of rows: {num_rows}")
    print(f"Number of columns: {num_cols}")
except pd.errors.EmptyDataError:
    print("The file is empty or has no valid data.")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# 3. Print the name of the columns
try:
    df = pd.read_csv(filename, delimiter='\t')
    column_names = df.columns.tolist()
    print("Column names:", column_names)
except pd.errors.EmptyDataError:
    print("The file is empty or has no valid data.")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# 4. What is the type of the column names?
try:
    df = pd.read_csv(filename, delimiter='\t')
    column_names_type = type(df.columns)
    print(f"Type of column names: {column_names_type}")  # Output: <class 'pandas.core.indexes.base.Index'>
except pd.errors.EmptyDataError:
    print("The file is empty or has no valid data.")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# 5. Get the country column and save it to a variable. Show the first 5 observations.
try:
    df = pd.read_csv(filename, delimiter='\t')
    country_column = df['country']
    print("First 5 observations of 'country':")
    print(country_column.head())
except pd.errors.EmptyDataError:
    print("The file is empty or has no valid data.")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except KeyError:
    print("The 'country' column does not exist in the file.")

# 6. Show the last 5 observations of the country column
try:
    df = pd.read_csv(filename, delimiter='\t')
    country_column = df['country']
    print("Last 5 observations of 'country':")
    print(country_column.tail())
except pd.errors.EmptyDataError:
    print("The file is empty or has no valid data.")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except KeyError:
    print("The 'country' column does not exist in the file.")

# 7. Look at country, continent, and year. Show the first 5 and last 5 observations.
try:
    df = pd.read_csv(filename, delimiter='\t')
    selected_columns = ['country', 'continent', 'year']
    if all(col in df.columns for col in selected_columns):
        print("First 5 observations of 'country', 'continent', and 'year':")
        print(df[selected_columns].head())
        print("Last 5 observations of 'country', 'continent', and 'year':")
        print(df[selected_columns].tail())
    else:
        missing_cols = [col for col in selected_columns if col not in df.columns]
        print(f"Columns '{', '.join(missing_cols)}' not found in the file.")
except pd.errors.EmptyDataError:
    print("The file is empty or has no valid data.")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")


# Error handling for file operations
def handle_file_errors(error_type, filename):
    if isinstance(error_type, pd.errors.EmptyDataError):
        print("The file is empty or has no valid data.")
    elif isinstance(error_type, FileNotFoundError):
        print(f"Error: File '{filename}' not found.")
    else:
        print(f"An unexpected error occurred: {error_type}")


# 8. Get the first row of the TSV file using two methods:
try:
    df = pd.read_csv(filename, delimiter='\t')
    print("First row using .head(1):")
    print(df.head(1))
    print("First row using .iloc[0]:")
    print(df.iloc[0])
except Exception as e:  # Catch any exception related to file operations
    handle_file_errors(e, filename)

# 9. Get the first column and first/last column by integer index:
try:
    df = pd.read_csv(filename, delimiter='\t')
    print("First column:")
    print(df.iloc[:, 0])  # Access all rows, column index 0
    print("First and last columns:")
    first_col = df.iloc[:, 0]
    last_col = df.iloc[:, -1]
    print(pd.concat([first_col, last_col], axis=1))  # Combine into DataFrame
except Exception as e:
    handle_file_errors(e, filename)

# 10. Get the last row using .loc and negative indexing:
try:
    df = pd.read_csv(filename, delimiter='\t')
    print("Last row using .loc[-1]:")
    print(df.loc[-1])  # Using -1 for the last index
except Exception as e:
    handle_file_errors(e, filename)

# 11. Select the first, 100th, and 1000th rows using .iloc and .loc:
try:
    df = pd.read_csv(filename, delimiter='\t')
    print("First, 100th, 1000th rows using .iloc:")
    print(df.iloc[[0, 99, 999]])  # Access rows 0, 99, 999 (handle potential IndexError)
    print("First, 100th, 1000th rows using .loc (assuming index starts from 0):")
    print(df.loc[[0, 99, 999]])  # Access rows 0, 99, 999 (handle potential KeyError)
except IndexError:
    print("The file may not have 1000 rows.")
except KeyError:
    print("The file may not have an index starting from 0 or may not have 1000 rows.")
except Exception as e:
    handle_file_errors(e, filename)

# 12. Get the 43rd country using .loc and .iloc (assuming 'country' is a column):
try:
    df = pd.read_csv(filename, delimiter='\t')
    if 'country' in df.columns:
        print("43rd country using .loc (assuming index starts from 0):")
        print(df.loc[42, 'country'])  # Access row 42 (zero-based), 'country' column
        print("43rd country using .iloc:")
        print(df.iloc[42, df.columns.get_loc('country')])  # Access row 42, 'country' column index
    else:
        print("The 'country' column does not exist in the file.")
except Exception as e:
    handle_file_errors(e, filename)

# 13. Get the first, 100th, 1000th rows from the first, 4th and 6th columns:
try:
    df = pd.read_csv(filename, delimiter='\t')
    cols = [0, 3, 5]  # First, 4th, and 6th columns (zero-based indexing)

    # Define desired rows (manage potential IndexError)
    desired_rows = [0, 99]
    try:
        desired_rows.append(999)
    except IndexError:
        print("The file may not have 1000 rows.")

    # Select the subset using .iloc
    subset = df.iloc[desired_rows, cols]

    print("Subset of specified rows and columns:")
    print(subset)

except Exception as e:
    handle_file_errors(e, filename)

# 14. Get the first 10 rows of your data
try:
    df = pd.read_csv(filename, delimiter='\t')
    print("First 10 rows:")
    print(df.head(10))
except pd.errors.EmptyDataError:
    print("The file is empty or has no valid data.")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# 15. Average life expectancy for each year
try:
    df = pd.read_csv(filename, delimiter='\t')
    if 'year' in df.columns:  # Check if 'year' column exists
        print("Average life expectancy for each year:")
        print(df.groupby('year')['life_expectancy'].mean())  # Group by year and calculate mean
    else:
        print("The 'year' column does not exist in the file.")
except pd.errors.EmptyDataError:
    print("The file is empty or has no valid data.")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# 16. Subsetting method for average life expectancy (alternative to 15)
try:
    df = pd.read_csv(filename, delimiter='\t')
    if 'year' in df.columns:  # Check if 'year' column exists
        year_groups = df.groupby('year')
        avg_life_expectancy = year_groups['life_expectancy'].mean()
        print("Average life expectancy for each year (subsetting):")
        print(avg_life_expectancy)
    else:
        print("The 'year' column does not exist in the file.")
except pd.errors.EmptyDataError:
    print("The file is empty or has no valid data.")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# 17. Create a Series with index for 'banana' and '42'
series = pd.Series(['banana', 42], index=['Person', 'Who'])
print("Series with index 'Person' and 'Who':")
print(series)

# 18. Series with index for 'Wes McKinney' and 'Creator of Pandas'
series = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Title'])
print("Series with index 'Person' and 'Title':")
print(series)

# 19. Create a dictionary for pandas and convert to DataFrame
data = {'Occupation': ['Chemist', 'Statistician'],
        'Born': ['1920-07-25', '1876-06-13'],
        'Died': ['1958-04-16', '1937-10-16'],
        'Age': [37, 61]}
df = pd.DataFrame(data, index=['Franklin', 'Gosset'])
print("DataFrame created from dictionary:")
print(df)
