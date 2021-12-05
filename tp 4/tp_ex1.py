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

    x_label, y_label = data.pop(0)
    x_data, y_data = [], []

    for x, y in data:
        x_data.append(int(x))
        y_data.append(float(y))

    plot(x_data, y_data, "-", label="T°C = f(altitude)", linewidth=2)
    xlabel(x_label)
    ylabel(y_label)
    legend()
    show()
