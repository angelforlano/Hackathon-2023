from database import Database

_df_colls_names = ['ID_Bcn_2019', 'ID_Bcn_2016', 'Codi_Principal_Activitat', 'Nom_Principal_Activitat', 'Codi_Sector_Activitat', 'Nom_Sector_Activitat', 'Codi_Grup_Activitat', 'Nom_Grup_Activitat', 'Codi_Activitat_2019', 'Nom_Activitat', 'Codi_Activitat_2016', 'Nom_Local', 'SN_Oci_Nocturn', 'SN_Coworking', 'SN_Servei_Degustacio', 'SN_Obert24h', 'SN_Mixtura', 'SN_Carrer', 'SN_Mercat', 'Nom_Mercat', 'SN_Galeria', 'Nom_Galeria', 'SN_CComercial', 'Nom_CComercial', 'SN_Eix', 'Nom_Eix', 'X_UTM_ETRS89', 'Y_UTM_ETRS89', 'Latitud', 'Longitud', 'Direccio_Unica', 'Codi_Via', 'Nom_Via', 'Planta', 'Porta', 'Num_Policia_Inicial', 'Lletra_Inicial', 'Num_Policia_Final', 'Lletra_Final', 'Solar', 'Codi_Parcela', 'Codi_Illa', 'Seccio_Censal', 'Codi_Barri', 'Nom_Barri', 'Codi_Districte', 'Nom_Districte', 'Referencia_cadastral', 'Data_Revisio']

def convert_str_num(_srt):
    if _srt.replace(".", "", 1).isdigit():  # Verificar que solo contenga números y un solo punto decimal
        numero = float(_srt)
        #print("La cadena es un número de punto flotante:", numero)
        return numero
    else:
        #print("La cadena no contiene solo números o es un número de punto flotante inválido.")
        return _srt


if __name__ == "__main__":
    main_db = Database("main", cluster = "main", develop = False)
    
    i = 0
    
    with open("data/2019_censcomercialbcn_detall.csv", "r", encoding="utf-8") as file:
        file.readline()
        data = file.readlines()
        
        for line in data:
            line = line.replace('"', "")
            row_data = line.split(",")
            
            _row_obj = {}
        
            for coll_name in _df_colls_names:
                _row_obj[coll_name] = convert_str_num(row_data[_df_colls_names.index(coll_name)])
    
            main_db.insert(_row_obj, into="data")
            
            i += 1
        
            if (i == 5):
                pass
                #break
            
    