# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True


def construireGrilleDemineur (nl: int, nc: int) -> list:
    """
    La fonction crée une grille avec des cellules (une cellule = nl et nc) qui sont passés
    en paramètre.

    :param nl: Ligne(s) souhaité(s) pour la grille.
    :param nc: Colonne(s) souhaité(s) pour la grille.
    :return: Une grille.
    """

    if type(nl) != int or type(nc) != int:

        raise TypeError('« construireGrilleDemineur : Le nombre de lignes (type_du_premier_paramètre) ou de colonnes '
                        '(type_du_second_paramètre) n’est pas un entier. »')

    if nl <= 0 or nc <= 0:

        raise ValueError(' « construireGrilleDemineur : Le nombre de lignes (valeur_du_premier_paramètre)'
                         ' ou de colonnes (valeur_du_second_paramètre) est négatif ou nul. »')

    grille = []                                    # On initie la grille vide

    for i in range(nl):

        ligne = []                                # On détermine la ligne vide

        for j in range(nc):

            ligne.append(construireCellule())   # On ajoute les colonnes à la ligne

        grille.append(ligne)                        # On ajoute les lignes à notre grille

    return grille


def getNbLignesGrilleDemineur(grille: list) -> int:
    """
    La fonction affiche le nombre de lignes présent dans la grille ('grille') passée en paramètre.

    :param grille: Liste de listes représentant une grille.
    :return: Nombre de lignes présent dans la grille.
    """

    if type_grille_demineur(grille) == False:

        raise TypeError('« getNbLignesGrilleDemineur : Le paramètre n’est pas une grille »')

    return len(grille)
# len (grille) renvoie le nombre de ligne Ex: grille = [[1,2,3],[3,2,1],[4,5,6]]
# len (grille) va renvoyer 3


def getNbColonnesGrilleDemineur(grille: list) -> int:
    """
    La fonction affiche le nombre de colonnes présent dans la grille ('grille') passée en paramètre.

    :param grille: Liste de listes représentant une grille.
    :return: Nombre de colonnes présent dans la grille.
    """

    if type_grille_demineur(grille) == False:

        raise TypeError('« getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille »')

    return len(grille[0])
    # len(grille[0]) va renvoyer le nombre de cellules contenu
    # Dans la premiere ligne donc le nombre de colonnes


def isCoordonneeCorrecte (grille: list, coord: tuple) -> bool:
    """
    La fonction vérifie si la coordonnée ('coord') passée en paramètre est présente
    dans la grille ('grille') passée en paramètre.

    :param grille: Liste de listes représentant une grille.
    :param coord: Tuple représentant la coordonnée d'une cellule sous forme (num_ligne, num_colonne).
    :return: 'True' si la coordonnée est présente dans la grille, 'False' sinon.
    """

    if type_grille_demineur(grille) == False or type_coordonnee(coord) == False:

        raise TypeError('« isCoordonneeCorrecte : un des paramètres n’est pas du bon type. »')

    contenue = False

    l, c = coord                                    # On décompose le tuple coord en 2 variables (l) et (c)

    nl, nc = len(grille), len(grille[0])            # On récupère le nombre de lignes et de colonnes de grille

    if 0 <= l < nl and 0 <= c < nc:                # On vérifie si 'l' est compris entre 0 et nl et si 'c' entre 0 et nc

        contenue = True

    return contenue


def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    """
    La fonction retourne la cellule se trouvant à la coordonnée ('coord') passée en paramètre dans la grille ('grille')
    passée en paramètre.

    :param grille: Liste de listes représentant une grille.
    :param coord: Tuple représentant la coordonnée d'une cellule sous forme (num_ligne, num_colonne).
    :return: Cellule se trouvant à coordonnée.
    """

    if type_grille_demineur(grille) == False or type_coordonnee(coord) == False:

        raise TypeError('« getCelluleGrilleDemineur : un des paramètres n’est pas du bon type. »')

    if isCoordonneeCorrecte(grille, coord) == False:

        raise IndexError('« getCelluleGrilleDemineur : coordonnée non contenue dans la grille. »')

    return grille[coord[0]][coord[1]]
    # On retourne la cellule se trouvant à la cordonnée passée en paramètre dans la
    # grille passée en paramètre


def getContenuGrilleDemineur (grille: list, coord: tuple) -> int:
    """
    La fonction retourne le contenu de la cellule se trouvant à la coordonnée ('coord') passée en paramètre
    dans la grille ('grille') passée en paramètre.

    :param grille: Liste de listes représentant une grille.
    :param coord: Tuple représentant la coordonnée d'une cellule sous forme (num_ligne, num_colonne).
    :return: Contenu de la cellule à coordonnée.
    """

    return getContenuCellule(getCelluleGrilleDemineur(grille, coord))
    # On retourne le contenu de la cellule se trouvant à la cordonnée passée en paramètre dans la grille passée en
    # paramètre


def setContenuGrilleDemineur(grille: list, coord: tuple, contenu: int) -> None:
    """
    La fonction modifie le contenu de la cellule se trouvant à la coordonnée ('coord') passée en
    paramètre dans la grille ('grille') avec le nouveau contenu ('contenu').

    :param grille: Liste de listes représentant une grille.
    :param coord: Tuple représentant la coordonnée d'une cellule sous forme (num_ligne, num_colonne).
    :param contenu: Contenu de la cellule de type ('int')
    :return: Rien.
    """

    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)
    # On modifie le contenu de la cellule se trouvant à la cordonnée passée en paramètre dans la grille passée en
    # paramètre avec le nouveau contenu
    return None


def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    La fonction détermine si la cellule se trouvant à la coordonnée ('coord') passée en paramètre dans
    la grille ('grille') passée en paramètre est visible.

    :param grille: Liste de listes représentant une grille.
    :param coord: Tuple représentant la coordonnée d'une cellule sous forme (num_ligne, num_colonne).
    :return: 'True' si la cellule est visible, 'False' sinon.
    """
    visible = False

    if isVisibleCellule(getCelluleGrilleDemineur(grille, coord)):

        visible = True

    return visible


def setVisibleGrilleDemineur (grille: list, coord: tuple, visible: bool) -> None:
    """
     La fonction modifie la visibilité de la cellule se trouvant à la coordonnée ('coord') passée en
    paramètre dans la grille ('grille') avec la nouvelle visibilité ('visible').

    :param grille: Liste de listes représentant une grille.
    :param coord: Tuple représentant la coordonnée d'une cellule sous forme (num_ligne, num_colonne).
    :param visible: Booléen représentant si la cellule est visible par le joueur ou non.
    :return: Rien.
    """
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visible)

    return None


def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    La fonction détermine si la cellule qui se trouve à la coordonnée ('coord') passée en paramètre
    dans la grille ('grille') contient une mine.

    :param grille: Liste de listes représentant une grille.
    :param coord: Tuple représentant la coordonnée d'une cellule sous forme (num_ligne, num_colonne).
    :return: 'True' si la cellule contient une mine, 'False' sinon.
    """
    contient = False

    if contientMineCellule(getCelluleGrilleDemineur(grille, coord)):

        contient = True

    return contient


def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    """
    La fonction affiche une liste des coordonnées des cellules voisines de la cellule ('coord')
    qui a été passée en paramètre dans la grille ('grille').

    :param grille: Liste de listes représentant une grille.
    :param coord: Tuple représentant la coordonnée d'une cellule sous forme (num_ligne, num_colonne).
    :return: Une liste des coordonnées des cellules voisines.
    """
    if type_grille_demineur(grille) == False or type_coordonnee(coord) == False:

        raise TypeError('« getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type. »')

    if isCoordonneeCorrecte(grille, coord) == False:

        raise IndexError('« getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille. »')

    (ligne, colonne) = coord    # La ligne représente la première valeur de la coordonnée, la colonne la deuxième

    coord_voisines = []         # On initie une liste vide dans laquelle seront stockées les coordonnées des voisines

    for x in [-1, 0, 1]:

        for y in [-1, 0, 1]:

            if x != 0 or y != 0:

                voisin_x = ligne + x
                voisin_y = colonne + y

                if 0 <= voisin_x < len(grille) and 0 <= voisin_y < len(grille[0]):

                    coord_voisines.append((voisin_x, voisin_y))

    return coord_voisines


def  placerMinesGrilleDemineur(grille: list, nb: int, coord: tuple) -> None:
    """
    La fonction place exactement un nombre ('nb') de mines passées en paramètre dans ('nb')
    cellules de la grille ('grille') passée en paramètre en évitant la coordonnée ('coord') passée en paramètre.

    :param grille: Liste de listes représentant une grille.
    :param nb: Nombre de mines à placer sur la grille.
    :param coord: Coordonnée de la cellule qui ne doit pas contenir de mine (Première cellule découverte par le joueur).
    :return: Rien.
    """
    if isCoordonneeCorrecte(grille, coord) == False:

        raise IndexError('« placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille. »')

    if type_grille_demineur(grille) == False:

        raise TypeError('placerMinesGrilleDemineur : la grille n est pas du bon type')

    x = getNbLignesGrilleDemineur(grille)
    y = getNbColonnesGrilleDemineur(grille)

    if nb < 0 or nb >= (x * y):             # Si le nb de mines est négatif ou dépasse le nombre total de casses
        raise ValueError('« placerMinesGrilleDemineur : Nombre de bombes à placer incorrect »')

    while nb > 0:
        coord_mine = (randint(0, x), randint(0, y))                 # On choisit une coordonnée aléatoire

# Si 'coord' est dans la cellule et que si le contenu de la cellule ne contient pas de mine

# Et que la coordonnée choisit n'est pas égale à 'coord'

# Sachant que 'coord' est la première casse découverte pas le joueur.

        if isCoordonneeCorrecte(grille, coord_mine) == True and getContenuGrilleDemineur(grille, coord_mine) != const.ID_MINE and coord_mine != coord:

            # On modifie le contenu de la cellule par la constante ID_MINE

            setContenuGrilleDemineur(grille, coord_mine, const.ID_MINE)

        else:

            nb += 1

        nb -= 1    # Si toute la cellule reçoit une mine nb diminue de 1.
    compterMinesVoisinesGrilleDemineur(grille)

    return None


def compterMinesVoisinesGrilleDemineur (grille: list) -> None:
    """
    La fonction compte, pour chaque case ne contenant pas de mine, le nombre de mines voisines de cette case.
    Puis va affecter ce nombre au contenu de la case.

    :param grille: Liste de listes représentant une grille
    :return: Rien.
    """

    for x in range(len(grille)):

        for y in range(len(grille[1])):

            coord = (x, y)

            if getContenuGrilleDemineur(grille, coord) != const.ID_MINE:

                mines_voisines = 0

                voisin = getCoordonneeVoisinsGrilleDemineur(grille, coord)      # Renvoi liste de coord des cellules voisines

                for i in voisin:                                    # Pour chaque voisin(s)

                    if getContenuGrilleDemineur(grille, i) == const.ID_MINE:            # Si le contenu du voisin contient une mine

                        mines_voisines += 1                                             # On ajoute

                setContenuGrilleDemineur(grille, coord, mines_voisines)             # Change le contenu de la cellule
    return None


def getNbMinesGrilleDemineur(grille: list) -> int:
    """
    La fonction retourne le nombre de mines présente dans la grille ('grille') passée en paramètre.

    :param grille: Liste de listes représentant une grille.
    :return: Nombre de mines présente sur la grille sous forme ('int').
    """
    if type_grille_demineur(grille) == False:

        raise ValueError('« getNbMinesGrilleDemineur : le paramètre n’est pas une grille. »')

    nombre_mines = 0

    for x in range(len(grille)):

        for y in range(len(grille[1])):

            coord = (x, y)

            if getContenuGrilleDemineur(grille, coord) == const.ID_MINE:

                nombre_mines += 1

    return nombre_mines


def getAnnotationGrilleDemineur(grille: list, coord: tuple):
    """
    La fonction retourne l'annotation correspondant à la cellule aux coordonnées ('coord') passez en paramètre
    dans la grille ('grille').

    :param grille: Liste de listes représentant une grille.
    :param coord: Tuple représentant la coordonnée d'une cellule sous forme (num_ligne, num_colonne).
    :return: Retourne l'annotation de la cellule.
    """

    return getAnnotationCellule(getCelluleGrilleDemineur(grille, coord))


def getMinesRestantesGrilleDemineur(grille: list) -> int:
    """
    La fonction retourne le nombre total de mines restantes dans la grille ('grille') passée en paramètre.

    :param grille: Liste de listes représentant une grille.
    :return: Nombre de mines restantes sous forme d'un entier ('int').
    """
    drapeau = 0

    for x in range(len(grille)):

        for y in range(len(grille[1])):

            coord = (x, y)

            if getAnnotationGrilleDemineur(grille, coord) == const.FLAG:   # Si la cellule contient un drapeau

                drapeau += 1

    return getNbMinesGrilleDemineur(grille)-drapeau

    # On soustrait le nombre de mines restante(s) par le nombre de drapeau(x).


def gagneGrilleDemineur(grille: list) -> bool:
    """
    La fonction retourne si la partie est gagnée.

    :param grille: Liste de listes représentant une grille.
    :return: 'True' si la partie est gagnée, 'False' si elle n'est pas encore gagnée.
    """
    gagne = True
    for x in range(len(grille)):

        for y in range(len(grille[x])):

            if contientMineCellule(grille[x][y]) and getAnnotationGrilleDemineur(grille, (x, y)) != const.FLAG:

                gagne = False

            if contientMineCellule(grille[x][y]) == False and isVisibleCellule(grille[x][y]) == False:

                gagne = False

            elif contientMineCellule(grille[x][y]) and isVisibleCellule(grille[x][y]):

                gagne = False

    return gagne


def perduGrilleDemineur(grille: list) -> bool:
    """
    La fonction retourne si la partie est perdue.

    :param grille: Liste de listes représentant une grille.
    :return: 'True' si la partie est perdue, 'False' si elle n'est pas encore perdue.
    """
    perdu = False

    for x in range(len(grille)):

        for y in range(len(grille[0])):

            coord = (x, y)

            if (isVisibleCellule(getCelluleGrilleDemineur(grille, coord))) == True and getContenuGrilleDemineur(grille, coord) == const.ID_MINE:

                perdu = True

    return perdu

def reinitialiserGrilleDemineur(grille: list) -> None:
    """
    La fonction réinitialise toutes les cellules de la grille ('grille') passée en paramètre.

    :param grille: Liste de listes représentant une grille.
    :return: Rien.
    """

    for x in range(len(grille)):

        for y in range(len(grille[0])):

            reinitialiserCellule(grille[x][y])              # On crée une cellule avec grille[x][y]

    return None


def decouvrirGrilleDemineur(grille: list, coord: tuple) -> set:
    """
    La fonction découvre (rend visible) la cellule correspondant à la coordonnée ('coord') passée en paramètre.
    Si cette cellule ne possède aucun voisin possédant une mine, la fonction va alors découvrir les cellules dans le
    voisinage de cette dernière. Si une des cellules du voisinage ne contient aucun voisin qui possède une mine, on
    relancera ce processus à nouveau.

    :param grille: Liste de listes représentant une grille.
    :param coord: Tuple représentant la coordonnée d'une cellule sous forme (num_ligne, num_colonne)
    :return: Retourne les coordonnées découvertes sous forme d'ensemble ('set').
    """

    coord_decouverte = []
    # On ajoute les coordonnées de départ à la liste des coordonnées découvertes
    coord_decouverte.append(coord)

    cellule_explorer = []
    # On ajoute les coordonnées de départ à la liste des cellules à explorer

    cellule_explorer.append(coord)

    i = 0
    # Tant qu'il y a encore des cellules à explorer

    while len(cellule_explorer) > i:
        # On vérifie si cellule ne contient aucun voisin
        if getContenuCellule(getCelluleGrilleDemineur(grille, cellule_explorer[i])) == 0:
            # On obtient les coordonnées des voisins de la cellule

            cellule_voisine = getCoordonneeVoisinsGrilleDemineur(grille, cellule_explorer[i])
            # Boucle pour les voisins

            for z in cellule_voisine:
# On ajoute les coordonnées du voisin dans la liste des coordonnées découvertes si elles n'ont pas été découvertes
                if not(z in coord_decouverte):

                    coord_decouverte.append(z)
                # Si le contenu du voisin est 0 et n'a pas encore été exploré et n'est pas visible

                if getContenuCellule(getCelluleGrilleDemineur(grille, z)) == 0 and not (z in cellule_explorer) and isVisibleCellule(getCelluleGrilleDemineur(grille, z)) == False:
                    cellule_explorer.append(z)
        i += 1

    # Retourne les coordonnées découvertes sous forme d'ensemble
    return set(coord_decouverte)


def simplifierGrilleDemineur (grille: list, coord: tuple) -> list:
    """
    La fonction vérifie déjà que la case cliqué est bien visible. Si ce n’est pas le cas, elle ne fait rien
    (elle retourne un ensemble vide). Dans le cas où la case est visible, la fonction compte le nombre de drapeaux
    dans le voisinage de cette case. Si ce nombre correspond exactement au contenu de la case, la fonction rend
    toutes les autres cases voisines visibles. On relance alors le procédé sur les cases rendues visibles.

    :param grille: Liste de listes représentant une grille.
    :param coord: Tuple représentant la coordonnée d'une cellule sous forme (num_ligne, num_colonne)
    :return: Retourne l'ensemble des coordonnées cases rendues visibles pour que l’application puisse mettre à
    jour l’interface graphique. Mais elle peut ne rien renvoyer si la case cliqué n'est pas visible.
    """
    liste = []

    voisin = getCoordonneeVoisinsGrilleDemineur(grille, coord)


    compteur = 0

    for i in range(len(voisin)):

        if isVisibleGrilleDemineur(grille, voisin[i]) == False and getAnnotationGrilleDemineur(grille, voisin[i]) != const.FLAG and contientMineGrilleDemineur(grille, voisin[i]) == False:

            liste.append(voisin[i])

        if getAnnotationGrilleDemineur(grille, voisin[i]) == const.FLAG:

            compteur += 1

    if compteur != getContenuGrilleDemineur(grille, coord):

        res = []

    return liste


def ajouterFlagsGrilleDemineur (grille: list, coord: tuple) -> list:
    """
    Si le contenu de la cellule correspond au nombre de cases non découvertes dans le voisinage, alors la
    fonction place un drapeau sur celles qui n’en n’ont pas.

    :param grille: Liste de listes représentant une grille.
    :param coord: Tuple représentant la coordonnée d'une cellule sous forme (num_ligne, num_colonne)
    :return: Retourne l'ensemble des coordonnées des cellules sur lesquelles elle a placé un drapeau afin que
    l'interface graphique puisse les mettre à jour.
    """

    coord_drapeau = []

    voisin = getCoordonneeVoisinsGrilleDemineur(grille, coord)

    compteur = 0

    for i in range(len(voisin)):

        if isVisibleGrilleDemineur(grille, voisin[i]) == False:

            coord_drapeau.append(voisin[i])

            compteur += 1


        if compteur != getContenuGrilleDemineur(grille, coord):

            coord_drapeau = []

    return coord_drapeau




def simplifierToutGrilleDemineur (grille: int) -> tuple:
    """
    La fonction parcourt toutes les cellules de la grille ('grille') passée en paramètre et tente de
    les simplifier en appelant 'simplifierGrilleDemineur' et 'ajouterFlagsGrilleDemineur'.
    Tant qu’il y a des modifications, la fonction reparcourt les cellules pour trouver des simplifications.

     :param grille: Liste de listes représentant une grille.
     :return: Retourne un tuple contenant en premier l’ensemble des coordonnées des cellules rendues visible
     et en second l’ensemble des coordonnées des cellules sur lesquelles a été ajouté un drapeau.
    """

    cellule_visible = set()

    cellule_drapeau = set()

    for x in range(len(grille)):

        for y in range(len(grille[x])):

            coord = (x, y)

            if simplifierGrilleDemineur(grille, coord):

                cellule_visible.add(coord)

            if ajouterFlagsGrilleDemineur(grille, coord):

                cellule_drapeau.add(coord)



    return (cellule_visible, cellule_drapeau)

# Problème avec simplifierToutGrilleDemineur, le scroll vers le bas fais apparaitre toutes les cellules, dont les mines.
# Mais aucun drapeau ne se place à la place des mines découvertes ...


