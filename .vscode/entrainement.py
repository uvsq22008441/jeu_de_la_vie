
#Import des modules
import tkinter as tk

racine = tk.Tk()


#constantes
HAUTEUR = 500
LONGUEUR = 500
cote = 50
pause = False

#Fonctions
def bouton_pause() :
    global pause
    if not pause :
        bouton.config(bouton, text = "restart")
        pause = True
    else :
        bouton.config(bouton, text = "pause")
        pause = False


def est_dans_carre (x,y):
     
    hgauche = 250-cote//2
    bdroite = 250+cote//2
    return hgauche <= x <= bdroite and hgauche <= y<= bdroite


def change_taille(event) :
    global cote
    if not pause :
        if est_dans_carre(event.x, event.y) and cote>= 20 : 
            cote -=10
            canvas.coords(carre, 250-cote//2,250-cote//2, 250+cote//2, 250+cote//2 )
        elif not est_dans_carre(event.x, event.y) and cote <= 100:
                cote +=10
                canvas.coords(carre, 250-cote//2,250-cote//2, 250+cote//2, 250+cote//2 )


#Programme principal








#Création des widgets
canvas = tk.Canvas(racine, bg = "black", width = LONGUEUR, height = HAUTEUR)
carre = canvas.create_rectangle(250-cote//2,250-cote//2, 250+cote//2, 250+cote//2,fill = "red")
bouton = tk.Button(racine, text = "pause", command = bouton_pause)
canvas.bind("<Button-1>", change_taille)
 
#Positionnement Widgets
canvas.grid(row = 1, column = 2)
bouton.grid (row=2, column = 2)








#Boucle principal

racine = tk.Tk()
racine.title("Exercice 1")

racine.mainloop()