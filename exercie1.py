#Votre fenêtre graphique doit contenir un canevas de couleur de fond noire et de taille 500x500 ainsi qu’un bouton avec le texte “Recommencer” placé en dessous du canevas.
#Dessiner un rectangle rempli de rouge sur le canvas (la taille et la position sont au choix).
#A chaque clic de l’utilisateur dans le rectangle, le rectangle devient bleu, puis rouge alternativement.
#Si l’utilisateur clique en dehors du rectangle alors le rectangle est figé: c’est-à-dire que si on reclique à l’intérieur de celui-ci, rien ne se passe.
#A tout moment, si l’utilisateur clique sur le bouton “recommencer”, alors on recommence du début avec le rectangle rempli de rouge dessiné.


#############################################
# Import des modules

import tkinter as tk


############################################
# Constantes
COUL_FOND = "black"
LARGEUR = 500
HAUTEUR = 500


############################################
# Fonction

#############################################
# Partie principale du code

racine = tk.Tk()
racine.title("Exercice1")

def change_coul(event):
    button_rectangle.configure(bg = "blue")





#Création des widgets
canvas = tk.Canvas(racine, bg=COUL_FOND, width = LARGEUR, height = HAUTEUR)
button_carre = tk.Button(text="Recommencer", borderwidth ="2m", fg="blue")
canvas.create_rectangle(150, 200, 350, 300, fill="blue", command = change_coul)

# Placement des widgets
button_carre.grid( row = 2, column =1)
canvas.grid(row= 1, column= 1)


# Boucle principale
racine.mainloop()
