# -*- coding: utf-8 -*-
"""
TP4 Python: TP_traitement données en table_Partie I exercice 1

Finished at 19:45 am 03/12/21.
By Lucas Maillet.
"""


from pylab import plot, xlabel, ylabel, legend, show


if __name__ == "__main__":

    valeurs_alt, valeurs_temp = [], []

    with open("ballonsonde.csv") as file:
        
        labelx, labely = file.readline().rstrip().split(";")
        
        for line in file.readlines():
            alt, temp = line.split(";")
            valeurs_alt.append(int(alt))
            valeurs_temp.append(float(temp))
            
    plot(valeurs_alt, valeurs_temp, "-", label="T°C = f(altitude)", linewidth=2)
    xlabel(labelx)
    ylabel(labely)
    legend()
    show()