# -*- coding: utf-8 -*-
"""
Mini-projet Jeu du pendu
Module dessin_pendu

@author: Lycee
"""


from os import get_terminal_size, system, name


SH_WIDTH, SH_HEIGTH = get_terminal_size()
CLEAR = (lambda: system('cls')) if name == 'nt' else (lambda: system('clear'))


class Frame:
    """

    Description
    -----------
    Use to display content in shell.

    """

    def __init__(self, width: int = SH_WIDTH, heigth: int = SH_HEIGTH):
        """

        Description
        -----------
        Create an representation of viewport in shell. 

        Parameters
        ----------
        width : TYPE INT
            DESCRIPTION : Frame's width.

        height : TYPE INT
            DESCRIPTION : Frame's height.

        """
        self.width = width
        self.heigth = heigth
        self.clear = CLEAR

    def __call__(self, *content: str) -> str:
        """

        Description
        -----------
        Update the viewport in shell.

        Parameters
        ----------
        *content : TYPE STRING 
            DESCRIPTION : The text to show.

        """
        self.clear()
        print(self.center_y('\n\n'.join(self.center_x(line)
              for line in content)))

    def center_x(self, text: str) -> str:
        """

        Description
        -----------
        Center a text horizontaly.

        Parameters
        ----------
        text : TYPE STRING 
            DESCRIPTION : The word to center.

        Returns
        -------
        TYPE STRING 
            DESCRIPTION : The word centered.

        """
        margin = ' '*((self.width - len(text)) // 2)
        return f"{margin}{text}{margin}"

    def center_y(self, text: str) -> str:
        """

        Description
        -----------
        Center a text verticaly.

        Parameters
        ----------
        text : TYPE STRING 
            DESCRIPTION : The word to center.

        Returns
        -------
        TYPE STRING 
            DESCRIPTION : The word centered.

        """
        margin = '\n'*((self.heigth - text.count('\n')) // 2)
        return f"{margin}{text}{margin}"

    def center_x_block(self, content: str, offset: int) -> str:
        """

        Description
        -----------
        Center a block of text horizontaly.

        Parameters
        ----------
        content : TYPE STRING 
            DESCRIPTION : The block to center.

        Returns
        -------
        TYPE STRING 
            DESCRIPTION : The block centered.

        """
        margin = " "*(self.width//2 - offset)
        return '\n'.join(f"{margin}{line}" for line in content.split('\n'))


def dessin_pendu(index):
    """
    Les différents dessins du pendu à afficher au cours de la partie sont
    stockés sous la forme d'une chaine de caractères dans une liste 

    Parameters
    ----------
    index : TYPE INTEGER
        DESCRIPTION : indice du dessin à afficher en console

    Returns
    -------
    TYPE STRING
        DESCRIPTION : chaine de caractères représentant le dessin à afficher

    """

    tab = [
        """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
    ]
    return tab[index]


if __name__ == '__main__':
    for i in range(7):
        print(dessin_pendu(i))
