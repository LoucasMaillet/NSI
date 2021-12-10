# -*- coding: utf-8 -*-
"""
Mini-projet Jeu du pendu
Implémentation selon les règles du jeu (version 1)

@author: 
"""

from random import choice
from dessin_pendu import dessin_pendu, Frame


def importer_mots(fichier: str) -> list:
    """

    Description
    -----------
    Import words from a file.

    Parameters
    ----------
    fichier : TYPE STRING
        DESCRIPTION : File's path.

    Returns
    -------
    TYPE LIST
        DESCRIPTION : Every word for each line of file.

    """
    with open(fichier) as file:
        return [w.rstrip() for w in file.readlines()]


def choisir_mot(liste_mots: list) -> str:
    """

    Description
    -----------
    Choose randomly a word in a list.

    Parameters
    ----------
    liste_mots : TYPE LIST
        DESCRIPTION : The list from you want a random item.

    Returns
    -------
    TYPE STRING
        DESCRIPTION : A random item from liste_mots.

    """
    return choice(liste_mots)


def construire_mot_partiel(mot_choisi: str) -> str:
    """

    Description
    -----------
    Create a hidden representation of word.

    Parameters
    ----------
    mot_choisi : TYPE STRING 
        DESCRIPTION : The word you want to hide.

    Returns
    -------
    TYPE STRING 
        DESCRIPTION : The word hidded.

    """
    return ("_ "*len(mot_choisi))[:-1]  # ' '.join('_' for _ in mot_choisi)


def ajouter_lettre(lettre: str, mot_choisi: str, mot_partiel: str) -> str:
    """

    Description
    -----------
    Update a hidden word with a character.

    Parameters
    ----------
    lettre : TYPE STRING
        DESCRIPTION : The character to update.

    mot_choisi : TYPE STRING
        DESCRIPTION : The original word.

    mot_partiel : TYPE STRING
        DESCRIPTION : The hidden word.

    Returns
    -------
    TYPE STRING
        The hidden word updated.

    """
    return ' '.join(lettre if mot_choisi[i] == lettre else c for i, c in enumerate(mot_partiel.split(' ')))


if __name__ == '__main__':

    liste_mots = importer_mots('mots.txt')
    mot_choisi = choisir_mot(liste_mots)
    mot_partiel, mot_partiel_end = construire_mot_partiel(mot_choisi), ' '.join(mot_choisi)
    screen, save_chars, errors = Frame(), [], 0

    screen(f"Word to find : {mot_partiel}",
           screen.center_x_block(dessin_pendu(errors), 10), 
           "Type a character")

    while errors != 6:

        char = input()
        save_chars.append(char)
        
        if not char in mot_choisi or char in mot_partiel:
            errors += 1
        else:
            mot_partiel = ajouter_lettre(char, mot_choisi, mot_partiel)
            if mot_partiel == mot_partiel_end:
                break
            
        screen(f"Word to find : {mot_partiel}",
               screen.center_x_block(dessin_pendu(errors), 10),
               f"You already use : {', '.join(save_chars)}")

    screen("Game Over",
           f"You {'win' if errors != 6 else 'loose'} with {errors} errors.",
           f" The word was {mot_choisi}")
