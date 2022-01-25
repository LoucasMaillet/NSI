# -*- coding: utf-8 -*-
"""
Mini-projet sur le code Morse
@author: lucas-maillet

Readme
----------
Ces fonctions ne fonctionnent que si les
conditions dans leur description sont respectées,
car elles ne font que le minimum attendue,
autrement regarder code_morse_v2.py.
"""


from typing import Iterable


alph_latin = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

code_morse = [".-/", "-.../", "-.-./", "-../", "./", "..-./", "--./",
              "..../ ", "../", ".---/", "-.-/", ".-../", "--/", "-./",
              "---/", ".--./", "--.-/", ".-./", ".../", "-/", "..-/",
              "...-/", ".--/", "-..-/", "-.--/", "--../"]

# =============================================================================
# PARTIE 1 : Fonctions d'encodage et de décodage
# =============================================================================


def encoder(mot: str, alphabet: Iterable, codage: Iterable) -> str:
    """

    Description
    ----------
    Unoptimized, call .index() for each characters.
    Encode strict uppercase alphabetic word to morse sequence.

    Parameters
    ----------
    mot : STRING
        Alphabetic word to encode.
    alphabet : ITERABLE
        List of strict uppercase alphabetic characters.
    codage : ITERABLE
        List of morse characters corresponding to alphabet.

    Returns
    -------
    res : STRING
        Word encoded.

    """

    res = ""
    for letter in mot:
        res += codage[alphabet.index(letter)]

    return res


def decoder(sequence: str, alphabet: Iterable, codage: Iterable) -> str:
    """

    Description
    ----------
    Unoptimized, call .index() for each buffer of sequence.
    Decode morse sequence to strict uppercase alphabetic word.

    Parameters
    ----------
    sequence : STRING
        Morse sequence to decode.
    alphabet : ITERABLE
        List of strict uppercase alphabetic characters.
    codage : ITERABLE
        List of morse characters corresponding to alphabet.

    Returns
    -------
    res : STRING
        Sequence decoded.

    """

    res = buffer = ""
    for c in sequence:
        buffer += c
        if c == "/":
            res += alphabet[codage.index(buffer)]
            buffer = ""

    return res


# =============================================================================
# PARTIE 2 : Prise en compte des erreurs d'encodage
# =============================================================================

def decoder_2(sequence: str, alphabet: Iterable, codage: Iterable) -> str:
    """

    Description
    ----------
    Unoptimized, call .index() for each buffer of sequence and use try/except instead of test.
    Decode morse sequence to strict uppercase alphabetic word.
    Handle transcription errors with '_'.

    Parameters
    ----------
    sequence : STRING
        Morse sequence to decode.
    alphabet : ITERABLE
        List of strict uppercase alphabetic characters.
    codage : ITERABLE
        List of morse characters corresponding to alphabet.

    Returns
    -------
    res : STRING
        Sequence decoded.

    """

    res = buffer = ""
    for c in sequence:
        buffer += c
        if c == "/":
            try:
                res += alphabet[codage.index(buffer)]
            except ValueError:
                res += "_"
            buffer = ""

    return res


# =============================================================================
# TESTS
# =============================================================================

#toEnc = "INFORMATIQUE"
#toDec = "-./..-/--/./.-./../--.-/..-/./"
#toDec_2 = "../-./..-./---./.-./--/.-/-/../--.-/..-/./"
#print(f"""encoder:\n\ttext: {toEnc}\n\tseq: {encoder(toEnc, alph_latin, code_morse)}\n\ndecoder:\n\ttext: {decoder(toDec, alph_latin, code_morse)}\n\tseq: {toDec}\n\ndecoder_2:\n\ttext: {decoder_2(toDec_2, alph_latin, code_morse)}\n\tseq: {toDec_2}""")