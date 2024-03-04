import numpy as np # Matrice
import random # Fonction aléatoire
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.integrate as integ

# Importation des valeurs
Taille = int(input("Entrez la taille de la matrice : "))
Demi_vie = float(input("Entrez la valeur de la demi-vie du matériau : "))
pas_t = float(input("Entrez le pas temporel : "))
duree = float(input("Entrez la durée totale de l'étude : "))
Demi_vie1 = float(input("Entrez la valeur de la demi-vie1 du matériau : "))
Demi_vie2 = float(input("Entrez la valeur de la demi-vie2 du matériau : "))

def desintegration_radioactive(Taille:int, Demi_vie:float, pas_t:float, duree:float)->np.ndarray:
    taille_matrice = (Taille,Taille)
    Matrice = np.ones(taille_matrice)
    proba_desintegration = np.log(2)*pas_t/Demi_vie
    Releve_Temporel = int(duree/pas_t)
    L_Restant = []
    Nbr_tours = 0
    while Nbr_tours < Releve_Temporel:
        for J in range(Taille):
            for I in range(Taille):
                if Matrice[I][J] == 1:
                    if random.random() < proba_desintegration:
                        Matrice[I][J] = 0
                    else:
                        pass
                else:
                    pass
        image = plt.imshow(Matrice, cmap=cm.binary) # binary nous permet d'avoir le graphique en noir et blanc
        plt.title("En cours de chargement ...")
        plt.axis('off')
        plt.draw()
        plt.pause(0.001)
        image.set_data(Matrice)
        L_Restant.append(np.count_nonzero(Matrice))
        Nbr_tours = Nbr_tours + 1
    print("Le relevé des nombres de pas restant à chaque balayage est :", L_Restant)
    print("A la fin de l'expérience, nous avons la matrice suivante : ")
    print(Matrice)
    plt.title("Terminer")
    plt.show()
    plt.close()
    return Matrice

print(desintegration_radioactive(Taille, Demi_vie, pas_t, duree))
a = -np.log(2)/Demi_vie
t = np.linspace(0, int(duree/pas_t), int(duree/pas_t))

def equation(N, t):
    return a*N

N0 = Taille*Taille
N = integ.odeint(equation, N0, t)
plt.plot(t, N)
plt.title('Graphique équa_diff')
plt.xlabel('temps')
plt.ylabel('N(t)')
plt.show()

print(N)
def filiation_radioactive(Taille:int, Demi_vie1:float, Demi_vie2:float, pas_t:float, duree:float)->np.ndarray:
    taille_matrice = (Taille,Taille)
    Matrice = np.ones(taille_matrice)
    proba_desintegration1 = np.log(2)*pas_t/Demi_vie1
    proba_desintegration2 = np.log(2)*pas_t/Demi_vie2
    Releve_Temporel = int(duree/pas_t)
    Releve_Temporel1 = Releve_Temporel - Demi_vie2
    Releve_Temporel2 = Releve_Temporel - Releve_Temporel1
    L_Restant1 = []
    L_Restant2 = []
    Nbr_tours = 0
    while Nbr_tours < Releve_Temporel1:
        for J in range(Taille):
            for I in range(Taille):
                if Matrice[I][J] == 1:
                    if random.random() < proba_desintegration1:
                        Matrice[I][J] = 0
                    else:
                        pass
                else:
                    pass
        image = plt.imshow(Matrice, cmap=cm.binary) # binary nous permet d'avoir le graphique en noir et blanc
        plt.title("En cours de chargement 1er ...")
        plt.axis('off')
        plt.draw()
        plt.pause(0.001)
        image.set_data(Matrice)
        L_Restant1.append(np.count_nonzero(Matrice))
        Nbr_tours = Nbr_tours + 1
    plt.title('Pause')
    plt.pause(20)
    Nbr_tours = 0
    while Nbr_tours < Releve_Temporel2:
        for J in range(Taille):
            for I in range(Taille):
                if Matrice[I][J] == 1:
                    if random.random() < proba_desintegration2:
                        Matrice[I][J] = 0
                    else:
                        pass
                else:
                    pass
        image = plt.imshow(Matrice, cmap=cm.binary) # binary nous permet d'avoir le graphique en noir et blanc
        plt.title("En cours de chargement 2eme ...")
        plt.axis('off')
        plt.draw()
        plt.pause(0.001)
        image.set_data(Matrice)
        L_Restant2.append(np.count_nonzero(Matrice))
        Nbr_tours = Nbr_tours + 1
    print("Le relevé des nombres de pas restant à chaque balayage de la 1er desintegration est :", L_Restant1)
    print("Le relevé des nombres de pas restant à chaque balayage de la 2eme desintegration est :", L_Restant2)
    print("A la fin de l'expérience, nous avons la matrice suivante : ")
    print(Matrice)
    plt.title("Terminer")
    plt.show()
    plt.close()
    return Matrice

print(filiation_radioactive(Taille, Demi_vie1, Demi_vie2, pas_t, duree))
a1 = -np.log(2)/Demi_vie1
a2 = -np.log(2)/Demi_vie2

Releve_Temporel = int(duree/pas_t)
Releve_Temporel1 = int(Releve_Temporel - Demi_vie2)
Releve_Temporel2 = int(Releve_Temporel - Releve_Temporel1)

t1 = np.linspace(0, Releve_Temporel1, Releve_Temporel1)

def equation1(N1, t1):
    return a1*N1

N0 = Taille*Taille

N1 = integ.odeint(equation1, N0, t1)
plt.subplot(1, 1, 1)
plt.plot(t1, N1, label="1er")

x = N1[-1]

t2 = np.linspace(Releve_Temporel1, Releve_Temporel1 + Releve_Temporel2, Releve_Temporel2)

def equation2(N2, t2):
    return a2*N2

N2 = integ.odeint(equation2, int(x), t2)
plt.subplot(1, 1, 1)
plt.plot(t2, N2, "r-", label="2eme")
plt.title('Graphique équa_diff_filiation')
plt.xlabel('temps')
plt.ylabel('N(t)')
plt.legend()
plt.show()

print(N1)
print(N2)
