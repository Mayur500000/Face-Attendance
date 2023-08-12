import os
import csv

# Path to the folder containing the CSV files
folder_path = r"C:\Users\91970\Downloads\Updated Attendence\Online-Face-Attendance--master\Online-Face-Attendance--master"

# Initialize a dictionary to store the attendance counts for each person
attendance_counts = {}

# Get a list of all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Process each CSV file
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    
    # Read the current CSV file
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        records = list(reader)
    
    # Extract names from the records, skipping the first row (column names)
    names = [record[0] for record in records[1:]]
    
    # Update the attendance counts for each person
    for name in names:
        attendance_counts[name] = attendance_counts.get(name, 0) + 1

# Calculate the attendance percentage for each person
total_entries = len(csv_files)
attendance_percentages = {}

for name, count in attendance_counts.items():
    percentage = (count / total_entries) * 100
    attendance_percentages[name] = percentage

# Print the attendance percentage for each person in the desired format
for name, percentage in attendance_percentages.items():
    print(f"{name}: {percentage:.2f}%")
