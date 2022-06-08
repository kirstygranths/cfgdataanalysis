import csv

def read_data():
    data = []

    with open('sales.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet:
            sls_value = row['sales']
            data.append(sls_value)

    return data


read_data()
print(read_data())
