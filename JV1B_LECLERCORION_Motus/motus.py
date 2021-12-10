#importation des bibliothèques nécessaires
import random
from colorama import Back, Style 

#définition des fonctions
def presenceLettre(mot,lettre): #vérifie la présence d'une lettre dans un mot
    for i in range(6):
        if mot[i]==lettre:
            return True
    return False

def indexLettre(mot,lettre): #renvoie l'index d'une lettre dans un mot
    stock=0
    for i in range(6):
        if mot[i]==lettre:
            return i

def doubleLettre(mot,lettre): #vérifie si une lettre est en double dans le mot
    compteur=0
    for i in range(6):
        if mot[i]==lettre:
            compteur+=1
    if compteur==2:
        return True
    else:
        return False

def indexDeuxiemeLettre(mot,lettre): #renvoie l'indice de la deuxième lettre dans le cas d'une lettre présente en double
    stock=0
    for i in range(6):
        if mot[i]==lettre:
            stock= i
    return stock

def testVictoire(mot,tentative): #vérifie si le mot essayé par le joueur est le même que le mot à deviner
    if tentative==mot:
        return True
    else:
        return False

#initialisation des variables
liste_mots= ["OISEAU","JOYEUX","HOCKEY","YAKUZA", "PYJAMA", "ZEPHYR", "AGENDA", "CROIRE", "ARCADE", "GATEAU"] #liste de dix mots à six lettres
tirage= random.randint(0,9) #tire un nombre aléatoire entre 0 et 9
mot= liste_mots[tirage] #le mot à deviner devient le mot de la liste ayant pour index le nombre aléatoire
victoire=False
compteurTour=0
deuxiemeLettre=False


while not victoire and compteurTour<8: #permet au joueur de continuer à deviner tant qu'il n'as pas gagné ou fait trop de tentatives
    
    tentative= input ("\n"+"Entrez un mot de six lettres: ")
    tentative= tentative.upper() 
    for j in range(6):
        lettre = tentative[j]
        if not doubleLettre(mot,lettre):
            if indexLettre(mot, lettre)== j:
                print(Back.RED+ lettre,end="")
            elif presenceLettre(mot,lettre):
                print(Back.YELLOW+ lettre,end="")
            else:
                print(Back.BLUE+ lettre,end="")
        else:
            if deuxiemeLettre:
                if indexDeuxiemeLettre(mot, lettre)==j:
                    print(Back.RED+ lettre,end="")
                elif presenceLettre(mot,lettre):
                    print(Back.YELLOW+ lettre,end="")
                else:
                    print(Back.BLUE+ lettre,end="" )
            else:
                if indexLettre(mot, lettre)== j:
                    print(Back.RED+ lettre,end="")
                    deuxiemeLettre= True
                elif presenceLettre(mot,lettre):
                    print(Back.YELLOW+ lettre,end="")
                else:
                    print(Back.BLUE+ lettre,end="")

    victoire=testVictoire(mot,tentative)
    compteurTour+=1
    print(Style.RESET_ALL)


if victoire:
    print("\n"+"Vous avez gagné")
else:
    print("\n"+"Vous avez échoué")




