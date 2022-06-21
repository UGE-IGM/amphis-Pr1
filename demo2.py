import fltk

hauteur_fenetre = 400
largeur_fenetre = 600
nb_lignes = 8
nb_colonnes = 12
hauteur_case = hauteur_fenetre / nb_lignes
largeur_case = largeur_fenetre / nb_colonnes


def message(texte):
    fltk.efface('message')
    x, y = largeur_fenetre/2, hauteur_fenetre/2
    fltk.texte(x, y, texte, tag='message', ancrage='center')

def tracer_grille():
    for i in range(nb_lignes-1):
        y = hauteur_case * i
        fltk.ligne(0, y, largeur_fenetre, y)
    for j in range(nb_colonnes-1):
        x = largeur_case * j
        fltk.ligne(x, 0, x, hauteur_fenetre)

def position_vers_case(x, y):
    return y // hauteur_case, x // largeur_case
    
if __name__ == '__main__':
    fltk.cree_fenetre(largeur_fenetre, hauteur_fenetre)
    tracer_grille()
    while True:
        # /!\ mise à jour de l'affichage et des événements
        fltk.mise_a_jour()
        
        # gestion des événements
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        if tev == 'ClicGauche':
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
            print(position_vers_case(x, y)
        elif tev == 'Quitte':
            break
    fltk.ferme_fenetre()