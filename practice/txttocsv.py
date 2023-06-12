import csv

# Read data from the text file
with open('data/txt_data.txt', 'r') as file:
    txt_data = file.read()

# Split the text into rows and columns
rows = txt_data.split('\n')
header = rows[0].split(' | ')
data = [row.split(' | ') for row in rows[2:]]

# Write the data to a CSV file
with open('out/txt.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(data)
