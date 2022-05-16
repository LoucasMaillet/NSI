# -*- coding: utf-8 -*-
"""
Mini projet automate cellulaire - simulation d'un feu de forêt

Partie 1 : AUTOMATE CELLULAIRE

@author: 
"""

from random import sample


# variables globales
epoque = 0

# variables globales modifiés/ajoutés
etats_ac = {
    "arbres_en_vie": 0,
    "arbres_en_feu": 0,
    "arbres_en_cendres" : 0,
    "vitesse_du_feu": 0,
    "vivable": 1.0
}
nb_tirages = 0


def tirage_aleatoire(p, n):
    global nb_tirages
    nb_tirages = int(p*n**2)
    return sample([(i, j) for j in range(n) for i in range(n)], nb_tirages)


def construction_grille(p, n):
    etats_ac['arbres_en_vie'] = int(p*n**2)
    etats_ac['arbres_en_feu'] = 0
    etats_ac['arbres_en_cendres'] = 0
    grille=[[0 for col in range(n)] for ligne in range(n)]
    arbres = tirage_aleatoire(p, n)
    for i in range(n):
        for j in range(n):
            if (i,j) in arbres:
                grille[i][j] = 1
    return grille


def affichage_grille(grille):
    global epoque
    print(f"époque {epoque}: {etats_ac['arbres_en_feu']} arbres en feu")
    epoque += 1
    for l in grille:
        print(*l)
    print()
    # TODO : question 4
        

def voisins(n, i, j):
    # TODO : question 1
    return [(x, y) for (x, y) in ((i-1, j), (i+1, j), (i, j-1),(i, j+1)) if 0 <= x < n and 0 <= y < n]


def mise_a_jour_grille(grille):
    # TODO : question 2
    n = len(grille)
    en_feu_avant = etats_ac['arbres_en_feu']
    en_feu = []
    for i in range(n):
        for j in range(n):
            if grille[i][j] == 2:
                grille[i][j] = 3
                etats_ac['arbres_en_feu'] -= 1
                etats_ac['arbres_en_cendres'] += 1
                voisins_ij = voisins(n,i,j)
                for (x,y) in voisins_ij:
                   if (x,y) not in en_feu and grille[x][y] == 1:
                       en_feu.append((x,y))
    for (x,y) in en_feu:
        grille[x][y] = 2
    etats_ac['arbres_en_vie'] -= len(en_feu)
    etats_ac['arbres_en_feu'] += len(en_feu)
    etats_ac['vivable'] = round(etats_ac['arbres_en_vie'] / nb_tirages, 2)
    etats_ac['vitesse_du_feu'] = etats_ac['arbres_en_feu'] - en_feu_avant
    return etats_ac['arbres_en_feu'] > 0
               

if __name__=='__main__':
    parcelle = construction_grille(0.6, 8)
    parcelle[0][0] = 2
    etats_ac['arbres_en_vie'] -= 1
    etats_ac['arbres_en_feu'] += 1
    affichage_grille(parcelle)
    # TODO : question 3
    while mise_a_jour_grille(parcelle):
        affichage_grille(parcelle)
    affichage_grille(parcelle)        


