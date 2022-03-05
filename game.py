from pretty_table import PrettyTable 
class Jeu:
    def __init__(self):
        self.j1 : tuple = ("o", "Joueur 1")
        self.j2 : tuple = ("x", "Joueur 2")
        self.plateau = \
            [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
            ]
        self.boucle_jeu()
    def boucle_jeu(self):
        while True:
            self.tour = self.j1
            self.affichage()
            self.jouer()
            self.test_resultat()
            if self.fin_du_jeu()[0]:break

            self.tour = self.j2
            self.affichage()
            self.jouer()
            self.test_resultat()
            if self.fin_du_jeu()[0]:break


    def jouer(self):
        pos = input("Entrez les coordonées séparées par une virgule : ")
        pos = pos.split(",")
        pos = list(map(int, pos))
        pos = [x-1 for x in pos if x > 0]
        self.plateau[pos[0]][pos[1]]=self.tour[0]

    def fin_du_jeu(self) -> tuple:
        plateau = self.plateau
        resultat = (False, 0) # égalité par défaut
        # 1 -> victoire
        # 0 -> égalité
        # horizontale
        for i in range(0,3):
            compteur = 0
            for j in range(0,3):
                if plateau[i][j] == self.tour[0]:
                    compteur += 1
            if compteur == 3:
                resultat = (True, 1)
        
        #verticale
        for i in range(0,3):
            compteur = 0
            for j in range(0,3):
                if plateau[j][i] == self.tour[0]:
                    compteur += 1
            if compteur == 3:
                resultat = (True, 1) 

        #diagonale 1
        compteur = 0
        for i in range(0,3):
            if plateau[i][i] == self.tour[0]:
                compteur += 1
            if compteur == 3:
                resultat = (True, 1)

        #diagonale 2
        compteur = 0
        for i in range(0,3):
            if plateau[2-i][i] == self.tour[0]:
                compteur += 1
            if compteur == 3:
                resultat = (True, 1)
        
        #égalité
        compteur = 0
        for i in range(3):
            for j in range(3):
                if plateau[i][j] != " ":
                    compteur += 1
        if compteur == 9 and resultat[0] == False:
            resultat = (True, 0)

        return resultat
    
    def test_resultat(self):
        fdj = self.fin_du_jeu()
        if fdj[0]:
            if fdj[1] == 1:
                self.affichage()
                print(f"Le gagnant est le {self.tour[1]}")
            elif fdj[1] == 0:
                self.affichage()
                print("Egalité entre les deux joueurs")
    
    def affichage(self):
        print(f"Tour du {self.tour[1]} => {self.tour[0]}")
        plateau = PrettyTable(self.plateau)


if __name__ == '__main__':
    instance = Jeu
    instance()
