import os
import csv

# Path to the folder containing the CSV files
folder_path = r"C:\Users\91970\Downloads\Updated Attendence\Online-Face-Attendance--master\Online-Face-Attendance--master"

# Initialize dictionaries to store the attendance counts for each person
attendance_counts = {}
out_counts = {}

# Get a list of all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Process each CSV file
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)

    with open(file_path, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row

        # Process the attendance and out entries in the current CSV file
        for row in reader:
            name = row[0]
            date = row[1]

            # Skip entries without a valid date
            if not date:
                continue

            if csv_file.startswith("attend"):
                # Increment attendance count
                if (name, date) in attendance_counts:
                    attendance_counts[(name, date)] += 1
                else:
                    attendance_counts[(name, date)] = 1
            elif csv_file.startswith("out"):
                # Increment out count
                if (name, date) in out_counts:
                    out_counts[(name, date)] += 1
                else:
                    out_counts[(name, date)] = 1

# Calculate the attendance percentage for each person present in both attend and out CSVs
attendance_percentages = {}

for key in attendance_counts.keys():
    if key in out_counts:
        count = attendance_counts[key]
        total_files = count + out_counts[key]
        percentage = (count / total_files) * 100
        attendance_percentages[key] = percentage

# Write the attendance percentages to the final CSV file
output_file = os.path.join(folder_path, "final.csv")

with open(output_file, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Date", "Percentage"])  # Write column headers

    for key, percentage in attendance_percentages.items():
        name, date = key
        writer.writerow([name, date, percentage])

print(f"Attendance percentages saved to {output_file}.")
