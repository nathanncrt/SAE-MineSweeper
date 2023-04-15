# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect (entier: int) -> bool:
    """
    La fonction retourne sous forme d'un booléen, si le contenu ('entier') reçu en paramètre peut représenter le contenu
    d'une cellule. Sachant que le contenu d'une cellule peut être un entier compris entre 0 et 8
    ou la valeur de la constante 'const.ID_MINE'.

    :param entier: Entier dont on veut observer sa possible représentation dans le contenu d'une cellule.
    :return: 'True' si entier représente le contenu d'une cellule, 'False' s'il ne représente pas le contenu.
    """
    represent = False

    if type(entier) != int:

        represent = False

    elif 0 <= entier <= 8 or entier == const.ID_MINE:

        represent = True

    return represent


def construireCellule(contenu: int = 0, visible: bool = False) -> dict:
    """
    La fonction retourne un dictionnaire correspondant à la cellule.

    :param contenu: Entier correspondant au contenu dont la valeur par défaut est égale à 0.
    :param visible: Booléen correspondant à la visibilité dont la valeur par défaut est égale à False.
    :return: Un dictionnaire représentant une cellule.
    """

    if isContenuCorrect(contenu) == False:

        raise ValueError('«construireCellule: le contenu valeur_du_contenu n’est pas correct.»')

    elif type(visible) != bool:

        raise TypeError('« construireCellule : le second paramètre (type_du_paramètre) n’est pas un booléen.»')

    dictionnaire = {const.CONTENU: contenu,
                    const.VISIBLE: visible,
                    const.ANNOTATION: None}

    return dictionnaire


def getContenuCellule(cellule: dict) -> int:
    """
    La fonction retourne le contenu de la cellule ('cellule') passé en paramètre sous forme d'un entier ('int').

    :param cellule: Dictionnaire représentant une cellule.
    :return: Le contenu de la cellule sous forme d'un entier ('int').
    """

    if type_cellule(cellule) == False:

        raise TypeError('« getContenuCellule : Le paramètre n’est pas une cellule.»')

    return int(cellule[const.CONTENU])


def isVisibleCellule(cellule: dict) -> bool:
    """
    La fonction retourne un booléen qui correspond à la visibilité de la cellule ('cellule') passé en paramètre.

    :param cellule: Dictionnaire représentant une cellule.
    :return: La visibilité de la cellule, 'True' si elle est visible, 'False' sinon.
    """

    if type_cellule(cellule) == False:

        raise TypeError('« isVisibleCellule : Le paramètre n’est pas une cellule. »')

    return cellule[const.VISIBLE]


def setContenuCellule(cellule: dict, contenu: int) -> None:
    """
    La fonction modifie le contenu de la cellule ('cellule') passée en paramètre
    par le contenu ('contenu') passé en paramètre.

    :param cellule: Dictionnaire représentant une cellule.
    :param contenu: Contenu de type 'int'.
    :return: Rien.
    """
    if type_cellule(cellule) == False:

        raise TypeError('« setContenuCellule : Le premier paramètre n’est pas une cellule. »')

    elif type(contenu) != int:

        raise TypeError('« setContenuCellule : Le second paramètre n’est pas un entier. »')

    if isContenuCorrect(contenu) == False:

        raise ValueError('« setContenuCellule : la valeur du contenu (valeur_passée_en_paramètre) n’est pas correcte.»')

    cellule[const.CONTENU] = contenu

    return None


def setVisibleCellule(cellule: dict, visible: bool) -> None:
    """
    La fonction modifie la visibilité de la cellule ('cellule') passée en paramètre par une nouvelle visibilité
    ('visible') passée en paramètre.

    :param cellule: Dictionnaire représentant une cellule.
    :param visible: Booléen représentant la visibilité de la cellule.
    :return: Rien.
    """

    if type_cellule(cellule) == False:

        raise TypeError('« setVisibleCellule : Le premier paramètre n’est pas une cellule. »')

    elif type(visible) != bool:

        raise TypeError('« setVisibleCellule : Le second paramètre n’est pas un booléen »')

    cellule[const.VISIBLE] = visible

    return None


def contientMineCellule (cellule: dict) -> bool:
    """
    La fonction retourne un booléen qui spécifie si la cellule
    ('cellule') passée en paramètre contient une mine ou non.

    :param cellule: Dictionnaire représentant une cellule.
    :return: 'True' si la cellule contient une mine,'False' sinon.
    """

    contient = False

    if type_cellule(cellule) == False:

        raise TypeError('« contientMineCellule : Le paramètre n’est pas une cellule. »')

    if getContenuCellule(cellule) == const.ID_MINE:

        contient = True

    return contient


def isAnnotationCorrecte (annotation: str) -> bool:
    """
    La fonction retourne un booléen suivant si l'annotation est correcte ou non.

    :param annotation: Booléen qui représente l'annotation.
    :return: 'True' si l'annotation est correct, 'False' sinon.
    """

    return annotation == None or annotation == const.DOUTE or annotation == const.FLAG


def getAnnotationCellule (cellule: dict) -> str:
    """
    La fonction retourne l'annotation contenue dans la cellule ('cellule') passée en paramètre.

    :param cellule: Dictionnaire représentant une cellule.
    :return: L'annotation contenue dans la cellule.
    """

    if type_cellule(cellule) == False:

        raise TypeError('« getAnnotationCellule : le paramètre valeur_du paramètre n’est pas une cellule »')

    if len(cellule) != 3:

        return None

    return cellule[const.ANNOTATION]


def changeAnnotationCellule(cellule: dict) -> None:
    """
    La fonction modifie l'annotation de la cellule ('cellule') passée en paramètre.

    :param cellule: Dictionnaire représentant une cellule.
    :return: Rien.
    """
    if type_cellule(cellule) == False:

        raise TypeError(' « changeAnnotationCellule : le paramètre n’est pas une cellule »')

    annotation = getAnnotationCellule(cellule)

    if isVisibleCellule(cellule) == False:

        if annotation == None :

            cellule[const.ANNOTATION] = const.FLAG

        elif annotation == const.FLAG:

            cellule[const.ANNOTATION] = const.DOUTE

        elif annotation == const.DOUTE:

            cellule[const.ANNOTATION] = None

    return None


def reinitialiserCellule (cellule: dict) -> None:
    """
    La fonction réinitialise tous les éléments de la cellule ('cellule') passée en paramètre pour une nouvelle partie.
    La cellule ne sera pas visible, contiendra 0 et ne possèdera aucune annotation.

    :param cellule: Dictionnaire représentant une cellule.
    :return: Rien.
    """
    cellule[const.CONTENU] = 0

    cellule[const.VISIBLE] = False

    cellule[const.ANNOTATION] = None

    return None















