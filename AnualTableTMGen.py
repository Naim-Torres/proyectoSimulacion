import numpy as np
import statistics as sta


class AnualTableTMGen:

    def __init__(self, pm25mu, pm25sd, tmcp, iteration):
        self.__BETA = 0.2322
        self.__PM25CONFMIN = 5.8
        self.__PM25CONFMAX = 8.8
        self.__pm25mu = pm25mu
        self.__pm25sd = pm25sd
        self.__tmcp = tmcp
        #Tabla con todos lo valores de TMCP25 del año generados por Monte Carlo
        self.__AllAnualTm = []
        self.__iteration = iteration
        # Tabla de los valores promedio
        self.__anualAvgTm = 0
        #Tabla con todos los valores de AF del año generados por Monte Carlo
        self.__all_af = []
        self.__anualAvgAF = 0
        # Tabla con todos los valores de RR del año generados por Monte Carlo
        self.__all_rr = []
        self.__anualAvgRR = 0

    def getAnualAvgTm(self):
        self.__anualAvgTm = sta.mean(self.__AllAnualTm)
        return self.__anualAvgTm

    def getAnualAvgAF(self):
        self.__anualAvgAF = sta.mean(self.__all_af)
        return self.__anualAvgAF

    def getAnualAvgRR(self):
        self.__anualAvgRR = sta.mean(self.__all_rr)
        return self.__anualAvgRR

    def get_beta(self):
        return self.__BETA

    def calculteTMPM25(self):

        pm25distnorm = np.random.normal(self.__pm25mu, self.__pm25sd, size=self.__iteration)
        pm25confdistunif = np.random.uniform(self.__PM25CONFMIN, self.__PM25CONFMAX, self.__iteration)

        for i in range(self.__iteration):
            rr = ((pm25distnorm[i]+1)/(pm25confdistunif[i]+1))**self.__BETA
            af = (rr - 1)/rr
            tmpm25 = af * self.__tmcp
            self.__AllAnualTm.append(tmpm25)
            self.__all_af.append(af)
            self.__all_rr.append(rr)
