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
    
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        
        # Count the attendance for each person in the current CSV file
        for row in reader:
            name = row[0]
            if name in attendance_counts:
                attendance_counts[name] += 1
            else:
                attendance_counts[name] = 1

# Calculate the percentage of attendance for each person
total_files = len(csv_files)
attendance_percentages = {}

for name, count in attendance_counts.items():
    percentage = (count / total_files) * 100
    attendance_percentages[name] = percentage

# Write the attendance percentages to the final CSV file
output_file = os.path.join(folder_path, "final.csv")

with open(output_file, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Percentage"])  # Write column headers
    
    for name, percentage in attendance_percentages.items():
        writer.writerow([name, percentage])

print(f"Attendance percentages saved to {output_file}.")
