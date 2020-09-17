from datetime import date
from random import *
from statistics import mean

class Etudiant:


    def __init__(self, prenom:str, nom:str, date_de_naissance:date):
        self.vivant = True
        self.prenom = prenom
        self.nom = nom
        self.date_de_naissance = date_de_naissance
        self.notes = []


    def evaluation(self):
        print(f"{self.prenom} passe une évaluation ...")
        self.noteActuelle = randint(0, 20)
        print(f"{self.prenom} a eu {self.noteActuelle} /20 !")
        self.notes.append(self.noteActuelle)

    def moyenne(self):
        print(f"{self.prenom} a eu les notes suivantes : {self.notes}")
        self.moyenneuser=mean(self.notes)
        print(f"{self.prenom} a une moyenne de {self.moyenneuser}")



adrien = Etudiant("Adrien","Fontaine",date(1994, 7, 4))
print(adrien.__dict__)


adrien.evaluation()
adrien.evaluation()
adrien.evaluation()
adrien.evaluation()
adrien.moyenne()