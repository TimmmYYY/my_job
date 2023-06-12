import openpyxl
import csv

# Load the XLSX file
workbook = openpyxl.load_workbook('data/xl.xlsx')

# Select the active worksheet
worksheet = workbook.active

# Create a CSV file
with open('out/xl.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Iterate through each row in the worksheet
    for row in worksheet.iter_rows():
        # Extract the values from each cell in the row
        values = [cell.value for cell in row]

        # Write the row of values to the CSV file
        writer.writerow(values)

print("XLSX file converted to CSV successfully.")
