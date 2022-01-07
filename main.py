import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
from main_simulation import main_simulation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = Tk()
root.geometry("800x500")
root.title("Simualción Mortalidad Cancer Pulmonar PM2.5")
root.state("zoomed")
root.minsize(width=950, height=600)
root.update()
sim = main_simulation(1)

def main():
    # Creacion de la ventana de la GUI
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 1, weight=1)

    # Frame de seleccion de datos
    frame = LabelFrame(root, text="Selección de datos", padx=5, pady=5)
    frame.grid(padx=10, pady=5, row=0, column=0, sticky="n")


    iterationLabel = Label(frame, text="Número de iteraciones")
    iterationLabel.grid(pady=0, padx=5, row=0, column=0, sticky="nw")
    iterationScale = Scale(frame, from_=2000, to=10000, orient="horizontal", tickinterval=2000,
                           length=root.winfo_width()/5, width=10, resolution=2000)
    iterationScale.grid(pady=0, padx=10, row=1, column=0)

    #Creacion del obhjeto que lleva la simulacion
    #sim.begin_simulation()

    def plot():
        sim.set_no(iterationScale.get())

        sim.begin_simulation()

        dic = sim.return_dic()
        age = list(dic.keys())
        value = list(dic.values())

        fig, ax = plt.subplots()
        ax.plot(age, sim.get_tm(), marker='o', label='Mortalidad general', color='tab:purple')
        ax.plot(age, value, marker='o', label='Mortalidad por PM2.5', color='tab:green')
        ax.set_title('Mortalidad por cancer pulmonar', loc="center",
                     fontdict={'fontsize': 14, 'fontweight': 'bold'})
        ax.set_xlabel("Año")
        ax.set_ylabel("Fracción de mortalidad")
        ax.set_yticks(range(1, 8))
        plt.grid(axis='y', color='gray', linestyle='dashed')
        plt.legend()

        canva = FigureCanvasTkAgg(fig, master=frame_canva)
        canva.draw()
        canva.get_tk_widget().grid(pady=10, padx=10, row=1, column=0, columnspan=3, sticky="nsew")

    #Boton que inicia la simulacion
    startsimulationbutton = Button(root, text="Start", padx=5, pady=5, command=plot)
    startsimulationbutton.grid(pady=2, padx=10, row=1, column=0, sticky="nsew")

    #Boton que termina la simulacion
    stopsimulationbutton = Button(root, text="Close", padx=5, pady=5, command=root.quit)
    stopsimulationbutton.grid(pady=2, padx=10, row=2, column=0, sticky="nsew")

    #Frame con las graficas
    frame_canva = LabelFrame(root, text="Graficos", padx=5, pady=5)
    frame_canva.grid(padx=10, pady=5, row=0, column=1, sticky="nsew", rowspan=3)
    Grid.rowconfigure(frame_canva, 1, weight=1)
    Grid.columnconfigure(frame_canva, 0, weight=1)

    def page1():
        try:
            frame_canva.grid_forget()
            frame_canva.grid(padx=10, pady=5, row=0, column=1, sticky="nsew", rowspan=3)
            Grid.rowconfigure(frame_canva, 1, weight=1)
            Grid.columnconfigure(frame_canva, 0, weight=1)

            dic = sim.return_dic()
            age = list(dic.keys())
            value = list(dic.values())

            fig, ax = plt.subplots()
            ax.plot(age, sim.get_tm(), marker='o', label='Mortalidad general', color='tab:purple')
            ax.plot(age, value, marker='o', label='Mortalidad por PM2.5', color='tab:green')
            ax.set_title('Mortalidad por cancer pulmonar', loc="center",
                         fontdict={'fontsize': 14, 'fontweight': 'bold'})
            ax.set_xlabel("Año")
            ax.set_ylabel("Fracción de mortalidad")
            ax.set_yticks(range(1, 8))
            plt.grid(axis='y', color='gray', linestyle='dashed')
            plt.legend()

            canva = FigureCanvasTkAgg(fig, master=frame_canva)
            canva.draw()
            canva.get_tk_widget().grid(pady=10, padx=10, row=1, column=0, columnspan=3, sticky="nsew")
        except:
            messagebox.showerror("Error", "Sin datos.")

    def page2():
        try:
            frame_canva.grid_forget()
            frame_canva.grid(padx=10, pady=5, row=0, column=1, sticky="nsew", rowspan=3)
            Grid.rowconfigure(frame_canva, 1, weight=1)
            Grid.columnconfigure(frame_canva, 0, weight=1)

            dic = sim.return_dic()
            if dic:
                age = list(dic.keys())
                value = list(dic.values())

            fig, ax = plt.subplots()
            ax.plot(age, value, marker='o', label='Mortalidad por PM2.5', color='tab:green')
            ax.set_title('Mortalidad por cancer pulmonar atribuible a PM2.5', loc="center",
                         fontdict={'fontsize': 14, 'fontweight': 'bold'})
            ax.set_xlabel("Año")
            ax.set_ylabel("Fracción de mortalidad")
            plt.grid(axis='y', color='gray', linestyle='dashed')
            plt.legend()

            canva = FigureCanvasTkAgg(fig, master=frame_canva)
            canva.draw()
            canva.get_tk_widget().grid(pady=10, padx=10, row=1, column=0, columnspan=3, sticky="nsew")
        except:
            messagebox.showerror("Error", "Sin datos.")

    def page3():
        try:
            frame_canva.grid_forget()
            frame_canva.grid(padx=10, pady=5, row=0, column=1, sticky="nsew", rowspan=3)
            Grid.rowconfigure(frame_canva, 1, weight=1)
            Grid.columnconfigure(frame_canva, 0, weight=1)

            data = sim.get_cdf_data()
            count, bins_count = np.histogram(data, bins=10)
            pdf = count / sum(count)
            cdf = np.cumsum(pdf)

            fig, ax = plt.subplots()
            ax.plot(bins_count[1:], pdf, color="red", label="PDF")
            ax.plot(bins_count[1:], cdf, label="CDF")
            plt.legend()

            canva = FigureCanvasTkAgg(fig, master=frame_canva)
            canva.draw()
            canva.get_tk_widget().grid(pady=10, padx=10, row=1, column=0, columnspan=3, sticky="nsew")
        except:
            messagebox.showerror("Error", "Sin datos.")

    #Botones para seleccionar las graficas
    frame_button = LabelFrame(frame_canva, padx=1, pady=1)
    frame_button.grid(padx=10, pady=5, row=0, column=0, sticky="nw")
    comp_button = Button(frame_button, text="Mortalidad Comparación", padx=2, pady=2, command=page1)
    comp_button.grid(pady=2, padx=2, row=0, column=0, sticky="nw")
    hist_button = Button(frame_button, text="Mortalidad por Pm2.5", padx=2, pady=2, command=page2)
    hist_button.grid(pady=2, padx=2, row=0, column=1, sticky="nw")
    rrplot_button = Button(frame_button, text="Función de distribucion acumulativa", padx=2, pady=2, command=page3)
    rrplot_button.grid(pady=2, padx=2, row=0, column=2, sticky="nw")

    #Canva con las graficas
    frame.update_idletasks()
    simulationchart = Canvas(frame_canva, bg="#596869")
    simulationchart.grid(pady=5, padx=5, row=1, column=0, columnspan=3, sticky="nsew")

    root.mainloop()


if __name__ == '__main__':
    main()

