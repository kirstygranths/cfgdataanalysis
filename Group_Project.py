import csv

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        sls_month = row['month']

print(sls_month)