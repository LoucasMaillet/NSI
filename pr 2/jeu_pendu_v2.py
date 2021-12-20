# -*- coding: utf-8 -*-
"""
Mini-projet Jeu du pendu
Implémentation avec modification du mot à trouver (version 2)

@author: 
"""

from dessin_pendu import dessin_pendu, Frame
from jeu_pendu_v1 import importer_mots, choisir_mot, construire_mot_partiel, ajouter_lettre
from time import sleep


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
    TYPE LIST
        DESCRIPTION : The list sorted.

    """
    length = len(mot_choisi)
    return [word for word in liste_mots if len(word) == length and word != mot_choisi if all(not char in word for char in lettres)]


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

                mot_nouveau = modifier_liste_mots(
                    liste_mots, mot_choisi, used_chars)
                if mot_nouveau != []:
                    mot_choisi = choisir_mot(mot_nouveau)

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
