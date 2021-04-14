#Votre fenêtre graphique doit contenir un canevas de couleur de fond blanche et de taille 500x500 ainsi qu’un bouton avec le texte “Pause” placé en dessous du canevas.
#Attendre deux clics de l’utilisateur.
#Afficher une ligne bleue entre les deux points cliqués.
#Attendre de nouveau deux clics.
#Afficher une ligne rouge entre les deux nouveaux points cliqués.
#Au clic suivant, les deux lignes sont effacées et on recommence (c’est-à-dire on attend de nouveau 2 clics comme au point 2.)
#Si l’utilisateur clique sur le bouton “Pause”, alors le programme est suspendu (c’est-à-dire que cliquer ne modifie pas la fenêtre graphique) et le nom du bouton devient “Restart”.
#Si l’utilisateur clique de nouveau sur le bouton “Restart” alors que le programme était suspendu, alors le programme reprend là où il en était, et le nom du bouton redevient “Pause”.



import tkinter as tk

pause = False
cote = 50

def bouton_pause() :
    global pause
    if not pause:
        bouton.config(text ="restart")
        pause = True
    else :
        bouton.config(text = "pause")
        pause = False
    


def est_dans_le_carre(x, y) :
    "la focntion retourn True si le point de coordonées (x, y) est dans le carré et False sinon"
    inf = 250-cote//2
    sup = 250+cote//2
    return inf <= x <= sup and inf <= y <= sup


def change_taille(event) : 
    global cote
    if not pause :
        if est_dans_le_carre(event.x, event.y) and cote >= 20 :
             cote -= 10
             canvas.coords(carre, 250-cote//2, 250-cote//2, 250+cote//2, 250+cote//2)
        elif not est_dans_le_carre(event.x, event.y) and cote <=100 :
            cote +=10
            canvas.coords(carre, 250-cote//2, 250-cote//2, 250+cote//2, 250+cote//2)


 


racine = tk.Tk()
canvas =tk.Canvas(racine, bg = "white", width = 500, height = 500)
canvas.grid(row =0, column =0)

bouton =tk.Button(racine, text = "pause", command= bouton_pause)
bouton.grid(rows = 1)

canvas.create_rectangle (225, 225, 275, 275, fill = "red", outline = "red")
canvas.bind ("<Button-1>", change_taille)

carre  = canvas.create_rectangle ((250-cote//2, 250-cote//2), (250+cote//2, 250+cote//2), fill = "red", outline = "red")


racine.mainloop()