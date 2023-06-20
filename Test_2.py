import pandas
import json

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

colls = ['Codi_Principal_Activitat', 'Nom_Principal_Activitat', 'Codi_Sector_Activitat', 'Nom_Sector_Activitat', 'Codi_Grup_Activitat', 'Nom_Grup_Activitat', 'Nom_Local', 'SN_Oci_Nocturn', 'SN_Obert24h', 'SN_Carrer', 'Nom_Mercat', 'Nom_Galeria', 'Nom_CComercial', 'Direccio_Unica', 'Codi_Via', 'Nom_Via', 'Codi_Barri', 'Nom_Barri', 'Codi_Districte', 'Nom_Districte']

_map = {

}

_rows = []

i = 0
#for item in list:
    #print(df["Codi_Principal_Activitat"].describe())
    #print(len(df["Codi_{}".format(item)].unique()))
    #print(len(df["Nom_{}".format(item)].unique()))

_df_colls_names = ['Codi_Principal_Activitat', 'Nom_Principal_Activitat', 'Codi_Sector_Activitat', 'Nom_Sector_Activitat', 'Codi_Grup_Activitat', 'Nom_Grup_Activitat', 'Nom_Local', 'SN_Oci_Nocturn', 'SN_Obert24h', 'SN_Carrer', 'Nom_Mercat', 'Nom_Galeria', 'Nom_CComercial', 'Direccio_Unica', 'Codi_Via', 'Nom_Via', 'Codi_Barri', 'Nom_Barri', 'Codi_Districte', 'Nom_Districte']

with open("data/2019_censcomercialbcn_detall.csv", "r", encoding="utf-8") as file:
    file.readline()
    data = file.readlines()
    
    for line in data:
        line = line.replace('"', "")
        row_data = line.split(",")
        
        #print(row_data)
        
        #print(_row_coi_index)
        #print(_row_nom_index)
        
        #print()
        #print(row_data[_row_nom_index])
        
        _row_obj = {}
        
        for coll_name in _df_colls_names:
            _row_obj[coll_name] = row_data[_df_colls_names.index(coll_name)]
        
        #print()
        _rows.append(_row_obj)
        
        #_codi_value = row_data[_row_coi_index]
        #_nom_value = row_data[_row_nom_index]

        """
        if (_nom_value == "Altres" or _nom_value == "Grup no definit"):
            _codi_value = "0"
        
        if not(_codi_value in _map):
            _map[_codi_value] = _nom_value
        """
        i += 1
        
        if (i == 25):
            pass
            #break

#print(json.dumps(_map))

_final_data = {
    "rows" : _rows
}

# Guardar el objeto JSON en un archivo
nombre_archivo = "data/datos.json"
with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    json.dump(_final_data, archivo, ensure_ascii=False)

"""
with open('data/locveevolucio.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
    for row in spamreader:
        print(', '.join(row))"""