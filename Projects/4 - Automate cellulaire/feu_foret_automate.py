#!/usr/bin/env python3.8
#coding: utf-8
"""
Mini projet automate cellulaire - simulation d'un feu de forêt

Partie 1 : AUTOMATE CELLULAIRE

@author: Lucas Maillet
"""


from time import sleep
from random import sample


# State possible for each cell
ST_NULL = 0
ST_ALIVE = 1
ST_FIRE = 2
ST_DEAD = 3
# Delay between each update (in seconde)
T_DELAY = 2


# variables globales
epoque = 0
etats_ac = {
    'arbres_en_vie': 0,
    'arbres_en_feu': 0,
    'arbres_en_cendres': 0,
    'previous_fires': 0,
    'velocity': 0
}


def tirage_aleatoire(p, n):
    nb_tirages = int(p*n**2)
    return sample([(i, j) for j in range(n) for i in range(n)], nb_tirages)


def construction_grille(p, n):
    etats_ac['arbres_en_vie'] = int(p*n**2)
    etats_ac['arbres_en_feu'] = 0
    etats_ac['arbres_en_cendres'] = 0
    grille = [[ST_NULL for col in range(n)] for ligne in range(n)]
    arbres = tirage_aleatoire(p, n)
    for i in range(n):
        for j in range(n):
            if (i, j) in arbres:
                grille[i][j] = ST_ALIVE
    return grille


def affichage_grille(grille):
    global epoque
    print(
        f"Time {epoque}:\nFires: {etats_ac['arbres_en_feu']}\nVélocity: {round(etats_ac['arbres_en_feu'] / (epoque or 1), 2)} fires/time\nEvolution: {etats_ac['arbres_en_feu'] - etats_ac['previous_fires']} fires")
    epoque += 1
    for l in grille:
        print(*l)
    print()


def voisins(n, i, j):
    n -= 1
    neighbors = []
    # Hummm some spaggettie code (but optimized)
    if i > 0:
        neighbors.append((i-1, j))
    if i < n:
        neighbors.append((i+1, j))
    if j > 0:
        neighbors.append((i, j-1))
    if j < n:
        neighbors.append((i, j+1))
    return neighbors


def mise_a_jour_grille(grille):
    global etats_ac
    global epoque
    i = 0
    n = len(grille)
    on_fire = set()
    etats_ac['previous_fires'] = etats_ac['arbres_en_feu']
    while i < n:
        j = 0
        while j < n:
            if grille[i][j] == ST_FIRE:
                etats_ac['arbres_en_feu'] -= 1
                etats_ac['arbres_en_cendres'] += 1
                grille[i][j] = ST_DEAD
                for i_n, j_n in voisins(n, i, j):
                    if grille[i_n][j_n] == ST_ALIVE:
                        on_fire.add((i_n, j_n))
            j += 1
        i += 1
    for i, j in on_fire:
        grille[i][j] = ST_FIRE
        etats_ac['arbres_en_feu'] += 1
        etats_ac['arbres_en_vie'] -= 1
    return etats_ac['arbres_en_feu'] > 0


if __name__ == '__main__':
    parcelle = construction_grille(0.6, 8)
    parcelle[0][0] = ST_FIRE
    etats_ac['arbres_en_vie'] -= 1
    etats_ac['arbres_en_feu'] += 1
    affichage_grille(parcelle)
    while mise_a_jour_grille(parcelle):
        try:
            affichage_grille(parcelle)
            sleep(T_DELAY)
        except KeyboardInterrupt:
            break
    affichage_grille(parcelle)
