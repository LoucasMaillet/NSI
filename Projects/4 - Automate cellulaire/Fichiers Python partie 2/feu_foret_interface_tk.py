# -*- coding: utf-8 -*-
"""
Mini projet automate cellulaire - simulation d'un feu de forêt

Partie 2 : INTERFACE GRAPHIQUE TKINTER

@author: 
"""


from tkinter import Tk, Canvas, Button, Label
from feu_foret_automate_cor import construction_grille, mise_a_jour_grille, etats_ac


COULEURS = ["ivory", "lime green", "red", "gray75"]
UNIT = 10
N = 50  # nombre de lignes / colonnes de la grille (taillen x n)
P = .6 # densité d'arbres dans la grille
run_stop = False # état run/stop de l'automate cellulaire

# Added constants
UPD_TIME = 50


def dessiner_cellule(grille, i, j):
    A = (UNIT*j, UNIT*i)
    B = (UNIT*(j+1), UNIT*(i+1))
    etat = grille[i][j]
    couleur = COULEURS[etat]
    cnv.create_rectangle(A, B, fill = couleur, outline='')


def dessiner_grille(grille):
    n = len(grille)
    for i in range(n):
        for j in range(n):
            dessiner_cellule(grille, i, j)


def actualiser_etats():
    # val_arbres_en_feu["text"]=f'{etats_ac["arbres_en_feu"]}'
    # TODO : question 9
    for k in vals:
        vals[k]["text"]=etats_ac[k]

def incendier_arbre(event):
    global parcelle
    i, j = event.y//UNIT, event.x//UNIT
    if parcelle[i][j] == 1:
        parcelle[i][j] = 2
        dessiner_cellule(parcelle, i, j)
        dessiner_grille(parcelle)
        etats_ac['arbres_en_feu'] += 1
        etats_ac['arbres_en_vie'] -= 1
        actualiser_etats()


def propager_incendie():
    global run_stop
    mise_a_jour_grille(parcelle)
    cnv.delete("all")
    dessiner_grille(parcelle)
    actualiser_etats()
    if run_stop:
        cnv.after(UPD_TIME, propager_incendie)
            
            
      
def lancer_execution():
    global run_stop
    # TODO : question 6
    if run_stop: return
    run_stop = True
    propager_incendie()
    

def arreter_execution():
    global run_stop
    # TODO : question 7
    if run_stop:
        run_stop = False
    

def executer_pas_a_pas():
    propager_incendie()


def reinitialiser_automate():
    global parcelle
    # TODO : question 8
    parcelle = construction_grille(P, N)
    dessiner_grille(parcelle)
    actualiser_etats()


if __name__=='__main__':
    # fenêtre principale
    fenetre_graphique = Tk()
    fenetre_graphique.title('Automate cellulaire simulant un feu de forêt')

    # canevas animation
    cnv = Canvas(fenetre_graphique, width=UNIT*N, height=UNIT*N, background="ivory")
    cnv.grid(row=0, column=0, columnspan=4)

    # éléments de l'interface Homme-Machine : souris, boutons et labels pour affichage
    cnv.bind("<Button-1>", incendier_arbre) # bouton gauche de la souris
    btn_run = Button(fenetre_graphique, text="RUN", command = lancer_execution, width=8)   
    btn_run.grid(row=3, column=0, pady=10)
    btn_stop = Button(fenetre_graphique, text="STOP", command = arreter_execution, width=8) 
    btn_stop.grid(row=3, column=1, pady=10)
    btn_step = Button(fenetre_graphique, text="STEP", command = executer_pas_a_pas, width=8) 
    btn_step.grid(row=3, column=2, pady=10)
    # lbl_arbres_en_feu = Label(fenetre_graphique,text="Arbres en feu", font='Arial 10 bold', width=14)
    # lbl_arbres_en_feu.grid(row=0, column=4, sticky="N", padx=10, pady=10)
    # val_arbres_en_feu = Label(fenetre_graphique,text='0', font='Arial 10 bold', bg='pink', width=8)
    # val_arbres_en_feu.grid(row=0, column=5, sticky="N", padx=10, pady=10)

    # TODO : question 8
    btn_new = Button(fenetre_graphique, text="NEW", command = reinitialiser_automate, width=8) 
    btn_new.grid(row=3, column=3, pady=10)
    

    # TODO : question 9
    vals = {}
    for i, k in enumerate(etats_ac):
        # if k.startswith('_'): continue # for hidden attributes
        lbl = Label(fenetre_graphique, text=k.replace('_', ' ').capitalize(), font='Arial 10 bold', width=14)
        lbl.grid(row=i, column=4, sticky="N", padx=10, pady=10)
        vals[k] = Label(fenetre_graphique,text='0', font='Arial 10 bold', bg='pink', width=8)
        vals[k].grid(row=i, column=5, sticky="N", padx=10, pady=10)

    # initialisation de l'automate cellulaire
    parcelle = construction_grille(P, N)
    dessiner_grille(parcelle)
    actualiser_etats()
    
    fenetre_graphique.mainloop()

