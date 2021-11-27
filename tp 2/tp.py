# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 10:27:25 2021
@author: lucas.maillet

Some functions are useless, like occurences_str(),
wich is the same as occurences(),
but with other parameters type.
"""

from typing import Any, List
from time import time
from random import randint, shuffle


## EXERCICE I


def occurences(liste: list) -> dict:
    """

    Description
    ----------
    Get the number of occurences for each element of liste.

    Parameters
    ----------
    liste : LIST
        The list where you want to know the element's occurence.

    Returns
    -------
    res : DICTIONNARY
        Dictionnary with liste's elements as keys and values as occurences.

    """

    res = {}

    for v in liste:
        if v in res:
            res[v] += 1
        else:
            res[v] = 1

    return res


## EXERCICE II


def plusFrequent(dic: dict, n: int) -> str:
    """

    Description
    ----------
    Find the dic's key with a 'n' length and the biggest value.

    Parameters
    ----------
    dic : DICTIONNARY
        Dict where you search.

    n : INT
        The key length.

    Returns
    -------
    res : STRING
        The result key.

    """

    res = ""
    lastLen = 0

    for k in dic:
        if len(k) == n and dic[k] > lastLen:
            lastLen = dic[k]
            res = k

    return res


## EXERCICE III


def testOnFile(filePath: str) -> str:
    """

    Description
    ----------
    Iterable the 10 first more frequent word from text file.

    Parameters
    ----------
    filePath : STRING
        The file path.

    Returns
    -------
    res : STRING
        The results.

    """

    with open(filePath, "r") as file:
        occ = occurences(file.read().split())
        file.close()

    char = plusFrequent(occ, 1)
    res = f"1 lettre : {char} qui apparait {occ[char]} fois."

    for l in range(2, 11):
        char = plusFrequent(occ, l)
        res += f"\n\t{l} lettres : {char} qui apparait {occ[char]} fois."

    return res


## EXERCICE IV


def occurences_str(string: str) -> dict:
    """

    Description
    ----------
    Useless, should use 'occurences()'.
    Get the number of occurences for each letter of string.

    Parameters
    ----------
    string : STRING
        The string where you want to know the letter's occurence.

    Returns
    -------
    res : DICTIONNARY
        Dictionnary with string's letter as keys and values as occurences.

    """

    res = {}

    for v in string:
        if v in res:
            res[v] += 1
        else:
            res[v] = 1

    return res


## EXERCICE V


def compListes(l1: list, l2: list) -> bool:
    """

    Description
    ----------
    Test if two list have the same occurences.

    Parameters
    ----------
    l1 : LIST
        The first list you want to compare.

    l2 : LIST
        The second list you want to compare.

    Returns
    -------
    BOOLEAN
        If they have the same occurence or not.

    """

    return occurences(l1) == occurences(l2)


## EXERCICE VI


def rechercheDic(dic: dict, m: str) -> Any:
    """

    Description
    ----------
    Useless.
    Find a values with his key in a dict.

    Parameters
    ----------
    dic : DICTIONNARY
        The dic where you search.

    m : STRING
        The key of value.

    Returns
    -------
    STRING
        If they have the same occurence or not.

    """
    # return dic.get(m)
    return dic[m]


def rechercheListe(liste: List[list], m: str) -> Any:
    """

    Description
    ----------
    Useless.
    Find a values with his key in a list of list : list[ list[ ... , ... ], ... ].

    Parameters
    ----------
    liste : LISTE
        The list where you search.

    m : STRING
        The key of value.

    Returns
    -------
    STRING
        If they have the same occurence or not.

    """

    for k, v in liste:
        if k == m:
            return v


## TESTS


if __name__ == "__main__":

    tests = [
        [occurences, ([1, 5, 3, 8, 1, 2, 4, 6, 9, 2, 8, 3, 3],)],  # I
        [plusFrequent, ({"les": 5, "des": 8, "mes": 2, "aux": 6}, 3)],  # II
        [testOnFile, ("tour_du_monde.txt",)],  # III
        [occurences_str, ("ouagadougou",)],  # IV
        [compListes, ([1, 1, 1, 2, 2, 3, 3, 3, 3, 5], [
            1, 2, 3, 1, 2, 3, 1, 3, 5, 3])],  # V
        [compListes, ([1, 1, 1, 2, 2, 3, 3, 3, 3, 5], [
            1, 2, 3, 1, 2, 3, 1, 3, 5, 5])],  # V
        [compListes, ([1, 1, 1, 2, 2, 3, 3, 3, 3, 5], [1, 2, 3, 5])],  # V
        [rechercheDic, ({"oui": "yes", "non": "no", "bonjour": "hello",
                         "au revoir": "goodbye"}, "non")],  # VI
        [rechercheListe, ([["oui", "yes"], ["non", "no"], ["bonjour", "hello"], [
            "au revoir", "goodbye"]], "non")]  # VI
    ]

    # Test all functions

    for f, args in tests:
        print(f"Test on {f.__name__}, results:\n\n\t{f(*args)}\n")

    # Measure function execution time (VI)

    liste = [[i, i] for i in range(10**5)]
    shuffle(liste)
    dic = dict(liste)
    for loop in range(100):
        random = randint(0, 10**5)

        print(f"Loop n°{loop}:\n\n\tRandom: {random}")

        before = time()
        rechercheDic(dic, random)
        print(
            f"\tFunction 'rechercheDic' finished in {(time()-before)} seconds.")

        before = time()
        rechercheListe(liste, random)
        print(
            f"\tFunction 'rechercheListe' finished in {(time()-before)} seconds.\n")
