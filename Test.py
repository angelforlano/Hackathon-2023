import pandas

file = "data/2019_censcomercialbcn_detall.csv"

df = pandas.read_csv(file)

print(df.head())
print(df.describe())

"""
with open("data/2019_censcomercialbcn_detall.csv", "r", encoding="utf-8") as file:
    data = file.readlines()
    
    for line in data:
        line_data = line.split(",")
        print(line_data)"""

"""
with open('data/locveevolucio.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
    for row in spamreader:
        print(', '.join(row))"""