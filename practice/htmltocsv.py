import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the URL
url = 'https://en.wikipedia.org/wiki/Toyota?useskin=vector'
response = requests.get(url)

# Create a BeautifulSoup object with the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table with class "wikitable"
table = soup.find('table', class_='wikitable')

# Extract table headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract table rows
rows = []
for row in table.find_all('tr'):
    rows.append([data.text.strip() for data in row.find_all('td')])

# Write data to a CSV file
with open('out/toyota_table.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(headers)
    writer.writerows(rows)

print("Table extracted and saved as 'toyota_table.csv'.")
