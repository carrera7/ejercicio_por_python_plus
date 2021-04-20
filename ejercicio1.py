import csv
archivo = open("appstore_games.csv","r")
csvreader = csv.reader(archivo, delimiter=',')
juegos_gratuitos_EN = filter(lambda x: x[7]== "0" and x[12] == "ES" , csvreader)
for linea in juegos_gratuitos_EN:
    print(linea)
 
archivo.close()
