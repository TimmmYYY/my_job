import csv
import PyPDF2

def pdf_to_csv(pdf_path, csv_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        with open(csv_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for page in pdf_reader.pages:
                text = page.extract_text()
                lines = text.split('\n')
                for line in lines:
                    row = line.split()
                    csv_writer.writerow(row)

# Provide the paths for the input PDF and output CSV files
pdf_path = 'data/xl.pdf'
csv_path = 'out/output_pdf.csv'

# Convert PDF to CSV
pdf_to_csv(pdf_path, csv_path)
