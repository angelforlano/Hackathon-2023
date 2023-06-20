import pandas
import json

def convert_str_num(_srt):
    return _srt

file = "data/2019_censcomercialbcn_detall.csv"

df = pandas.read_csv(file)

new_df = df[['Codi_Principal_Activitat', 'Nom_Principal_Activitat', 'Codi_Sector_Activitat', 'Nom_Sector_Activitat', 'Codi_Grup_Activitat', 'Nom_Grup_Activitat', 'Nom_Local', 'SN_Oci_Nocturn', 'SN_Obert24h', 'SN_Carrer', 'Nom_Mercat', 'Nom_Galeria', 'Nom_CComercial', 'Direccio_Unica', 'Codi_Via', 'Nom_Via', 'Codi_Barri', 'Nom_Barri', 'Codi_Districte', 'Nom_Districte']]
