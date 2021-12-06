# -*- coding: utf-8 -*-
"""
TP3 Python: dictionary, list and tuple (n_uplet)

Finished at 17:03 am 02/12/21.
By Lucas Maillet.
"""


# UTILS


from functools import wraps


def strictType(check_return=True):
    """

    Description
    -----------
    Wrap a function to overide it if the specified arguments
    passed haven't the type required.

    Parameters
    ----------
    fn : FUNCTION
        The function you want to supervise.

    check_return : BOOLEAN
        If you want to check the result type or not.

    Returns
    -------
    FUNCTION
        The new wrapped function.

    """
    def wrapper(fn):

        annotations = fn.__annotations__
        fn_ = lambda args, kwargs : fn(*args, **kwargs)

        if 'return' in annotations:
            restype = annotations.pop('return')
            if check_return:
                def fn_(args, kwargs):
                    res = fn(*args, **kwargs)
                    if not isinstance(res, restype): raise TypeError(f"{fn.__name__}() return an unexpected type, should be an instance of {restype}")
                    return res

        annotations = annotations.items()

        @wraps(fn)
        def wrapped(*args, **kwargs):
            for argid, [arg, argtype] in enumerate(annotations):
                if arg in kwargs:
                    if not isinstance(kwargs[arg], argtype):
                        raise TypeError(
                            f"{fn.__name__}() got an unexpected keyword argument type: '{arg}' should be an instance of {argtype}")
                elif argid < len(args) and not isinstance(args[argid], argtype):
                    raise TypeError(
                        f"{fn.__name__}() got an unexpected positional argument type: '{arg}' should be an instance of {argtype}")
            return fn_(args, kwargs)

        return wrapped

    return wrapper


## EXERCICE 1

# QUESTION 1
@strictType()
def note_moyenne(notes: list) -> float:
    """

    Description
    -----------
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
@strictType()
def moyenne_generale(data: list) -> float:
    """

    Description
    -----------
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
@strictType()
def top_etudiant(data: list) -> tuple:
    """

    Description
    -----------
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
@strictType(False)
def recherche_moyenne(nId: int, data: list) -> float:
    """

    Description
    -----------
    Get the average of a student from a database by
    checking every student id until it found it and
    return the student average.

    Parameters
    ----------
    nId : INT
        The student id.

    data : LIST
        The database where you search the student average.

    Returns
    -------
    FLOAT
        The student's average.

    """
    return {s[2]: note_moyenne(s[3]) for s in data}.get(nId)


## EXERCICE 2


# QUESTION 1
@strictType()
def nb_ingredients(data: dict, nId: str) -> int:
    """

    Description
    -----------
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
@strictType()
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
@strictType()
def tous_ingredients(data: dict) -> list:
    """

    Description
    -----------
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
    return list({i for r in data for i in data[r]})


# QUESTION 4
@strictType()
def table_ingredients(data: dict) -> dict:
    """

    Description
    -----------
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
@strictType()
def ingredient_principal(data: dict) -> str:
    """

    Description
    -----------
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
    return (lambda d: d[max(d)])({len(r): i for (i, r) in table_ingredients(data).items()})


# QUESTION 6
@strictType()
def recettes_sans(data: dict, nId: str) -> dict:
    """

    Description
    -----------
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


## TESTS


if __name__ == "__main__":

    # EXERCICE 1
    
    BaseUPMC = [('GARGA', 'Amel', 20231343, [12, 8, 11, 17, 9]),
                ('POLO', 'Marcello', 20342241, [9, 11, 19, 3]),
                ('AMANGEAI', 'Hildegard', 20244229, [15, 11, 7, 14, 12]),
                ('DENT', 'Arthur', 42424242, [8, 4, 9, 4, 12, 5]),
                ('ALEZE', 'Blaise', 30012024, [17, 15, 20, 14, 18, 16, 20]),
                ('D2', 'R2', 10100101, [10, 10, 10, 10, 10, 10])]

    print(note_moyenne([12, 8, 14, 6, 5, 15],))
    print(note_moyenne([]))

    print(moyenne_generale(BaseUPMC))

    print(top_etudiant(BaseUPMC))

    print(recherche_moyenne(20244229, BaseUPMC))
    print(recherche_moyenne(20342241, BaseUPMC))
    print(recherche_moyenne(2024129111, BaseUPMC))

    # EXERCICE 2

    Dessert = {'gateau chocolat': ('chocolat', 'oeuf', 'farine', 'sucre', 'beurre'),
            'gateau yaourt': ('yaourt', 'oeuf', 'farine', 'sucre'),
            'crepes': ('oeuf', 'farine', 'lait'),
            'quatre-quarts': ('oeuf', 'farine', 'beurre', 'sucre'),
            'kouign amann': ('farine', 'beurre', 'sucre')}

    print(nb_ingredients(Dessert, 'gateau chocolat'))

    print(recette_avec(Dessert, 'beurre'))

    print(tous_ingredients(Dessert))

    print(table_ingredients(Dessert))

    print(ingredient_principal(Dessert))

    print(recettes_sans(Dessert, 'farine'))
    print(recettes_sans(Dessert, 'oeuf'))
    print(recettes_sans(Dessert, 'beurre'))
