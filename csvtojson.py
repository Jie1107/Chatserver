import csv
import json

def csv_to_json(csv_file_name, json_file_name):
    data = []
    
    with open(csv_file_name, encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
            data.append(row)
    
    with open(json_file_name, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

csv_to_json('eiv030.csv', 'eiv030.json')