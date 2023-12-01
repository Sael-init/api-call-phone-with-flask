from difflib import SequenceMatcher
import csv


def leer_csv(nombre_archivo):
    usuarios = []
    with open(nombre_archivo, 'r', newline='') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            usuarios.append(dict(fila))
    return usuarios


def encontrar_propietario(numero_busqueda):
    archivo = 'data.csv'  # Reemplaza 'usuarios.csv' con el nombre de tu archivo CSV
    usuarios = leer_csv(archivo)
    # Algoritmo de comparación de secuencias para encontrar números similares
    for usuario in usuarios:
        print(usuario)
        if usuario["celular"] == numero_busqueda: 
            man = [usuario["celular"],usuario["name"],usuario["saldo"]]
            return man
        
    return "No se encontro usuario"
        
def obtener_transacciones(numero):
    transacciones_usuario = []
    with open('transiciones.csv', 'r', newline='') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            if fila['numero'] == numero:
                transacciones_usuario.append({
                    'numero': fila['numero'],
                    'monto': fila['monto'],
                    'destinatario': fila['destinatario']
                })
    return transacciones_usuario


def pagary(mynum, number, valor):
    # Crear un diccionario con los datos a escribir en la línea del CSV
    datos_transaccion = {'mynum': mynum, 'number': number, 'valor': valor}

    # Nombre del archivo CSV donde se escribirán los datos
    nombre_archivo = 'transiciones.csv'

    # Escribir los datos en una línea del archivo CSV
    with open(nombre_archivo, 'a', newline='') as archivo_csv:  # Usamos 'a' para agregar al archivo
        campos = ['mynum', 'number', 'valor']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)

        # Verificar si el archivo está vacío para escribir el encabezado
        archivo_csv.seek(0, 2)
        vacio = archivo_csv.tell() == 0
        if vacio:
            escritor_csv.writeheader()

        # Escribir los datos en una fila
        escritor_csv.writerow(datos_transaccion)
    return obtener_transacciones(mynum)

