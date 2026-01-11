#=================>>>PROJET n°2: Le jeu du pendue<<<=================#

from random import *
from turtle import *
from tab_difficile import *
from tab_facile import *

n = 0
def pendu(n):
    """
    Entrer: n qui est le nombre d'erreur que la personne a fait (int)
    Sortie: La representation graphique du pendu en fonction de n (turtle)
    Cette fonction renvoie le pendu dessiner en fonction du nombre d'erreur n
    """
    if n == 1:
        bgcolor("yellowgreen")
        pencolor('saddlebrown')
        pensize(10)
        forward(100)

    if n == 2:
        right(180)
        forward(50)
        right(90)
        forward(200)
        
    if n == 3:
        right(90)
        forward(100)

    if n == 4 :
        right(180)
        forward(50)
        left(45)
        forward(71)
        pensize(3)
        right(180)
        forward(71)
        right(45)
        forward(40)
        right(90)
        
    if n == 5:
        
        pencolor('gray')
        forward(30)
        right(90)
        
    if n == 6:
        pencolor('navajowhite')
        pensize(5)
        circle(20)
        left(90)
        up()
        forward(40)
        down()
        
    if n == 7:
        forward(50)

    if n == 8:
        right(30)
        forward(50)
        
    if n == 9:
        right(180)
        forward(50)
        right(120)
        forward(50)

    if n == 10:
        right(180)
        forward(50)
        right(30)
        forward(30)
        left(120)
        forward(40)

    if n== 11 :
        right(180)
        forward(40)
        right(60)
        forward(40)
        right(110)
        up()
        forward(500)
        down()
        pencolor('red')
        pensize(50)
        write("TU ES PENDU !!!!!!", font=('Arial', 36))
        up()
        forward(50)
pendu(n)
reponse = "rien"

reponse = input("Voulez vous jouer au mode facile ou difficile ? ",)

if reponse == "facile":
    mot_aléatoire = choice (f)

elif reponse == "difficile":
    mot_aléatoire = choice (d)
else:
    print("Recommencer le programme")
    
mot_decouvert = []
#on ajoute la première lettr
mot_decouvert.append(mot_aléatoire[0])
#on ajoute les tirets
mot_decouvert = mot_decouvert + [("_")for i in range (len(mot_aléatoire)-2)]
#on ajoute la dernière lettre
mot_decouvert.append(mot_aléatoire[-1])


def affiche(tab_mot):
    """
    Entrer: Un tableau contenant la premier et derniere lettre d'un
    mot séparé du nombre de tirets des lettres manquantent (tab)
    Sortie: lettre du mot qui etait dans le tableau (str)
    Cette fonction affiche les elements du tableau sous forme d'une chaine de caractere
    """
    for i in range(len(tab_mot)):
        print(tab_mot[i],end=" ")


while '_' in mot_decouvert:
    affiche(mot_decouvert)
    print()
    lettre_choisie = str(input("Entrer une lettre : ",))
    for i in range(len(mot_aléatoire)):
        if lettre_choisie == mot_aléatoire[i]:
            mot_decouvert[i] = lettre_choisie

    if lettre_choisie not in mot_aléatoire:
        n += 1
        pendu(n)

    if n >= 11:
        print("tu as perdu! le mot été",mot_aléatoire,"!")
        mot_decouvert = mot_aléatoire

if n < 11:
    print("tu as gagner! le mot été bien ",mot_aléatoire,"!")
