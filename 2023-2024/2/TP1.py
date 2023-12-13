def affiche_liste(liste):
    """
    Affiche la liste donnée en argument.
    Paramètres :
    liste (list) : la liste
    """
    for i in range(len(liste)):
        print(liste[i])
        
def affiche_iterable(iterable):
    """
    Affiche l'itérable donné en argument.
    Paramètres :
    iterable (iterable) : l'itérable
    """
    for element in iterable:
        print(element)
        
def appartient(x, elems):
    """
    Teste si x appartient à elems
    Paramètres :
    - x : l'élément à rechercher
    - elems (iterable) : l'itérable contenant les éléments
    Valeur de retour (bool) : True si x appartient à elems,
                              False sinon.
    """
    for elt in elems:
        if elt == x:
            return True
    return False

def premier_indice(x, elems):
    """
    Renvoie le premier indice où x apparaît dans elems, et -1 sinon.
    Paramètres :
    - x : l'élément à rechercher
    - elems (iterable) : l'itérable contenant les éléments
    Valeur de retour (int) :
    i si elems[i] = x et si x n'apparaît pas avant
    -1 si x n'apparaît pas dans elems.
    """
    for i in range(len(elems)):
        if elems[i] == x:
            return i
    return -1

def premier_indice_enum(x, elems):
    """
    Renvoie le premier indice où x apparaît dans elems, et -1 sinon.
    Utilise `enumerate`.
    Paramètres :
    - x : l'élément à rechercher
    - elems (iterable) : l'itérable contenant les éléments
    Valeur de retour (int) :
    i si elems[i] = x et si x n'apparaît pas avant
    -1 si x n'apparaît pas dans elems.
    """
    for i, elt in enumerate(elems):
        if elt == x:
            return i
    return -1
