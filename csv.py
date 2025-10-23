import csv

with open("C:\\Users\\B09S202est\\Desktop\\mist\\variables.csv", "r") as csvfile:
    lector = csv.reader(csvfile, delimiter=";")
    encabezado = next(lector)
    presion = []
    temperatura = []
    humedad = []
    densidad = []
    print(encabezado)
    for fila in lector:
        datos = int(fila[0])
        dato = int(fila[1])
        dat = int(fila[2])
        fila[3] = fila[3].replace(",",".")
        datoss = float(fila[3])
        presion.append(datos)
        temperatura.append(dato)
        humedad.append(dat)
        densidad.append(datoss)
print(presion)
print(temperatura)
print(humedad)
print(densidad)
