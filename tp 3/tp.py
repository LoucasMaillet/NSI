# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 10:16:32 2021

@author: lucas.maillet
"""


# UTILS


def checkType(callback):
    """

    Description
    ----------
    Wrap a function to overide it if the specified arguments
    passed haven't the type required. 

    Warning
    ----------
    Work only on function with parameters specified in his
    declaration, example: def foo(a : str, b : int): ...
    Can not copy the parameters in the help, just the docstring.

    Parameters
    ----------    
    ctx : FUNCTION
        The function you want to supervise.

    Returns
    -------
    callback : FUNCTION
        The wrapped function.

    """
    f_kwargs = callback.__annotations__

    if "return" in f_kwargs:
        del f_kwargs["return"]

    f_args = list(f_kwargs.items())
    f_l_args = len(f_args)

    def wrapped(*args, **kwargs):
        l_args = len(args)
        l_t_args = l_args + len(kwargs)
        if l_t_args > f_l_args:
            raise TypeError(
                f"In '{callback.__name__}'() takes exactly {f_l_args} arguments ({l_t_args} given)")
        for p in kwargs:
            if not p in f_kwargs:
                raise TypeError(
                    f"{callback.__name__}() got an unexpected keyword argument '{p}'")
            if not isinstance(kwargs[p], f_kwargs[p]):
                raise TypeError(
                    f"In '{callback.__name__}'() got an unexcepected keyword argument type: '{p}' should be {f_kwargs[p].__name__}")
        for p in range(l_args):
            if not isinstance(args[p], f_args[p][1]):
                raise TypeError(
                    f"In '{callback.__name__}'() got an unexcepected positionnal argument type: '{f_args[p][0]}' should be {f_args[p][1].__name__}")

        return callback(*args, **kwargs)

    wrapped.__name__, wrapped.__doc__ = callback.__name__, callback.__doc__

    return wrapped


# EXERCICE 1


BaseUPMC = [('GARGA', 'Amel', 20231343, [12, 8, 11, 17, 9]),
            ('POLO', 'Marcello', 20342241, [9, 11, 19, 3]),
            ('AMANGEAI', 'Hildegard', 20244229, [15, 11, 7, 14, 12]),
            ('DENT', 'Arthur', 42424242, [8, 4, 9, 4, 12, 5]),
            ('ALEZE', 'Blaise', 30012024, [17, 15, 20, 14, 18, 16, 20]),
            ('D2', 'R2', 10100101, [10, 10, 10, 10, 10, 10])]


# QUESTION 1
@checkType
def note_moyenne(notes: list) -> float:
    """

    Description
    ----------
    Return the average of list by adding
    every item of list and divide the sum by the list lenght.

    Parameters
    ----------
    notes : LIST
        The liste you want to know the average.

    Returns
    -------
    FLOAT
        The average of liste.

    """
    return round(sum(notes)/(len(notes) or 1), 2)


# QUESTION 2
@checkType
def moyenne_generale(data: list) -> float:
    """

    Description
    ----------
    Get the average from all sudent from a database by adding
    every student average and divide the sum by the student number.

    Parameters
    ----------
    data : LIST
        The database where you search the average.

    Returns
    -------
    FLOAT
        The average of database.

    """
    return note_moyenne([note_moyenne(s[3]) for s in data])


# QUESTION 3
@checkType
def top_etudiant(data: list) -> tuple:
    """

    Description
    ----------
    Get the top student from a database by creating a dictionnary of
    average by student, and then return the (name : str, firstname : str)
    of the maximum average.

    Parameters
    ----------
    data : LIST
        The database where you search the top student.

    Returns
    -------
    TUPLE
        The best student name and first name.

    """
    return (lambda d: d[max(d)])({note_moyenne(s[3]): s[0:2] for s in data})


# QUESTION 4
@checkType
def recherche_moyenne(nId: int, data: list) -> float:
    """

    Description
    ----------
    Get the average of a student from a database by
    checking every student id until it found it and
    return the student average.

    Parameters
    ----------    
    nId : STRING
        The student id.

    data : LIST
        The database where you search the student average.

    Returns
    -------
    FLOAT
        The student's average.

    """
    for student in data:
        if student[2] == nId:
            return note_moyenne(student[3])


# EXERCICE 2


Dessert = {'gateau chocolat': ('chocolat', 'oeuf', 'farine', 'sucre', 'beurre'),
           'gateau yaourt': ('yaourt', 'oeuf', 'farine', 'sucre'),
           'crepes': ('oeuf', 'farine', 'lait'),
           'quatre-quarts': ('oeuf', 'farine', 'beurre', 'sucre'),
           'kouign amann': ('farine', 'beurre', 'sucre')}


# QUESTION 1
@checkType
def nb_ingredients(data: dict, nId: str) -> int:
    """

    Description
    ----------
    Get the number of ingredient needed in a recipe just with the len() function.

    Parameters
    ----------    
    data : DICTIONARY
        The database where you search the recipe.

    nId : STRING
        The recipe's name.

    Returns
    -------
    INT
        The recipe's length.

    """
    return len(data[nId])


# QUESTION 2
@checkType
def recette_avec(data: dict, nId: str) -> list:
    """

    Description
    ----------
    Get the recipes with a special ingredient.

    Parameters
    ----------    
    data : DICTIONARY
        The database where you search the recipes.

    nId : STRING
        The ingredient's name.

    Returns
    -------
    LIST
        The recipes with this ingredient.

    """
    return [recette for recette in data if nId in data[recette]]


# QUESTION 3
@checkType
def tous_ingredients(data: dict) -> list:
    """

    Description
    ----------
    Get all the ingredients used in a recipes database by
    appending it to a new list if the ingredient isn't aleready in the list.

    Parameters
    ----------    
    data : DICTIONARY
        The database where you want to know the ingredients.

    Returns
    -------
    res : LIST
        All the ingredients found.

    """
    res = []
    for r in data:
        for i in data[r]:
            if i not in res:
                res.append(i)
    return res


# QUESTION 4
@checkType
def table_ingredients(data: dict) -> dict:
    """

    Description
    ----------
    Sort the ingredients with all the recipes they're used by
    adding every recipe where the ingredient is used
    to the list of recipes used by ingredient
    in a dictionnary. 

    Parameters
    ----------    
    data : DICTIONARY
        The database where you want to know the ingredients.

    Returns
    -------
    DICTIONNARY
        The ingredients sorted.
    """
    return {i: [r for r in data if i in data[r]] for i in tous_ingredients(data)}


# QUESTION 5
@checkType
def ingredient_principal(data: dict) -> str:
    """

    Description
    ----------
    Get the most used ingredients by creating a dictionnary of
    the number of time the ingredient is use by ingredient, and then
    return the maximum used ingredient. 

    Parameters
    ----------    
    data : DICTIONARY
        The database where you want to know the ingredients.

    Returns
    -------
    STRING
        The most used ingredients.

    """
    return (lambda d: d[max(d)])({len(r): i for [i, r] in table_ingredients(data).items()})


# QUESTION 6
@checkType
def recettes_sans(data: dict, nId: str) -> dict:
    """

    Description
    ----------
    Sort a recipes database without all the recipe who use a special ingredient.

    Parameters
    ----------    
    data : DICTIONARY
        The database where you want to know the ingredients.

    nId : STRING
        The ingredients you don't want to use.

    Returns
    -------
    DICTIONARY
        The database sorted.

    """
    return {r: data[r] for r in data if not nId in data[r]}


# TESTS


if __name__ == "__main__":

    # EXERCICE 1

    print(note_moyenne([12, 8, 14, 6, 5, 15]))
    print(note_moyenne([]))

    print(moyenne_generale(BaseUPMC))

    print(top_etudiant(BaseUPMC))

    print(recherche_moyenne(20244229, BaseUPMC))
    print(recherche_moyenne(20342241, BaseUPMC))
    print(recherche_moyenne(2024129111, BaseUPMC))

    # EXERCICE 2

    print(nb_ingredients(Dessert, 'gateau chocolat'))

    print(recette_avec(Dessert, 'beurre'))

    print(tous_ingredients(Dessert))

    print(table_ingredients(Dessert))

    print(ingredient_principal(Dessert))

    print(recettes_sans(Dessert, 'farine'))
    print(recettes_sans(Dessert, 'oeuf'))
    print(recettes_sans(Dessert, 'beurre'))
