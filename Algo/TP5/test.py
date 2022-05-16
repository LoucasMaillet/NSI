# NSI Première Louis-Armand
# Programme de Test à l'aide de pytest

#on importe le module pytest
import pytest
#on importe le module random pour créer les listes aléatoires
import random
#on importe le fichier qui contient les tris
import tris



# on enregistre dans une liste les différents tris à tester
tris_tests = [tris.tri_par_insertion, tris.tri_par_selection]

#on enregistre dans une liste les différentes listes qu'on va trier.
liste_tests=[[random.randint(0, 200) for _ in range(200)] for _ in range(50)]

#Fonction qui vérifie qu'une liste passée en argument est triée.
def estTrie(liste):
    """ Vérifie que la liste passée en arguments est triée
    Prend une liste en argument :
    renvoie True si la liste est triée et False si elle ne l'est pas"""
    for i in range(1, len(liste)):
        if liste[i-1] > liste[i]:
            return False
    return True
   

#la fonction test_trie sera lancée automatiquement par pytest.
#on lui a passé comme paramètres les deux tris et les listes à trier
@pytest.mark.parametrize('tris',tris_tests)
@pytest.mark.parametrize('entree',liste_tests)   
def test_trie(tris,entree):
    tris(entree)
    assert estTrie(entree)



#  lancement de pytest
if __name__ == '__main__':
    pytest.main(args=[__file__])