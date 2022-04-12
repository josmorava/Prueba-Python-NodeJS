archivo = open("ejemplo2.txt","r")
lineas = archivo.readlines()

for linea in lineas:
    linea = linea.replace("\n","")
    separacion = linea.split(' | ')

    vinos=separacion[0].split(' ')
    letras=separacion[1]

    semejanzas=False
    
    for vino in vinos:
        #print(vino,letras)
        if letras in vino:
          print(letras,'está en :',vino)
        else:
          print(False)
    
  #Comparar si letras están dentro del nombre del vino
