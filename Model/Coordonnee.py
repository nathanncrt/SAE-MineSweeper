# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0


def construireCoordonnee (nl: int, nc: int) -> tuple:
    """
    La fonction affiche une coordonnée sous forme d'un tuple (num_ligne, num_colonne).

    :param nl :Numéro de la ligne.
    :param nc: Numéro de la colonne.
    :return: Un tuple (num_ligne, num_colonne).
    """

    if type(nl) != int or type(nc) != int:

        raise TypeError('« construireCoordonnee : Le numéro de ligne type_du_premier_paramètre ou le numéro de colonne '
                        'type_du_second_paramètre ne sont pas des entiers »')

    if nl < 0 and nc < 0:

        raise ValueError('« construireCoordonnee : Le numéro de ligne (valeur_de_la_ligne) '
                         'ou de colonne (valeur_de_la_colonne) ne sont pas positifs »')

    coord = (nl, nc)

    return coord


def getLigneCoordonnee (coord: tuple) -> int:
    """
    La fonction affiche le numéro de la ligne contenu dans la coordonnée passée en paramètre.

    :param coord: Coordonnée sous forme d'un tuple.
    :return: Numéro de la ligne.
    """

    if type(coord) != tuple:

        raise TypeError('« getLigneCoordonnee : Le paramètre n’est pas une coordonnée »')

    return coord[0]


def getColonneCoordonnee (coord: tuple) -> int:
    """
    La fonction affiche le numéro de la colonne contenu dans la coordonnée passée en paramètre.

    :param coord: Coordonnée sous forme d'un tuple.
    :return: Numéro de la colonne.
    """
    if type_coordonnee(coord) == False:

        raise TypeError('« getColonneCoordonnee : Le paramètre n’est pas une coordonnée »')

    return coord[1]





