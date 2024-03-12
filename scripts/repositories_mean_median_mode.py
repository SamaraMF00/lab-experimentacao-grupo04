import pandas as pd

def calculate_stats(data_file):
    """
    Reads data from a CSV file, calculates mean, median, and mode for numeric columns,
    and calculates mode (ignoring non-programming languages) for the primary language column.

    Args:
        data_file (str): Path to the CSV file containing the data.

    Returns:
        dict: A dictionary containing the calculated statistics.
    """

    df = pd.read_csv(data_file)

    # Separate numeric and non-numeric columns
    numeric_cols = df.select_dtypes(include=[int])
    non_numeric_cols = df.select_dtypes(exclude=[int])

    # Calculate mean and median for numeric columns
    numeric_stats = {col: df[col].mean() for col in numeric_cols}
    numeric_stats.update({col: df[col].median() for col in numeric_cols})

    # Calculate mode for primary language, ignoring non-programming languages
    language_mode = df[df['Primary language'].str.isalnum()]['Primary language'].mode().iloc[0]

    # Calculate mode for other columns (excluding primary language)
    other_modes = {col: df[col].mode().iloc[0] for col in non_numeric_cols if col != 'Primary language'}

    # Combine all statistics
    all_stats = {**numeric_stats, **other_modes, 'Primary language (Mode)': language_mode}

    return all_stats

# Example usage
data_file = "your_data.csv"  # Replace with the actual path to your CSV file
stats = calculate_stats(data_file)

# Print the calculated statistics
for stat_name, stat_value in stats.items():
    print(f"{stat_name}: {stat_value}")
