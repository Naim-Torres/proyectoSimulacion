import numpy as np
import statistics as sta
from tkinter import *
from AnualTableTMGen import AnualTableTMGen


def main():
    # Creacion de la ventana de la GUI
    root = Tk()
    root.geometry("800x500")
    root.title("Simualción Mortalidad Cancer Pulmonar PM2.5")
    root.state("zoomed")
    root.minsize(width=800, height=600)
    root.update()

    frame = LabelFrame(root, text="Selección de datos", padx=5, pady=5)
    frame.grid(padx=5, pady=5, row=0, column=0)

    iterationLabel = Label(frame, text="Número de iteraciones")
    iterationLabel.grid(pady=0, padx=5, row=0, column=0, sticky="nw")
    iterationScale = Scale(frame, from_=2000, to=10000, orient="horizontal", tickinterval=2000,
                           length=root.winfo_width()/5, width=10, resolution=2000)
    iterationScale.grid(pady=0, padx=5, row=1, column=0)

    frame.update_idletasks()
    simulationchart = Canvas(root, width=(root.winfo_width()-(frame.winfo_width()+20)),
                             height=root.winfo_height()-(root.winfo_height()/3), bg="#596869")
    simulationchart.grid(pady=5, padx=5, row=0, column=1)

    startsimulationbutton = Button(root, text="Start", padx=5, pady=5, command=simulation)
    startsimulationbutton.grid(pady=0, padx=5, row=1, column=0, sticky="nsew")

    root.mainloop()


def simulation():
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
        simulIterationTable.append([dataMatrix[i][0], np.mean(anualIteration)])
    print(simulIterationTable)


if __name__ == '__main__':
    main()
