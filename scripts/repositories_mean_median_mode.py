import csv

# Define the path to your CSV file
file_path = "repositories_info.csv"

# Initialize variables to store data
data = []
rq1 = []  # RQ1 - Repository age (days)
rq2 = []  # RQ2 - Total pull requests accepted
rq3 = []  # RQ3 - Total releases
rq4 = []  # RQ4 - Time since last update (days)
rq5 = []  # RQ5 - Primary language
rq6 = []  # RQ6 - Issues closed percentage

# Read the CSV data
with open(file_path, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)  # Skip the header row
    for row in reader:
        data.append(row)
        rq1.append(int(row[1]))
        rq2.append(int(row[2]))
        rq3.append(int(row[3]))
        # Handle cases where data is missing (represented by '-1')
        if row[4] == "-1":
            rq4.append(float("nan"))  # Use 'nan' for not a number
        else:
            rq4.append(int(row[4]))
        rq5.append(row[5])
        rq6.append(float(row[6]))

# Calculate mean, median, and mode for each data set
import statistics

def calculate_statistics(data_set):
    try:
        mean = statistics.mean(data_set)
        median = statistics.median(data_set)
        mode = statistics.mode(data_set)
        return f"Mean: {mean:.2f}, Median: {median}, Mode: {mode}"
    except statistics.StatisticsError:
        return "Insufficient data to calculate statistics."  # Handle cases with insufficient data

# Print the results
print("RQ1 - Repository Age (days):")
print(calculate_statistics(rq1))
print("RQ2 - Total Pull Requests Accepted:")
print(calculate_statistics(rq2))
print("RQ3 - Total Releases:")
print(calculate_statistics(rq3))
print("RQ4 - Time Since Last Update (days):")
print(calculate_statistics(rq4))
print("RQ5 - Primary Language:")
# Mode not applicable for categorical data like primary language
print(f"Most frequent language: {statistics.mode(rq5)}")
print("RQ6 - Issues Closed Percentage:")
print(calculate_statistics(rq6))


