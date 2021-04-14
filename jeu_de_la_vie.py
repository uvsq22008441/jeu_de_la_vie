import tkinter as tk



#############################################
# Import des modules

import tkinter as tk


############################################
# Constantes
COUL_FOND = "blue"
LARGEUR = 600
HAUTEUR = 400

############################################
# Fonction

#############################################
# Partie principale du code

racine = tk.Tk()
racine.title("jeu de la vie")

#Création des widgets
canvas = tk.Canvas(racine, bg=COUL_FOND, width = LARGEUR, height = HAUTEUR)

# Placement des widgets
canvas.grid()

# Boucle principale
racine.mainloop()