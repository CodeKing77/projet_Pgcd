from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from math import *
from PIL import Image , ImageTk  #Importation des bibliothèques de pour l'affichage d'images sur la fenêtre


def calcul(event):
    try :
        premierNombre = int(zoneSaisiePremierNombre.get())
        secondNombre = int(zoneSaisieSecondNombre.get())

    except :
        showwarning("Erreur", "Veuillez entrer des nombres entiers")
        return

    else :
        operation = choixFonction.get()
        match operation:
            case "PGCD" :
                resultatPgcd = gcd(premierNombre, secondNombre)
                labelAffichageResultat["text"] = f"PGCD = {resultatPgcd}"
            
            case "PPCM" :

                resultatPpcm = lcm(premierNombre, secondNombre)
                labelAffichageResultat["text"] = f"PPCM = {resultatPpcm}"

            case _ :
                labelAffichageResultat["text"] = "Veuillez choisir une Opération"

def calculFonction():
    try :
        premierNombre = int(zoneSaisiePremierNombre.get())
        secondNombre = int(zoneSaisieSecondNombre.get())

    except :
        showwarning("Avertissement", "Veuillez entrer des nombres entiers")
        return

    else :
        operation = choixFonction.get()
        match operation:
            case "PGCD" :
                resultatPgcd = gcd(premierNombre, secondNombre)
                labelAffichageResultat["text"] = f"PGCD = {resultatPgcd}"
            
            case "PPCM" :

                resultatPpcm = lcm(premierNombre, secondNombre)
                labelAffichageResultat["text"] = f"PPCM = {resultatPpcm}"

            case _ :
                labelAffichageResultat["text"] = "Veuillez choisir une Opération"

def annulation():
    zoneSaisiePremierNombre.delete(0, END)
    zoneSaisieSecondNombre.delete(0,END)
    labelAffichageResultat["text"] = ""

#Création et configuration de la fenêtre principale
fenetre = Tk()
fenetre.title("Calcul PGCD | PPCM")
fenetre.geometry("650x450")
fenetre.resizable(width=False , height=False)
fenetre.eval('tk::PlaceWindow .  center')    #Pour centrer la fenêtre principale
fenetre.config(background="darkslateblue")


# Charger l'image pour l'icône de la fenêtre
icon_path = "C:/Users/lenovo/Desktop/MyApps/projet_calculPgcd/calculpgcd_png.png" 
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)
fenetre.iconphoto(False, icon_photo)


#Ajout des Widgets
labelDuPremierNombre = Label(fenetre, text="Entrer le premier nombre : ")
labelDuPremierNombre.place_configure(x= 50 , y=50)

labelDuSecondNombre = Label(fenetre, text="Entrer le second nombre :")
labelDuSecondNombre.place_configure(x=50 , y=100)

labelChoixFonction = Label(fenetre, text="Choisir Fonction : ")
labelChoixFonction.place_configure(x=50 , y=150)

zoneSaisiePremierNombre = Entry(fenetre)
zoneSaisiePremierNombre.place_configure(x=250 , y=40, width=350 , height=30)

zoneSaisieSecondNombre = Entry(fenetre)
zoneSaisieSecondNombre.place_configure(x= 250, y= 90, width= 350, height=30)

listeFonction =[#"Veuillez choisir une fonction....",
                "PGCD",
                "PPCM"]
choixFonction = Combobox(fenetre, values=listeFonction, width=54)  # Affichage du Combobox (liste à choix multiple)
choixFonction.place_configure(x=250 , y=150)
choixFonction.configure(justify="center")    #Centre chaque item de la liste à choix multiple
choixFonction.set("Veuillez choisir une fonction...")  # définir ce qui s'affichera par défaut
choixFonction.bind("<<ComboboxSelected>>" , calcul)   #Liaison 


labelAffichageResultat = Label(fenetre, text="")
labelAffichageResultat.place_configure(x= 250 , y=220)


#Ajout des boutons
#boutonDeCalcul =  Button(fenetre, text="Calculer", command=calculFonction)
#boutonDeCalcul.place(x=250 , y=300)

boutonAnnuler  = Button(fenetre, text="Annuler", command=annulation)
boutonAnnuler.place(x=330 ,  y=250, width=150 , height=40)


#Affichage de la fenêtre principale
fenetre.mainloop()