"""
PROGRAMA PARA ORGANIZAR UNA FRASE POR UN ORDEN DADO EN LA MISMA ORACION

  1-Volver las lineas del archivo externo una lista
  2-Separar esa lista entre orden y palabras 
  3-Crear un diccionario vacío donde se harán referencia al orden que debe seguir la oración
  4-Guardar valores llave[orden] valor[palabra] dentro del diccionario(Organizar la lista de palabras con respecro a la lista de orden)
  5-Agregar en oracion la palbras ordenadas
"""
archivo= open("ejemplo1.txt","r")
lineas= archivo.readlines()#1

for linea in lineas: 
    linea = linea.replace("\n", "")
    linea = linea.split(';')#2


    palabras = linea[0].split(' ')#2
    orden = linea[1].split(' ')#2

    oracion= ''
    diccionario={}#3

    for indice in range(0,len(orden)):#4
        diccionario[int(orden[indice])] = palabras[indice]#4 
        pass

    for indice in range(1,len(diccionario)+1):
      if oracion == '':
        oracion = diccionario[indice]
      else:
        oracion = oracion + ' ' + diccionario[indice]

    print('Oracion organizada: ',oracion)


archivo.close()

#print(lineas[0]) acceder a las lineas 