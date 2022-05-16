#!/usr/bin/env python3
# coding: utf-8

"""
Tp Algo glouton : compression de données par codage de Huffman   

@author: Lycee Louis Armand
"""

from heapq import heapify, heappush, heappop


# =============================================================================
# Construction de la table des fréquences
# =============================================================================

def table_frequences(texte : str) -> dict:
    occ = {}
    for item in texte:
        if item in occ:
            occ[item] += 1
        else:
            occ[item] = 1
    return occ


# =============================================================================
# Construction de l'arbre de Huffman
# ============================================================================= 

def arbre_huffman(dico_occ : dict):
    tas = [(occ, i, lettre) for i, (lettre, occ) in enumerate(dico_occ.items())]
    heapify(tas)
    i = len(tas)
    while len(tas) >= 2:
        occ1, _, label1 = heappop(tas)
        occ2, _, label2 = heappop(tas)
        heappush(tas, (occ1+occ2, i, {'0': label1, '1': label2}))
        i += 1            
    return heappop(tas)[2]


# =============================================================================
# Construction du dictionnaire {mot_binaire : caractère}
# =============================================================================

def parcours_arbre(arbre : str, prefixe : str, codes : dict):
    for noeud in arbre.keys():
        if len(arbre[noeud]) == 1:
            codes[prefixe+noeud] = arbre[noeud]
        else:
            parcours_arbre(arbre[noeud], prefixe+noeud, codes)
    
    
def code_huffman(arbre):
    codes = {}
    parcours_arbre(arbre, '', codes)
    return codes


# =============================================================================
# Encodage d'un texte à partir du code de Huffman
# =============================================================================

def encodage(texte: str):
    code = code_huffman(arbre_huffman(table_frequences(texte)))
    code = dict(zip(code.values(), code.keys()))
    res = ""
    for char in texte:
        res += code[char]
    return res


# =============================================================================
# Calcul du taux de compression (Huffman vs ASCII)
# =============================================================================

def taux_compression(texte : str):
    len_default = len(texte) * 8
    return round((len_default - len(encodage(texte))) / len_default * 100, 2)

# =============================================================================
# Décodage d'un fichier binaire à partir du code de Huffman
# =============================================================================

def decodage(codes : dict,chaine_binaire : str) -> str:
    res = ""
    bit_buffer = ""
    for bit in chaine_binaire:
        bit_buffer += bit
        if bit_buffer in codes:
            res += codes[bit_buffer]
            bit_buffer = ""
#     return res
    
# with open("tour_du_monde.txt") as file:
#     texte = file.read()
#     code = code_huffman(arbre_huffman(table_frequences(texte)))
#     encoded = encodage(texte)
#     # print(encoded)
#     # print(taux_compression(texte))
#     #print(decodage(code, encoded))

if __name__ == "__main__":
    
    import timeit
    
    def bench():
        with open("tour_du_monde.txt") as file:
            text = file.read()
            return arbre_huffman(table_frequences(text))
        
    print(f"Bench took approximatly {timeit.timeit(bench, number=100)} ms")
