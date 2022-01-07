import numpy as np
import statistics as sta
from AnualTableTMGen import AnualTableTMGen


class main_simulation:

    def __init__(self, no):
        self.dataMatrix = [[2004, 36, 6.8], [2005, 28, 7.1], [2006, 23, 7.2], [2007, 26, 6.6],
                      [2008, 26, 6.8], [2009, 26, 7.0], [2010, 25, 7.2], [2011, 25, 7.4],
                      [2012, 26, 6.7], [2013, 28, 7.3], [2014, 27, 7.2], [2015, 28, 7.0],
                      [2016, 25, 7.1], [2017, 29, 6.7], [2018, 28, 6.8], [2019, 28, 7.0],
                      [2020, 20, 6.0]]

        self.pm25concentration = []
        self.tm = []
        for n in self.dataMatrix:
            self.pm25concentration.append(n[1])
            self.tm.append(n[2])
        self.pm25mu = sta.mean(self.pm25concentration)
        self.pm25sd = np.std(self.pm25concentration)
        # Tabla el año y los promedios de todos los años y todas las interaciones
        self.simulIterationTable = []
        self.__no = no
        self.__cdf_data = []

    def begin_simulation(self):
        self.simulIterationTable = []
        self.__cdf_data = []
        # ciclo por cada anio
        for i in range(len(self.dataMatrix)):
            # Tabla con los valores de cada año para todas las iteraciones
            anualIteration = []
            for iteration in range(100):
                tablaanual = AnualTableTMGen(self.pm25mu, self.pm25sd, self.tm[i], self.__no)
                tablaanual.calculteTMPM25()
                anualIteration.append(tablaanual.getAnualAvgTm())
            self.simulIterationTable.append([self.dataMatrix[i][0], np.mean(anualIteration)])
            self.__cdf_data.extend(anualIteration)

    def return_dic(self):
        age_list = []
        value_list = []
        for n in self.simulIterationTable:
            age_list.append(n[0])
            value_list.append(n[1])

        dict_from_list = dict(zip(age_list, value_list))
        return dict_from_list

    def get_cdf_data(self):
        return self.__cdf_data

    def get_tm(self):
        return self.tm

    def set_no(self, no):
        self.__no = no
