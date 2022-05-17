#!/usr/bin/env python3.10
# #coding: utf-8

#  _ ____ _  _ ___  _    _ ____ _ ___    _  _ _  _ ___  ____ ____ ____ ___ ____ _  _ ___  _ _  _ ____ _
# |  |___  \/  |__] |    | |    |  |     |  | |\ | |  \ |___ |__/ [__   |  |__| |\ | |  \ | |\ | | __  |
# |_ |___ _/\_ |    |___ | |___ |  |     |__| | \| |__/ |___ |  \ ___]  |  |  | | \| |__/ | | \| |__] _|

# A useless piece of code made to show the explicit building in py object

def auteurs(bd: dict) -> list:
    # I choosed to use a set with convertion to list because adding
    # an author have a O(1) complexity unlike a list
    # wich have a O(n) complexity with n = len(list)
    return list(set(v[0] for v in bd.values()))


def titres_empruntables(bd: dict) -> list:
    return [k for k, v in bd.items() if v[1] > 0]


def titres_auteur(bd: dict, author: str) -> list:
    return [k for k, v in bd.items() if v[0] == author]


def auteurs_disponibles(bd: dict, n: int) -> list:
    return [k for k in auteurs(bd) if sum(bd[k_][1] for k_ in titres_auteur(bd, k)) >= n]


def ajout(bd: dict, author: str, title: str, n: int) -> list:
    bd[title] = (author, n)


def emprunt(bd: dict, title: str, n: int = 1) -> list:
    if bd[title][1] < n:
        return False
    bd[title] = (bd[title][0], bd[title][1] - n)
    return True


def conversion(bd: dict) -> dict:
    return {k: list(v) for k, v in bd.items()}


if __name__ == "__main__":

    from timeit import timeit

    LivresBD = {"Les misérables": ("Victor Hugo", 6), "L'assommoir": ("Emile Zola", 15),
                "Le dernier des Mohicans": ("James F. Cooper", 0), "Les travailleurs de la mer": ("Victor Hugo", 5),
                "Au bonheur des dames": ("Emile Zola", 5), "Un animal doué de raison": ("Robert Merle", 6),
                "Les pionniers": ("James F. Cooper", 3), "Le grand Meaulnes": ("Alain Fournier", 4),
                "Notre-Dame de Paris": ("Victor Hugo", 8), "Les contemplations": ("Victor Hugo", 0),
                "La prairie": ("James F. Cooper", 12), "Germinal": ("Emile Zola", 0)}

    print(auteurs(LivresBD))
    print(titres_empruntables(LivresBD))
    print(titres_auteur(LivresBD, "Victor Hugo"))
    print(auteurs_disponibles(LivresBD, 15))
    ajout(LivresBD, "Philip K. Dick", "Les androïdes rêvent-ils de moutons électriques?", 18)
    print(LivresBD)
    print(emprunt(LivresBD, "Les misérables", 2))
    print(LivresBD)
    print(conversion(LivresBD))

    print(f"""Bench ended in {timeit("auteurs(LivresBD)", setup="from __main__ import auteurs, LivresBD", number=100)}""")
