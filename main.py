import numpy as np
import statistics as sta
from AnualTableTMGen import AnualTableTMGen


def main():
    dataMatrix = [[2004, 36, 6.8], [2005, 28, 7.1], [2006, 23, 7.2], [2007, 26, 6.6],
                     [2008, 26, 6.8], [2009, 26, 7.0], [2010, 25, 7.2], [2011, 25, 7.4],
                     [2012, 26, 6.7], [2013, 28, 7.3], [2014, 27, 7.2], [2015, 28, 7.0],
                     [2016, 25, 7.1], [2017, 29, 6.7], [2018, 28, 6.8], [2019, 28, 7.0],
                     [2020, 20, 6.0]]

    pm25concentration = []
    tm = []
    for n in dataMatrix:
        pm25concentration.append(n[1])
        tm.append(n[2])
    pm25mu = sta.mean(pm25concentration)
    pm25sd = np.std(pm25concentration)

    # Tabla el año y los promedios de todos los años y todas las interaciones
    simulIterationTable = []
    # ciclo por cada anio
    for i in range(len(dataMatrix)):
        # Tabla con los valores de cada año para todas las iteraciones
        anualIteration = []
        for iteration in range(10):
            tablaanual = AnualTableTMGen(pm25mu, pm25sd, tm[i], 200)
            tablaanual.calculteTMPM25()
            anualIteration.append(tablaanual.getAnualAvgTm())
            #print('Año:{}  Promedio = {}'.format(dataMatrix[i][0], tablaanual.getAnualAvgTm()))
        simulIterationTable.append([dataMatrix[i][0], np.mean(anualIteration)])
    print(simulIterationTable)


if __name__ == '__main__':
    main()
