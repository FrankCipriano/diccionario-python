

midiccionario = {"frank":"cipriano","chicua":"chichicastenango"}

#comprobamos de que la declaracion anterior es un diccionario
print(type(midiccionario))

#hacer una consulta en el diccionario mediante una clave
print(midiccionario["chicua"])

#cambiar el valor de una clave en el diccionario
midiccionario["chicua"]="quiche"
print(midiccionario)

#eliminar un elemento en el diccionario mediante la clave
del(midiccionario["chicua"])
print(midiccionario)

#embeber diccionarios en una lista
dicc1 = {"frank":"cipriano","chicua":"chichi"}
dicc2 = {"cristian":"xiloj","semeja":"chichi"}
lista = []
lista.append(dicc1)
lista.append(dicc2)
print(lista)