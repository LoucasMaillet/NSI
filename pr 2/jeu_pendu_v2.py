# -*- coding: utf-8 -*-
"""
Mini-projet Jeu du pendu
Implémentation avec modification du mot à trouver (version 2)

@author: 
"""

from dessin_pendu import dessin_pendu, Frame
from jeu_pendu_v1 import importer_mots, choisir_mot, construire_mot_partiel, ajouter_lettre


def modifier_liste_mots(liste_mots: list, mot_choisi: str, lettres: list) -> str:
    """

    Parameters
    ----------
    liste_mots : TYPE LIST
        DESCRIPTION : The word's list to search.

    mot_choisi : TYPE STRING
        DESCRIPTION : The word already used.

    lettres : TYPE STRING
        DESCRIPTION : The characters already used.

    Returns
    -------
    res : TYPE LIST
        DESCRIPTION : The list sorted.

    """
    length = len(mot_choisi)
    return [word for word in liste_mots if len(word) == length and word != mot_choisi if all(not char in word for char in lettres)]


if __name__ == '__main__':

    liste_mots = importer_mots('mots.txt')
    mot_choisi = choisir_mot(liste_mots)
    mot_partiel = construire_mot_partiel(mot_choisi)
    screen, save_chars, errors = Frame(), [], 0

    screen(f"Word to find : {mot_partiel}",
           screen.center_x_block(dessin_pendu(errors), 10), 
           "Type a character")

    while errors != 6:

        char = input()
        save_chars.append(char)
        errors += 1

        if char in mot_choisi:
            mot_nouveau = modifier_liste_mots(liste_mots, mot_choisi, save_chars)
            if mot_nouveau == []:
                break
            mot_choisi = choisir_mot(mot_nouveau)

        screen(f"Word to find : {construire_mot_partiel(mot_choisi)}",
               screen.center_x_block(dessin_pendu(errors), 10),
               f"You already use : {', '.join(save_chars)}")

    screen("Game Over",
           f"You {'win' if errors != 6 else 'loose'} with {errors} errors.",
           f" The word was {mot_choisi}")
