# -*- coding: utf-8 -*-
"""
Mini-projet Jeu du pendu
Implémentation selon les règles du jeu (version 1)

@author: 
"""

from random import choice
from dessin_pendu import dessin_pendu, Frame
from time import sleep


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
    return ("_ "*len(mot_choisi))[:-1]  # ' '.join('_' for _ in mot_choisi) # Depend on the word size


def ajouter_lettre(lettre: str, mot_choisi: str, mot_partiel: str) -> str:
    """

    Description
    -----------
    Update a hidden word with a stdinacter.

    Parameters
    ----------
    lettre : TYPE STRING
        DESCRIPTION : The stdinacter to update.

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
    frame = Frame()
    used_chars, used_chars_str, errors = [], '', 0

    @frame.loop
    def _frame_gen(f_count):
        frame(f"Hangman Game {['[   ]', '[=  ]', '[== ]', '[===]', '[ ==]', '[  =]', '[ ==]', '[===]', '[== ]', '[=  ]'][f_count%10]}",
              '',
              "Rules",
              '',
              "Type a latin character",
              "Retype a character has not effect",
              "You only have 6 chance to guess the word",
              '',
              "[Press Enter to start]")
        sleep(.1)

    mot_partiel, mot_end = construire_mot_partiel(
        mot_choisi), len(set(mot_choisi))

    input()  # wait user to press enter
    frame.loop_stop()

    try:

        frame(f"Word to find : {mot_partiel}",
              frame.center_x_block(dessin_pendu(errors), 10),
              "[Type a latin character]")

        while errors != 6 and mot_end != 0:

            stdin = input().upper()

            if stdin != '' and not stdin in used_chars:  # avoid empty character and retype issues

                used_chars.append(stdin)
                used_chars_str = ', '.join(used_chars)

                if len(stdin) == 1:  # check for a character

                    if not stdin in mot_choisi:
                        errors += 1

                    else:
                        mot_end -= 1
                        mot_partiel = ajouter_lettre(
                            stdin, mot_choisi, mot_partiel)

                else:  # check for a word

                    if stdin == mot_choisi:
                        break

                    else:
                        errors += 1

            frame(f"Word to find : {mot_partiel}",
                  frame.center_x_block(dessin_pendu(errors), 10),
                  f"You already use : {used_chars_str}")

        frame("Game Over",
              '',
              f"You {'win' if errors != 6 else 'loose'} with {errors} errors",
              f'The word was "{mot_choisi}"')

    except KeyboardInterrupt:
        frame("Game Over")
