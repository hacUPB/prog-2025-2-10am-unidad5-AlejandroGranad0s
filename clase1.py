'''
fp = open("./Desktop/mist/UPB.txt","r")
datos = fp.read(34)
print(datos)
datos = fp.read(5)
print(datos)
datos = fp.read(25)
print(datos)
fp.close()
'''
'''
archivo = open("./Desktop/mist/texto.txt", "r")
#datos = archivo.read(1000)
#for i in range(5):
    #datos = archivo.read()
#for datos in archivo:
    #print(datos[0])
datos = archivo.readlines()
print(datos)
archivo.close()
'''
