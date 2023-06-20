
def convert_str_num(_srt):
    if _srt.replace(".", "", 1).isdigit():  # Verificar que solo contenga números y un solo punto decimal
        numero = float(_srt)
        #print("La cadena es un número de punto flotante:", numero)
        return numero
    else:
        #print("La cadena no contiene solo números o es un número de punto flotante inválido.")
        return _srt
