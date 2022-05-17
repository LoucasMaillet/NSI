# -*- coding: utf-8 -*-
"""
Mini-projet sur le code Morse (version amelioré)
@author: lucas-maillet

Readme
----------
Ces fonctions utilisent cet alphabet:
    ABCDEFGKLMNOPQRSTUVWXYZ
    0123456789
    .,?:=/×
    \s
Avec une gestion des problemes de transcription (code: ERROR / ........).
"""

alphMorse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": ".... ",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    ":": "---...",
    "=": "−···−",
    "-": "-....-",
    "/": "-..-.",
    "×": ".-.-.",
    " ": ".......",
    "ERROR": "........"
}
morseAlph = dict(zip(alphMorse.values(), alphMorse.keys()))

# =============================================================================
# PARTIE 1 : Fonctions d'encodage et de décodage
# =============================================================================


def encoder(sentence: str) -> str:
    """

    Description
    ----------
    Encode sentence to morse sequence.

    Parameters
    ----------
    sentence : STRING
        Alphabetic sentence to encode.

    Returns
    -------
    res : STRING
        Sentence encoded.

    """

    res = ""
    for letter in sentence.upper():
        if letter in alphMorse:
            res += f"{alphMorse[letter]}/"
        else:
            res += f"{alphMorse['ERROR']}/"

    return res


def decoder(sequence: str) -> str:
    """

    Description
    ----------
    Decode morse sequence to an uppercase sentence.

    Parameters
    ----------
    sequence : STRING
        Morse sequence to decode.

    Returns
    -------
    res : STRING
        Sequence decoded.

    """

    res = buffer = ""

    for c in sequence:
        if c == "/":
            if buffer in morseAlph:
                res += morseAlph[buffer]
            else:
                res += "_"
            buffer = ""
        else:
            buffer += c

    return res


# =============================================================================
# TESTS
# =============================================================================

#seq0 = encoder("abcdefghijkmnlopqrstuvwxyz, 0123456789, .,?:=/× &")
#seq1 = encoder("? = 7×6 = 42 = the meaning of life")
#print(f"""First test: \n\tsequ: {seq0}\n\ttext: {decoder(seq0)}\n\nSecond test: \n\tsequ: {seq1}\n\ttext: {decoder(seq1)}""")
