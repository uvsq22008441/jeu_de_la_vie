import tkinter as tk



#############################################
# Import des modules

import tkinter as tk


############################################
# Constantes
COUL_FOND = "grey20"
LARGEUR = 600
HAUTEUR = 400
cote = 10
COUL_QUADR = "white"
COUL_VIVANTE = "blue"
######################################################
#Variables globales
tableau = None

############################################
# Fonction
def quadrillage():
    y = 0 
    while y <= HAUTEUR :
        canvas.create_line((0, y), (LARGEUR, y), fill = COUL_QUADR)
        y += cote
    x = 0
    while x <= LARGEUR :
        canvas.create_line(x,0, x, HAUTEUR, fill = COUL_QUADR)
        x += cote

def xy_to_cl(x, y):
#retourne la colonne et la ligne du tableau correspondant aux coordonées(x, y) du canva"
    return 0, 0


def chg_case(event): 
"modifier l'etat de la case aux coords (event.x, event.y)"
c, l = xy_to_cl(event.x, event.y)
if tableau[c][l] >= 0:
    #si case vivante
    canvas.delete(tableau[c] [l])
    tableau[c][l] = -1
else
    #si case morte
    carre = canvas.create_rectangle((0, 0), (cote, cote), fill = COUL_vivante)
    talbeau[c][l]= carre


#############################################
# Partie principale du code

racine = tk.Tk()
racine.title("jeu de la vie")

#Création des widgets
canvas = tk.Canvas(racine, bg=COUL_FOND, width = LARGEUR, height = HAUTEUR)

# Placement des widgets
canvas.grid()

quadrillage()

# Boucle principale
racine.mainloop()

#~Evenements 
canvas.bind("<Button-1>",chg_case)