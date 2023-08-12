import csv
import os

def open_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)

# Specify the folder path and file name
folder_path = r'C:\Users\91970\Downloads\Updated Attendence\Online-Face-Attendance--master\Online-Face-Attendance--master\\'
file_name = 'final.csv'

# Construct the full file path
file_path = os.path.join(folder_path, file_name)

# Call the function to open and read the CSV file
#open_csv_file(file_path)

# Open the CSV file using the default program
os.startfile(file_path)
