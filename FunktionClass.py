'''
Tony Baude
01.08.2023

Diese Datei enthält eine Klasse zum Initialisieren von Spielern.
Folgende Klasse ist enthalten: Eine Dataclass repräsentiert einen Spieler.
    - Report (dataclass): 
'''

import nltk
nltk.download('names')
import random
from dataclasses import dataclass
from nltk.corpus import names


@dataclass
class Report:
    '''
    Eine Dataclass repräsentiert einen Spieler.
    
    Attribute:
        ep (int): Das Energie Level des Spielers (anfangs bei 10).
        ev (int): Die Evaluation des Spielers (anfangs bei 0).
        liste_studenten (dict): Dictionary, in welchem die Namen und Noten der Schüler gespeichert werden (anfangs ohne Namen und Noten).
        will_spieler_spielen (bool): Ein boolesches Attribut, das angibt, on der Spieler spielen möchte.
                                    True, wenn der Spieler spieln möchte, ansonsten False.
    '''
    _ep = int(10)
    _ev = int(0)
    _liste_studenten = dict()
    will_spieler_spielen = True

    def play_again(self):
        '''
        Diese Funktion setzt alle Attribute in ihren Urzustand, bricht das Spiel aber nicht ab.
        '''
        self._ep = int(10)
        self._ev = (0)
        self._liste_studenten = {}

    def exit(self):
        '''
        Diese Funktion bricht das Spiel ab und setzt die Attribute in ihren Urzustand zurück.
        '''
        self.will_spieler_spielen = False
        self._ep = int(10)
        self._ev = (0)
        self._liste_studenten = {}

    def liste_befuellen(self):
        '''
        Die Studentenliste wird mit 8 zufällig generierten Namen befüllt.
        '''
        num_students = 8
        for number in range(num_students):
            namens_liste = names.words()
            namen = random.choice(namens_liste)
            self._liste_studenten[namen] = []

    def inspect_report(self):
        '''
        Gibt den Semesterbericht mit dem Energy Level (EP), der Evaluation (EV) und der Notenliste der Studierenden wieder.
        '''
        print(f'*****Semester Report*****\nEnergy Level: {self._ep}          Evaluation: {self._ev}\nGrades:')
        for student, note in self._liste_studenten.items():
            print(f'\t{student.ljust(20)}\t{" / ".join(map(str, note))}')

    #Bewertung

    def rest(self):
        '''
        Der Spieler ruht sich aus und erhöht sein Energy Level (EP) um 5.
        '''
        self._ep += 5
        print('EP: +5')

    def chocolate(self):
        '''
        Der Spieler nimmt ein Snack zu sich und erhöht sein Energy Level (EP) um 10.
        '''
        self._ep += 10
        print('EP: +10')

    def note(self):
        '''
        Der Spieler bewertet Aufgaben und verringert sein Energy Level (EP) um 5.
        '''
        self._ep -= 5
        print('EP: -5')

    def dankbarkeit(self):
        '''
        Studierende bedanken sich beim Spieler, was sein Energy Level (EP) um 3 erhöht.
        '''
        self._ep += 3
        print('A student is grateful to you for your evaluation.\nEP: +3')

    def uebermaessiges_debugging(self):
        '''
        Der Spieler muss übermäßig viel debuggen , was sein Energy Level (EP) um 1 verringert. 
        '''
        self._ep -= 1
        print('You need to debug excessively.\nEP: -1')

    def neubewertung(self):
        '''
        Studierende fordern eine Neubewertung beim Spieler, was sein Energy Level (EP) um 2 verringert.
        '''
        self._ep -= 2
        print('A student calls for a reassessment.\nEP: -2')

    def verlaengerung(self):
        '''
        Studierende fordern eine Verlängerung bei Spieler, was sein Energy Level (EP) um 3 verringert.
        '''
        self._ep -= 3
        print('A student wants an extension.\nEP: -3')
        
    def Bewertung(self):
        '''
         Die Bewertung erfolgt zufällig, und je nach dem erzielten Wert wird eine der folgenden Aktionen ausgeführt:
    
            - Mit einer Wahrscheinlichkeit von 10% wird die Dankbarkeit des Spielers erhöht.
            - Mit einer Wahrscheinlichkeit von 30% wird übermäßiges Debugging ausgelöst.
            - Mit einer Wahrscheinlichkeit von 20% erfolgt eine Neubewertung.
            - Mit einer Wahrscheinlichkeit von 20% wird die Verlängerung aktiviert.

        Diese Bewertungsfunktion beeinflusst das Energy Level (EP) des Spielers.
        '''

        self.note()
        zahl = random.randint(1,100)
        if zahl >= 1 and zahl <= 10:
            self.dankbarkeit()
        elif zahl >= 11 and zahl <= 40:
            self.uebermaessiges_debugging()
        elif zahl >= 41 and zahl <= 60:
            self.neubewertung()
        elif zahl >= 61 and zahl <= 80:
            self.verlaengerung()    

#Initialisierter Spieler   
spieler1 = Report()