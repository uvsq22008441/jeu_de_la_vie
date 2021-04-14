import tkinter as tk
import random as rd
racine = tk.Tk()

#Import des modules

#constantes



#Fonctions
def bouton_pause():
    pass

def start():
    mouvement(balle)

def creer_balle():
    x, y = 300, 200
    r = 20
    cercle = canvas.create_oval(300-r,200-r, 300+r, 200+r, fill = "blue")
    dx = rd.randint(1, 7)
    dy = rd.randint(1, 7)
    return [cercle, dx, dy]

def mouvement(b):
    global id_after
    canvas.move(b[0], b[1], b[2])
    id_after = canvas.after(20, lambda : mouvement(b))
    rebond1(b)
 
#Programme principal



#Création des widgets
canvas = tk.Canvas(racine, bg="black", width = 600, height = 400)
bouton =tk.Button(racine, text = "pause", command= start)



#Positionnement Widgets

bouton.grid(row = 2, column = 1)
canvas.grid(row =1, column = 1 )
balle = creer_balle()

racine.mainloop()
