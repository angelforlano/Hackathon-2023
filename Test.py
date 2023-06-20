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

colls = ["Sector_Activitat"]

_map = {

}

_rows = []

i = 0
#for item in list:
    #print(df["Codi_Principal_Activitat"].describe())
    #print(len(df["Codi_{}".format(item)].unique()))
    #print(len(df["Nom_{}".format(item)].unique()))

_df_colls_names = ['ID_Bcn_2019', 'ID_Bcn_2016', 'Codi_Principal_Activitat', 'Nom_Principal_Activitat', 'Codi_Sector_Activitat', 'Nom_Sector_Activitat', 'Codi_Grup_Activitat', 'Nom_Grup_Activitat', 'Codi_Activitat_2019', 'Nom_Activitat', 'Codi_Activitat_2016', 'Nom_Local', 'SN_Oci_Nocturn', 'SN_Coworking', 'SN_Servei_Degustacio', 'SN_Obert24h', 'SN_Mixtura', 'SN_Carrer', 'SN_Mercat', 'Nom_Mercat', 'SN_Galeria', 'Nom_Galeria', 'SN_CComercial', 'Nom_CComercial', 'SN_Eix', 'Nom_Eix', 'X_UTM_ETRS89', 'Y_UTM_ETRS89', 'Latitud', 'Longitud', 'Direccio_Unica', 'Codi_Via', 'Nom_Via', 'Planta', 'Porta', 'Num_Policia_Inicial', 'Lletra_Inicial', 'Num_Policia_Final', 'Lletra_Final', 'Solar', 'Codi_Parcela', 'Codi_Illa', 'Seccio_Censal', 'Codi_Barri', 'Nom_Barri', 'Codi_Districte', 'Nom_Districte', 'Referencia_cadastral', 'Data_Revisio']

with open("data/2019_censcomercialbcn_detall.csv", "r", encoding="utf-8") as file:
    file.readline()
    
    data = file.readlines()
    
    for cool in colls:
        
        _row_coi = "Codi_{}".format(cool)
        _row_nom = "Nom_{}".format(cool)
        
        _row_coi_index = _df_colls_names.index(_row_coi)
        _row_nom_index = _df_colls_names.index(_row_nom)
        
        for line in data:
            line = line.replace('"', "")
            row_data = line.split(",")
            
            #print(row_data)
            
            #print(_row_coi_index)
            #print(_row_nom_index)
            
            #print()
            #print(row_data[_row_nom_index])
            
            _codi_value = row_data[_row_coi_index]
            _nom_value = row_data[_row_nom_index]
            
            if not(_codi_value in _map):
                _map[_codi_value] = _nom_value
            
            i += 1
            
            if (i == 1):
                pass
                #break

print(json.dumps(_map))

_final_data = {
    "rows" : _rows
}

"""
with open('data/locveevolucio.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
    for row in spamreader:
        print(', '.join(row))"""