import csv

with open("data/locveevolucio.csv", "r") as file:
        data = file.readlines()
        
        for line in data:
            line_data = line.split(",")
            print(line_data)

"""
with open('data/locveevolucio.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
    for row in spamreader:
        print(', '.join(row))"""