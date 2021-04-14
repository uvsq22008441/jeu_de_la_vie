import tkinter as tk
import random as rd

#Import des modules

racine = tk.Tk()
racine.title("titre")
demarrer = False

#constantes

#Fonctions
def bouton_demarrer():
    global demarrer
    if not demarrer :
        mouvement(balle)
        bouton.config( text = "arreter")
        demarrer = True
    else:
        canvas.after_cancel(id_after)
        bouton.config( text = "demarrer")
        demarrer = False

def rebond1(b):
    x0, y0, x1, y1 = canvas.coords(b[0])
    print(x0, y0, x1, y1)
    if x0 <= 0 or x1 >= 600 :
        b[1] = -b[1]
    if y0 <= 0 or y1 >= 400 :
        b[2] = -b[2]




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
canvas = tk.Canvas(racine, bg = "black", width = 600, height = 400)
bouton = tk.Button(racine, text = "demarrer", command = bouton_demarrer)

#Positionnement Widgets
canvas.grid(row = 1, column = 1)
bouton.grid(row = 2, column = 1)
balle = creer_balle()
racine.mainloop()


can1.itemconfigure(ovall, fill = "blue")
