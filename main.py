import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from main_simulation import main_simulation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = Tk()
root.geometry("800x500")
root.title("Simualción Mortalidad Cancer Pulmonar PM2.5")
root.state("zoomed")
root.minsize(width=1000, height=600)
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
    iterationScale = Scale(frame, from_=400, to=1000, orient="horizontal", tickinterval=200,
                           length=root.winfo_width()/5, width=10, resolution=200)
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

            plt.close()
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

        except Exception as e:
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

            plt.close()
            fig, ax = plt.subplots()
            ax.plot(age, value, marker='o', label='Mortalidad por PM2.5', color='tab:orange')
            ax.set_title('Mortalidad por cancer pulmonar atribuible a PM2.5', loc="center",
                         fontdict={'fontsize': 14, 'fontweight': 'bold'})
            ax.set_xlabel("Año")
            ax.set_ylabel("Fracción de mortalidad")
            plt.grid(axis='y', color='gray', linestyle='dashed')
            plt.legend()

            canva = FigureCanvasTkAgg(fig, master=frame_canva)
            canva.draw()
            canva.get_tk_widget().grid(pady=10, padx=10, row=1, column=0, columnspan=3, sticky="nsew")

        except Exception as e:
            messagebox.showerror("Error", "Sin datos.")

    def page3():
        try:

            frame_canva.grid_forget()
            frame_canva.grid(padx=10, pady=5, row=0, column=1, sticky="nsew", rowspan=3)
            Grid.rowconfigure(frame_canva, 1, weight=1)
            Grid.columnconfigure(frame_canva, 0, weight=1)

            data = sim.get_cdf_data()
            if data:
                count, bins_count = np.histogram(data, bins=10)
                pdf = count / sum(count)
                cdf = np.cumsum(pdf)

            plt.close()
            fig, ax = plt.subplots()
            ax.set_title('Función de probalidad acumulativa', loc="center",
                         fontdict={'fontsize': 14, 'fontweight': 'bold'})
            ax.set_xlabel("Tasa de Mortalidad")
            ax.set_ylabel("F(x)")
            ax.plot(bins_count[1:], pdf, color="red", label="PDF")
            ax.plot(bins_count[1:], cdf, label="CDF")
            plt.grid(axis='y', color='gray', linestyle='dashed')
            plt.legend()

            canva = FigureCanvasTkAgg(fig, master=frame_canva)
            canva.draw()
            canva.get_tk_widget().grid(pady=10, padx=10, row=1, column=0, columnspan=3, sticky="nsew")

        except:
            messagebox.showerror("Error", "Sin datos.")

    def page4():
        try:
            frame_canva.grid_forget()
            frame_canva.grid(padx=10, pady=5, row=0, column=1, sticky="nsew", rowspan=3)
            Grid.rowconfigure(frame_canva, 1, weight=1)
            Grid.columnconfigure(frame_canva, 0, weight=1)

            data_table = ttk.Treeview(frame_canva, columns=("PM2.5", "TM", "B", "AF", "RR", "TMPM2.5"))

            data_table.column("#0", width=90, anchor="center")
            data_table.column("PM2.5", width=110, anchor="center")
            data_table.column("TM", width=110, anchor="center")
            data_table.column("B", width=110, anchor="center")
            data_table.column("AF", width=110, anchor="center")
            data_table.column("RR", width=110, anchor="center")
            data_table.column("TMPM2.5", width=130, anchor="center")

            data_table.heading("#0", text="Año")
            data_table.heading("PM2.5", text="PM2.5 Anual")
            data_table.heading("TM", text="TM")
            data_table.heading("B", text="Beta")
            data_table.heading("AF", text="AF")
            data_table.heading("RR", text="RR")
            data_table.heading("TMPM2.5", text="TM atribuible a Pm2.5")

            data_table.grid(pady=10, padx=10, row=1, column=0, sticky="nsew")

            data = sim.getDataMetrix()
            anual_avg_af = sim.get_anualaf()
            anual_avg_rr = sim.get_anualrr()
            anual_avg_tm = sim.get_tmpm()
            for n in range(len(data)):
                data_table.insert("", END, text=str(data[n][0]),
                                  values=(str(data[n][1]), str(data[n][2]), str(sim.getBeta()),
                                          anual_avg_af[n], anual_avg_rr[n],anual_avg_tm[n] ))


        except Exception as e:
            messagebox.showerror("Error", "Sin datos.")
            print(e)

    #Botones para seleccionar las graficas
    frame_button = LabelFrame(frame_canva, padx=1, pady=1)
    frame_button.grid(padx=10, pady=5, row=0, column=0, sticky="nw")
    comp_button = Button(frame_button, text="Mortalidad Comparación", padx=2, pady=2, command=page1)
    comp_button.grid(pady=2, padx=2, row=0, column=0, sticky="nw")
    hist_button = Button(frame_button, text="Mortalidad por Pm2.5", padx=2, pady=2, command=page2)
    hist_button.grid(pady=2, padx=2, row=0, column=1, sticky="nw")
    rrplot_button = Button(frame_button, text="Función de distribucion acumulativa", padx=2, pady=2, command=page3)
    rrplot_button.grid(pady=2, padx=2, row=0, column=2, sticky="nw")
    data_table_button = Button(frame_button, text="Tabla de resultados", padx=2, pady=2, command=page4)
    data_table_button.grid(pady=2, padx=2, row=0, column=3, sticky="nw")

    #Canva con las graficas
    frame.update_idletasks()
    simulationchart = Canvas(frame_canva, bg="#596869")
    simulationchart.grid(pady=5, padx=5, row=1, column=0, columnspan=3, sticky="nsew")

    root.mainloop()


if __name__ == '__main__':
    main()
