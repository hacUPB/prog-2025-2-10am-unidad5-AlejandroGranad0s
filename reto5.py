import os
import matplotlib.pyplot as plt
import numpy as np
import csv
lista = ["txt1","txt2","txt3","txt4"]
lis = ["Aviación_Comercial_2020","AEROLINEA_SATENA","Entrada_AIM_2020","Salidas_AIM_2020"]
control = True
while control == True:
    print("Menu principal")
    print(" 1. Lista de archivos \n 2. Procesar archivo de texto (txt) \n 3. Procesar archivo separado por comas (csv) \n 4. Salir\n")
    opcion = input("Elija una opcion ")
    match opcion:
        case "1":
            print("Lista de archivostxt")
            print(lista)
            print("Lista de archivoscsv")
            print(lis)
        case "2":
            contr = True
            while contr == True:
                print("archivo de texto (txt)")
                print(" 1. txt1 \n 2. txt2 \n 3. txt3 \n 4. txt4 \n 0. salir \n")
                opcio = input("Elija una opcion ")
                match opcio:
                    case "1":
                        con1 = True
                        while con1 == True:
                            print("txt1")
                            print(" 1. procesar \n 2. contar \n 3. reemplazar \n 4. histograma \n 0. salir \n")
                            op1 = input("Elija una opcion ")
                            match op1:
                                case "1":
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "hola1.txt"
                                    modo = "r"
                                    fp = open(ubicacion+nombre, modo, encoding="utf-8")
                                    datos = fp.read()
                                    print(datos)
                                    fp.close()
                                case "2":
                                    print("contar")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "hola1.txt"
                                    modo = "r"
                                    fp = open(ubicacion+nombre, modo, encoding="utf-8")
                                    contenido = fp.read()
                                    cantidad = len(contenido)
                                    print(f"el archivo tiene {cantidad} caracteres.")
                                    fp.close()
                                case "3":
                                    print("reemplazar") #editar el resto
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "hola1.txt"
                                    modo = "r"
                                    palabra_vieja = input("Palabra a reemplazar: ")
                                    palabra_nueva = input("Nueva palabra: ")
                                    with open(ubicacion+nombre, modo, encoding="utf-8") as f:
                                        texto = f.read()
                                    texto = texto.replace(palabra_vieja, palabra_nueva)
                                    with open(ubicacion+nombre, "w", encoding="utf-8") as f:
                                        f.write(texto)
                                    print("Reemplazo completado.")
                                case "4":
                                    print("histograma")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "hola1.txt"
                                    modo = "r"
                                    fp = open(ubicacion+nombre, modo, encoding="utf-8")
                                    datos = fp.read()
                                    datos = datos.lower()
                                    vocales=["a","e","i","o","u"]
                                    conteo = []
                                    for v in vocales:
                                        cantidad=datos.count(v)
                                        conteo.append(cantidad)
                                    plt.bar(vocales, conteo, edgecolor='black')
                                    plt.title('Histograma')
                                    plt.show()
                                case "0":
                                    print("Regresando")
                                    break
                                case _:
                                    print("modo no valido")
                    case "2":
                        con2 = True
                        while con2 == True:
                            print("txt2")
                            print(" 1. procesar \n 2. contar \n 3. reemplazar \n 4. histograma \n 0. salir \n")
                            op2 = input("Elija una opcion ")
                            match op2:
                                case "1":
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "hola2.txt"
                                    modo = "r"
                                    fp = open(ubicacion+nombre, modo, encoding="utf-8")
                                    datos = fp.read()
                                    print(datos)
                                    fp.close()
                                case "2":
                                    print("contar")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "hola2.txt"
                                    modo = "r"
                                    fp = open(ubicacion+nombre, modo, encoding="utf-8")
                                    contenido = fp.read()
                                    cantidad = len(contenido)
                                    print(f"el archivo tiene {cantidad} caracteres.")
                                    fp.close()
                                case "3":
                                    print("Reemplazar")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "hola2.txt"
                                    modo = "r"
                                    palabra_vieja = input("Palabra a reemplazar: ")
                                    palabra_nueva = input("Nueva palabra: ")
                                    with open(ubicacion+nombre, modo, encoding="utf-8") as f:
                                        texto = f.read()
                                    texto = texto.replace(palabra_vieja, palabra_nueva)
                                    with open(ubicacion+nombre, "w", encoding="utf-8") as f:
                                        f.write(texto)
                                    print("Reemplazo completado.")
                                case "4":
                                    print("histograma")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "hola2.txt"
                                    modo = "r"
                                    fp = open(ubicacion+nombre, modo, encoding="utf-8")
                                    datos = fp.read()
                                    datos = datos.lower()
                                    vocales=["a","e","i","o","u"]
                                    conteo = []
                                    for v in vocales:
                                        cantidad=datos.count(v)
                                        conteo.append(cantidad)
                                    plt.bar(vocales, conteo, edgecolor='black')
                                    plt.title('Histograma')
                                    plt.show()
                                case "0":
                                    print("Regresando")
                                    break
                                case _:
                                    print("modo no valido")
                    case "3":
                        con3 = True
                        while con3 == True:
                            print("txt3")
                            print(" 1. procesar \n 2. contar \n 3. reemplazar \n 4. histograma \n 0. salir \n")
                            op2 = input("Elija una opcion ")
                            match op2:
                                case "1":
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "txt3.txt"
                                    modo = "r"
                                    fp = open(ubicacion+nombre, modo, encoding="utf-8")
                                    datos = fp.read()
                                    print(datos)
                                    fp.close()
                                case "2":
                                    print("contar")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "txt3.txt"
                                    modo = "r"
                                    fp = open(ubicacion+nombre, modo, encoding="utf-8")
                                    contenido = fp.read()
                                    cantidad = len(contenido)
                                    print(f"el archivo tiene {cantidad} caracteres.")
                                    fp.close()
                                case "3":
                                    print("Reemplazar")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "txt3.txt"
                                    modo = "r"
                                    palabra_vieja = input("Palabra a reemplazar: ")
                                    palabra_nueva = input("Nueva palabra: ")
                                    with open(ubicacion+nombre, modo, encoding="utf-8") as f:
                                        texto = f.read()
                                    texto = texto.replace(palabra_vieja, palabra_nueva)
                                    with open(ubicacion+nombre, "w", encoding="utf-8") as f:
                                        f.write(texto)
                                    print("Reemplazo completado.")
                                case "4":
                                    print("historiograma")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "txt3.txt"
                                    modo = "r"
                                    fp = open(ubicacion+nombre, modo, encoding="utf-8")
                                    datos = fp.read()
                                    datos = datos.lower()
                                    vocales=["a","e","i","o","u"]
                                    conteo = []
                                    for v in vocales:
                                        cantidad=datos.count(v)
                                        conteo.append(cantidad)
                                    plt.bar(vocales, conteo, edgecolor='black')
                                    plt.title('Histograma')
                                    plt.show()
                                case "0":
                                    print("Regresando")
                                    break
                                case _:
                                    print("modo no valido")
                    case "4":
                        con4 = True
                        while con4 == True:
                            print("txt4")
                            print(" 1. procesar \n 2. contar \n 3. reemplazar \n 4. histograma \n 0. salir \n")
                            op2 = input("Elija una opcion ")
                            match op2:
                                case "1":
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "txt4.txt"
                                    modo = "r"
                                    fp = open(ubicacion+nombre, modo, encoding="utf-8")
                                    datos = fp.read()
                                    print(datos)
                                    fp.close()
                                case "2":
                                    print("contar")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "txt4.txt"
                                    modo = "r"
                                    fp = open(ubicacion+nombre, modo, encoding="utf-8")
                                    contenido = fp.read()
                                    cantidad = len(contenido)
                                    print(f"el archivo tiene {cantidad} caracteres.")
                                    fp.close()
                                case "3":
                                    print("Reemplazar")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "txt4.txt"
                                    modo = "r"
                                    palabra_vieja = input("Palabra a reemplazar: ")
                                    palabra_nueva = input("Nueva palabra: ")
                                    with open(ubicacion+nombre, modo, encoding="utf-8") as f:
                                        texto = f.read()
                                    texto = texto.replace(palabra_vieja, palabra_nueva)
                                    with open(ubicacion+nombre, "w", encoding="utf-8") as f:
                                        f.write(texto)
                                    print("Reemplazo completado.")
                                case "4":
                                    print("histograma")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivostxt\\"
                                    nombre = "txt4.txt"
                                    modo = "r"
                                    fp = open(ubicacion+nombre, modo, encoding="utf-8")
                                    datos = fp.read()
                                    datos = datos.lower()
                                    vocales=["a","e","i","o","u"]
                                    conteo = []
                                    for v in vocales:
                                        cantidad=datos.count(v)
                                        conteo.append(cantidad)
                                    plt.bar(vocales, conteo, edgecolor='black')
                                    plt.title('Histograma')
                                    plt.show()
                                case "0":
                                    print("Regresando")
                                    break
                                case _:
                                    print("modo no valido")
                    case "0":
                        print("regresando")
                        break
                    case _:
                        print("modo no valido")
        case "3":
            contr = True
            while contr == True:
                print("archivo separado por comas (csv)")
                print(" 1. Aviación_Comercial_2020 \n 2. AEROLINEA_SATENA \n 3. Entrada_AIM_2020 \n 4. Salidas_AIM_2020 \n 0. salir \n")
                opcio = input("Elija una opcion ")
                match opcio:
                    case "1":
                        con1 = True
                        while con1 == True:
                            print("Aviación_Comercial_2020")
                            print(" 1. procesar \n 2. filas \n 3. estadisticas \n 4. graficas \n 0. salir \n")
                            op1 = input("Elija una opcion ")
                            match op1:
                                case "1":
                                    print("archivo separado por comas (csv)")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "Aviación_Comercial_2020.csv"
                                    modo = "r"
                                    with open(ubicacion+nombre, modo) as csvfile:
                                        lector = csv.reader(csvfile, delimiter=";")
                                        for fila in lector:
                                            print(fila)
                                case "2":
                                    print("filas")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "Aviación_Comercial_2020.csv"
                                    modo = "r"
                                    with open(ubicacion+nombre, modo) as csvfile:
                                        lector = csv.reader(csvfile, delimiter=";")
                                        for i, fila in enumerate(lector):
                                            if i >= 15:
                                                break
                                            print(fila)
                                case "3": # todos los caso 3 "estadisticas" fuero ayudadas con ia
                                    print("estadisticas")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "Aviación_Comercial_2020.csv"
                                    modo = "r"
                                    columna = int(input("Número de columna (empezando en 0): "))
                                    datos = []
                                    with open(ubicacion+nombre, modo, encoding="utf-8") as f:
                                        lector = csv.reader(f)
                                        contador = 0
                                        for fila in lector:
                                            if contador != 0:  # para saltar el encabezado sin usar next()
                                                if fila[columna] != "":
                                                    valor = float(fila[columna].replace(",","."))
                                                    datos.append(valor)
                                            contador += 1

                                        if len(datos) == 0:
                                            print("No hay datos numéricos en esa columna.")
                                            break

                                        # Calcular cantidad
                                        cantidad = len(datos)

                                        # Calcular promedio
                                        suma = 0
                                        for x in datos:
                                            suma = suma + x
                                        promedio = suma / cantidad

                                        # Ordenar manualmente (burbuja simple)
                                        for i in range(cantidad - 1):
                                            for j in range(cantidad - 1 - i):
                                                if datos[j] > datos[j + 1]:
                                                    temp = datos[j]
                                                    datos[j] = datos[j + 1]
                                                    datos[j + 1] = temp

                                        # Calcular mediana
                                        if cantidad % 2 == 0:
                                            mediana = (datos[cantidad//2 - 1] + datos[cantidad//2]) / 2
                                        else:
                                            mediana = datos[cantidad//2]

                                        # Calcular desviación estándar
                                        suma_desv = 0
                                        for x in datos:
                                            suma_desv = suma_desv + (x - promedio)**2
                                        desv = (suma_desv / cantidad)**0.5

                                        # Calcular máximo y mínimo
                                        maximo = datos[-1]
                                        minimo = datos[0]

                                        print("Cantidad:", cantidad)
                                        print("Promedio:", promedio)
                                        print("Mediana:", mediana)
                                        print("Desviación estándar:", desv)
                                        print("Máximo:", maximo)
                                        print("Mínimo:", minimo)
                                case "4":
                                    print("graficas")
                                    colu = int(input("numero de columnas: "))
                                    datos = []
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "Aviación_Comercial_2020.csv"
                                    modo = "r"
                                    with open(ubicacion+nombre, modo) as csvfile:
                                        lector = csv.reader(csvfile, delimiter=";")
                                        for fila in lector[1:]:
                                            datos.append(float(fila[colu]))
                                        if len(datos) > 0:
                                            plt.scatter(range(len(datos)), datos, color="blue")
                                            plt.title("grafico de dispersion")
                                            plt.xlabel("indice")
                                            plt.ylabel("valor")
                                            plt.show()

                                            plt.bar(range(len(sorted(datos))), sorted(datos), color="orange")
                                            plt.title("grafico de barras")
                                            plt.xlabel("indice")
                                            plt.ylabel("valor")
                                            plt.show()
                                        else:
                                            print("no se puede")
                                case "0":
                                    print("Regresando")
                                    break
                                case _:
                                    print("modo no valido")
                    case "2":
                        con2 = True
                        while con2 == True:
                            print("AEROLINEA_SATENA")
                            print(" 1. procesar \n 2. filas \n 3. estadisticas \n 4. graficas \n 0. salir \n")
                            op2 = input("Elija una opcion ")
                            match op2:
                                case "1":
                                    print("archivo separado por comas (csv)")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "AEROLINEA_SATENA.csv"
                                    modo = "r"
                                    with open(ubicacion+nombre, modo) as csvfile:
                                        lector = csv.reader(csvfile, delimiter=";")
                                        for fila in lector:
                                            print(fila)
                                case "2":
                                    print("filas")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "AEROLINEA_SATENA.csv"
                                    modo = "r"
                                    with open(ubicacion+nombre, modo) as csvfile:
                                        lector = csv.reader(csvfile, delimiter=";")
                                        for i, fila in enumerate(lector):
                                            if i >= 15:
                                                break
                                            print(fila)
                                case "3":
                                    print("estadisticas")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "AEROLINEA_SATENA.csv"
                                    modo = "r"
                                    columna = int(input("Número de columna (empezando en 0): "))
                                    datos = []
                                    with open(ubicacion+nombre, modo, encoding="utf-8") as f:
                                        lector = csv.reader(f)
                                        contador = 0
                                        for fila in lector:
                                            if contador != 0:  # para saltar el encabezado sin usar next()
                                                if fila[columna] != "":
                                                    valor = float(fila[columna].replace(",","."))
                                                    datos.append(valor)
                                            contador += 1

                                        if len(datos) == 0:
                                            print("No hay datos numéricos en esa columna.")
                                            break

                                        # Calcular cantidad
                                        cantidad = len(datos)

                                        # Calcular promedio
                                        suma = 0
                                        for x in datos:
                                            suma = suma + x
                                        promedio = suma / cantidad

                                        # Ordenar manualmente (burbuja simple)
                                        for i in range(cantidad - 1):
                                            for j in range(cantidad - 1 - i):
                                                if datos[j] > datos[j + 1]:
                                                    temp = datos[j]
                                                    datos[j] = datos[j + 1]
                                                    datos[j + 1] = temp

                                        # Calcular mediana
                                        if cantidad % 2 == 0:
                                            mediana = (datos[cantidad//2 - 1] + datos[cantidad//2]) / 2
                                        else:
                                            mediana = datos[cantidad//2]

                                        # Calcular desviación estándar
                                        suma_desv = 0
                                        for x in datos:
                                            suma_desv = suma_desv + (x - promedio)**2
                                        desv = (suma_desv / cantidad)**0.5

                                        # Calcular máximo y mínimo
                                        maximo = datos[-1]
                                        minimo = datos[0]

                                        print("Cantidad:", cantidad)
                                        print("Promedio:", promedio)
                                        print("Mediana:", mediana)
                                        print("Desviación estándar:", desv)
                                        print("Máximo:", maximo)
                                        print("Mínimo:", minimo)
                                case "4":
                                    print("graficas")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "AEROLINEA_SATENA.csv"
                                    modo = "r"
                                    columna = int(input("Número de columna (empezando en 0): "))
                                    datos = []
                                    with open(ubicacion+nombre, newline='', encoding="utf-8") as f:
                                        lector = csv.reader(f)
                                        next(lector)
                                        for fila in lector:
                                            try:
                                                valor = float(fila[columna])
                                                datos.append(valor)
                                            except:
                                                pass
                                    if len(datos) == 0:
                                        print("No hay datos numéricos en esa columna.")
                                        break
                                    plt.scatter(range(len(datos)), datos, color="red")
                                    plt.title("Gráfica de dispersión")
                                    plt.xlabel("Índice")
                                    plt.ylabel("Valor")
                                    plt.show()

                                    plt.bar(range(len(datos[:10])), datos[:10], color="green")
                                    plt.title("Gráfico de barras (primeros 10)")
                                    plt.xlabel("Índice")
                                    plt.ylabel("Valor")
                                    plt.show()
                    case "3":
                        con3 = True
                        while con3 == True:
                            print("Entrada_AIM_2020")
                            print(" 1. procesar \n 2. filas \n 3. estadisticas \n 4. graficas \n 0. salir \n")
                            op2 = input("Elija una opcion ")
                            match op2:
                                case "1":
                                    print("archivo separado por comas (csv)")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "Entrada_AIM_2020.csv"
                                    modo = "r"
                                    with open(ubicacion+nombre, modo) as csvfile:
                                        lector = csv.reader(csvfile, delimiter=";")
                                        for fila in lector:
                                            print(fila)
                                            
                                case "2":
                                    print("filas")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "Entrada_AIM_2020.csv"
                                    modo = "r"
                                    with open(ubicacion+nombre, modo) as csvfile:
                                        lector = csv.reader(csvfile, delimiter=";")
                                        for i, fila in enumerate(lector):
                                            if i >= 15:
                                                break
                                            print(fila)
                                case "3":
                                    print("estadisticas")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "Entrada_AIM_2020.csv"
                                    modo = "r"
                                    columna = int(input("Número de columna (empezando en 0): "))
                                    datos = []
                                    with open(ubicacion+nombre, modo, encoding="utf-8") as f:
                                        lector = csv.reader(f)
                                        contador = 0
                                        for fila in lector:
                                            if contador != 0:  # para saltar el encabezado sin usar next()
                                                if fila[columna] != "":
                                                    valor = float(fila[columna].replace(",","."))
                                                    datos.append(valor)
                                            contador += 1

                                        if len(datos) == 0:
                                            print("No hay datos numéricos en esa columna.")
                                            break

                                        # Calcular cantidad
                                        cantidad = len(datos)

                                        # Calcular promedio
                                        suma = 0
                                        for x in datos:
                                            suma = suma + x
                                        promedio = suma / cantidad

                                        # Ordenar manualmente (burbuja simple)
                                        for i in range(cantidad - 1):
                                            for j in range(cantidad - 1 - i):
                                                if datos[j] > datos[j + 1]:
                                                    temp = datos[j]
                                                    datos[j] = datos[j + 1]
                                                    datos[j + 1] = temp

                                        # Calcular mediana
                                        if cantidad % 2 == 0:
                                            mediana = (datos[cantidad//2 - 1] + datos[cantidad//2]) / 2
                                        else:
                                            mediana = datos[cantidad//2]

                                        # Calcular desviación estándar
                                        suma_desv = 0
                                        for x in datos:
                                            suma_desv = suma_desv + (x - promedio)**2
                                        desv = (suma_desv / cantidad)**0.5

                                        # Calcular máximo y mínimo
                                        maximo = datos[-1]
                                        minimo = datos[0]

                                        print("Cantidad:", cantidad)
                                        print("Promedio:", promedio)
                                        print("Mediana:", mediana)
                                        print("Desviación estándar:", desv)
                                        print("Máximo:", maximo)
                                        print("Mínimo:", minimo)
                                case "4":
                                    print("graficas")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "Entrada_AIM_2020.csv"
                                    modo = "r"
                                    columna = int(input("Número de columna (empezando en 0): "))
                                    datos = []
                                    with open(ubicacion+nombre, newline='', encoding="utf-8") as f:
                                        lector = csv.reader(f)
                                        next(lector)
                                        for fila in lector:
                                            try:
                                                valor = float(fila[columna])
                                                datos.append(valor)
                                            except:
                                                pass
                                    if len(datos) == 0:
                                        print("No hay datos numéricos en esa columna.")
                                        break
                                    plt.scatter(range(len(datos)), datos, color="red")
                                    plt.title("Gráfica de dispersión")
                                    plt.xlabel("Índice")
                                    plt.ylabel("Valor")
                                    plt.show()

                                    plt.bar(range(len(datos[:10])), datos[:10], color="green")
                                    plt.title("Gráfico de barras (primeros 10)")
                                    plt.xlabel("Índice")
                                    plt.ylabel("Valor")
                                    plt.show()
                                case "0":
                                    print("Regresando")
                                    break
                                case _:
                                    print("modo no valido")
                    case "4":
                        con4 = True
                        while con4 == True:
                            print("Salidas_AIM_2020")
                            print(" 1. procesar \n 2. filas \n 3. estadisticas \n 4. graficas \n 0. salir \n")
                            op2 = input("Elija una opcion ")
                            match op2:
                                case "1":
                                    print("archivo separado por comas (csv)")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "Salidas_AIM_2020.csv"
                                    modo = "r"
                                    with open(ubicacion+nombre, modo) as csvfile:
                                        lector = csv.reader(csvfile, delimiter=";")
                                        for fila in lector:
                                            print(fila)
                                case "2":
                                    print("filas")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "Salidas_AIM_2020.csv"
                                    modo = "r"
                                    with open(ubicacion+nombre, modo) as csvfile:
                                        lector = csv.reader(csvfile, delimiter=";")
                                        for i, fila in enumerate(lector):
                                            if i >= 15:
                                                break
                                            print(fila)
                                case "3":
                                    print("estadisticas")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "Salidas_AIM_2020.csv"
                                    modo = "r"
                                    columna = int(input("Número de columna (empezando en 0): "))
                                    datos = []
                                    with open(ubicacion+nombre, modo, encoding="utf-8") as f:
                                        lector = csv.reader(f)
                                        contador = 0
                                        for fila in lector:
                                            if contador != 0:  # para saltar el encabezado sin usar next()
                                                if fila[columna] != "":
                                                    valor = float(fila[columna].replace(",","."))
                                                    datos.append(valor)
                                            contador += 1

                                        if len(datos) == 0:
                                            print("No hay datos numéricos en esa columna.")
                                            break

                                        # Calcular cantidad
                                        cantidad = len(datos)

                                        # Calcular promedio
                                        suma = 0
                                        for x in datos:
                                            suma = suma + x
                                        promedio = suma / cantidad

                                        # Ordenar manualmente (burbuja simple)
                                        for i in range(cantidad - 1):
                                            for j in range(cantidad - 1 - i):
                                                if datos[j] > datos[j + 1]:
                                                    temp = datos[j]
                                                    datos[j] = datos[j + 1]
                                                    datos[j + 1] = temp

                                        # Calcular mediana
                                        if cantidad % 2 == 0:
                                            mediana = (datos[cantidad//2 - 1] + datos[cantidad//2]) / 2
                                        else:
                                            mediana = datos[cantidad//2]

                                        # Calcular desviación estándar
                                        suma_desv = 0
                                        for x in datos:
                                            suma_desv = suma_desv + (x - promedio)**2
                                        desv = (suma_desv / cantidad)**0.5

                                        # Calcular máximo y mínimo
                                        maximo = datos[-1]
                                        minimo = datos[0]

                                        print("Cantidad:", cantidad)
                                        print("Promedio:", promedio)
                                        print("Mediana:", mediana)
                                        print("Desviación estándar:", desv)
                                        print("Máximo:", maximo)
                                        print("Mínimo:", minimo)
                                case "4":
                                    print("graficas")
                                    ubicacion = "C:\\Users\\ANDRES GRANADOS\\Documents\\Mist2025\\5\\archivoscsv\\"
                                    nombre = "Salidad_AIM_2020.csv"
                                    modo = "r"
                                    columna = int(input("Número de columna (empezando en 0): "))
                                    datos = []
                                    with open(ubicacion+nombre, newline='', encoding="utf-8") as f:
                                        lector = csv.reader(f)
                                        next(lector)
                                        for fila in lector:
                                            try:
                                                valor = float(fila[columna])
                                                datos.append(valor)
                                            except:
                                                pass
                                    if len(datos) == 0:
                                        print("No hay datos numéricos en esa columna.")
                                        break
                                    plt.scatter(range(len(datos)), datos, color="red")
                                    plt.title("Gráfica de dispersión")
                                    plt.xlabel("Índice")
                                    plt.ylabel("Valor")
                                    plt.show()

                                    plt.bar(range(len(datos[:10])), datos[:10], color="green")
                                    plt.title("Gráfico de barras (primeros 10)")
                                    plt.xlabel("Índice")
                                    plt.ylabel("Valor")
                                    plt.show()
                                case "0":
                                    print("Regresando")
                                    break
                                case _:
                                    print("modo no valido")
        case "4":
            break
        case _:
            print("modo no valido")
