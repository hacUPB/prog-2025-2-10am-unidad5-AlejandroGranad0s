ubicacion = "C:\\Users\\B09S202est\\Desktop\\mist\\"
nombre_archivo = "frut.txt"
modo = "x"
fp = open(ubicacion+nombre_archivo, modo, encoding="utf-8")

frase = input("por favor ingresa una fruta: ")

cantidad_frutas = int(input("ingrese la cantidad de frutas: "))


porcentaje_ventas = float(input("ingrese el peso de la fruta: "))

fp.write(frase)
fp.write("\n")
fp.write(str(cantidad_frutas))
fp.write("\n")
fp.write(str(porcentaje_ventas))
fp.write("\n")
fp.close()
