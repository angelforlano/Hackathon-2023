import pandas

file = "data/2019_censcomercialbcn_detall.csv"

df = pandas.read_csv(file)

print(list(df.columns))
print(df.head())
print(df.describe())


def get_all_colls():
    for col in df.columns:
        if ("Codi_" in col):
            print(col)
            print(df[col].unique())

list = ["Grup_Activitat"]

_map = {

}

_rows = {

}

#for item in list:
    #print(df["Codi_Principal_Activitat"].describe())
    #print(len(df["Codi_{}".format(item)].unique()))
    #print(len(df["Nom_{}".format(item)].unique()))

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