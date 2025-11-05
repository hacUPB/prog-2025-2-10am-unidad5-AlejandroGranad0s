lista = ["Little Dark Age","High Hopes","Reflektor","Take a slice","Black sheep","We Are The People","Engel","wiped out","Me and the devil","i walk this earth all by myself","Crumb Locket","Put Your Money On Me"]
ubicacion = "C:\\Users\\B09S202est\\Desktop\\mist\\"
modo = "a"
nombre_archivo = "canciones.txt"
fp = open(ubicacion+nombre_archivo, modo, encoding="utf-8")
for canciones in lista:
    fp.write(canciones+"\n")
fp.close()
