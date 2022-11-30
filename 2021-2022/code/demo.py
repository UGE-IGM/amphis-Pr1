import fltk

hauteur_fenetre = 400
largeur_fenetre = 600

def message(texte):
    fltk.efface('message')
    x, y = largeur_fenetre/2, hauteur_fenetre/2
    fltk.texte(x, y, texte, tag='message', ancrage='center')
    
def animation(pas, x, y):
    rayon = 10 + abs(pas % 20 - 10)
    fltk.efface('animation')
    fltk.cercle(x, y, rayon, remplissage='lightblue', tag='animation')

if __name__ == '__main__':
    fltk.cree_fenetre(largeur_fenetre, hauteur_fenetre)
    cpt = 1
    while True:
        # /!\ mise à jour de l'affichage et des événements
        fltk.mise_a_jour()
        
        # animation
        x, y = fltk.abscisse_souris(), fltk.ordonnee_souris()
        animation(cpt, x, y)
        cpt += 1
        
        # gestion des événements
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        if tev == 'ClicGauche':
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
            message(f'Clic gauche en ({x}, {y})')
        elif tev == 'Touche':
            t = fltk.touche(ev)
            message(f'Appui sur la touche {t} !')
        elif tev == 'Quitte':
            break
    fltk.ferme_fenetre()