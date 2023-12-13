import random

# Décommenter pour fixer l'aléatoire (qui n'est donc plus aléatoire)
# random.seed(10)

# Renvoie une valeur différente (plus ou moins) à chaque fois,
# sauf si on a fixé l'aléatoire
print(random.randint(0,100))


# random.seed(N) permet de faire des doctests,
# si on fixe N

def liste_aleatoire(longueur, mini, maxi):
    """
    Renvoie une liste aléatoire de longueur donnée,
    constituée d'entiers aléatoires entre mini et maxi
    
    Paramètres :
    - longueur (int) : la longueur de la liste
    - mini (int) : l'entier minimum (inclus)
    - maxi (int) : l'entier maximum (inclus)
    
    Retour (int list) : la liste d'entiers aléatoires
    
    Exemple :
    >>> random.seed(0)
    >>> liste_aleatoire(5,0,10)
    [6, 6, 0, 4, 8]
    """
    liste = []
    for i in range(longueur):
        liste.append(random.randint(mini, maxi))
    return liste


if __name__ == "__main__":
    import doctest
    doctest.testmod()
