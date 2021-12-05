# -*- coding: utf-8 -*-
"""
TP4 Python: TP_traitement données en table_Partie I exercice 1

Finished at 19:45 am 03/12/21.
By Lucas Maillet.
"""


from pylab import plot, xlabel, ylabel, legend, show


if __name__ == "__main__":

    with open("ballonsonde.csv") as file:
        data = [l.split(";") for l in file.readlines()]

    label_x, label_y = data.pop(0)
    alts = []
    temps = []

    for alt, temp in data:
        alts.append(int(alt))
        temps.append(float(temp))

    plot(alts, temps, "-", label="T°C = f(altitude)", linewidth=2)
    xlabel(label_x)
    ylabel(label_y)
    legend()
    show()