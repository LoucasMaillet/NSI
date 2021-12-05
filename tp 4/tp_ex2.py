# -*- coding: utf-8 -*-
"""
TP4 Python: TP_traitement données en table_Partie I exercice 2

Finished at 19:45 am 03/12/21.
By Lucas Maillet.
"""


from pylab import figure, plot, xlabel, ylabel, legend, show


# UTILS
def create_window(title: str):
    """

    Description
    -----------
    Create a new window.

    Parameters
    ----------
    title : STRING
        The window's title.

    """
    figure(title)
    xlabel("Années")
    ylabel("Population")


# EXERCICE 2
def pop_o_19(data: list) -> list:
    """

    Description
    -----------
    Get a portion from database with everybody between 0-19 years old.

    Parameters
    ----------
    data : LIST
        The database where you search.

    Returns
    -------
    LIST
        The database sorted.

    """
    return [(year, pop) for year, age, pop in data if age == "0-19 ans"]


# EXERCICE 3
def scinde_liste(data: list) -> list:
    """

    Description
    -----------
    Cut in two a database : one for the year, 
    the other for the populations.

    Parameters
    ----------
    data : LIST
        The database you want to cut.

    Returns
    -------
    years : LIST
        All the years from data.

    pops : LIST
        All the populations from data.

    """
    years, pops = [], []
    for year, pop in data:
        years.append(year)
        pops.append(pop)
    return years, pops


# EXERCICE 4
def trace_graph(data: list):
    """

    Description
    -----------
    Draw a graphical representation of data.

    Parameters
    ----------
    data : LIST
        The data you want to show.

    """
    create_window("Exercice 3 - 4")
    plot(*data, '-', label="0 à 19 ans", linewidth=2)
    legend()


# EXERCICE 5
def genere_csv(data: list, file_path: str):
    """

    Description
    -----------
    Save data in file as .csv format.

    Parameters
    ----------
    data : LIST
        The data you want to save.

    file_path : STRING
        The file location.

    """
    with open(f"{file_path}.csv", 'w') as file:
        for year, pop in data:
            file.write(f"{year};{pop}\n")


# EXERCICE 6
def pop_tranche_age(data: list) -> dict:
    """

    Description
    -----------
    Sort data into a dictionary of [(year, population), ... ] for age range.

    Parameters
    ----------
    data : LIST
        The database you want to sort.

    Returns
    -------
    res : DICTIONARY
        The database sorted.

    """
    res = {}
    for year, age, pop in data:
        if age in res:
            res[age].append((year, pop))
        else:
            res[age] = [(year, pop)]
    return res


# EXERCICE 8
def pop_total(data: list) -> list:
    """

    Description
    -----------
    Sort data into a list of tuple [(year, pop_total_for_year), ... ].

    Parameters
    ----------
    data : LIST
        The database you want to sort.

    Returns
    -------
    res : LIST
        The total of population by years.

    """    
    res = {}
    for year, _, pop in data:
        res[year] = res.get(year, 0) + pop
    return list(res.items())


# TESTS
if __name__ == "__main__":

    # EXERCICE 1
    with open("Population.csv") as file:
        contenu_fichier = [[int(year), age, int(pop)] for line in file.readlines() for year, age, pop in (line.split(";"),)]
            
    # EXERCICE 2
    population_0_19 = pop_o_19(contenu_fichier)

    # EXERCICE 3 - 4
    trace_graph(scinde_liste(population_0_19))

    # EXERCICE 5
    genere_csv(population_0_19, "population_0_19")

    # EXERCICE 6 - 7
    create_window("Exercice 6 - 7 - 8 - 9")
    for age, pops in pop_tranche_age(contenu_fichier).items():
        plot(*scinde_liste(pops), '-', label=age, linewidth=2)

    # EXERCICE 8 - 9
    plot(*scinde_liste(pop_total(contenu_fichier)),
         '--', label="Tous", linewidth=3)
    legend()

    show()
