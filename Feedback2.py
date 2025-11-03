'''
Tony Baude
23.08.2023

Dieses Dokument enthält Funktionen zum Ausführen von Feedback 2.
Folgende Funktionen sind enthalten:
    - gueltiger_Codesatz: Die Funktion überprüft die Gültigkeit des eingegebenen Codesatzes.
    - feedback2 : Diese Funktion überprüft, ob der eingegebene Codesatz gültig ist, indem sie die Funktion gueltiger_Codesatz verwendet. Bei gültigem Codesatz wird die Evaluation des Spielers aktualisiert.
'''
import re
from FunktionClass import spieler1
from Feedback1 import feedback1

def gueltiger_Codesatz(string):
    '''
    Die Funktion überprüft die Gültigkeit des eingegebenen Codesatzes.

    Parameters:
        string(str): Der eingegebene Input des Spielers.

    Returns:
        Bool:   True, wenn Codesatz gültig.
                False, wenn Codesatz ungültig.
    '''
    #Mithilfe des Patterns werden Sonderzeichen im String aussortiert und der String wird in seine Tokens gespalten.
    pattern = r'[\*\-\!\?\'\$\.\,]'
    string = re.sub(pattern, '', string)
    woerter_list = string.lower().split()

    if len(woerter_list) == 0:
        return True
    
    if len(woerter_list) == 1:
        buchstaben = str(woerter_list[0])
        buchstaben = buchstaben.split()
        if buchstaben[0] <= buchstaben[-1]:
            return True
        else:
            return False
    
    else:
        #Rekursive Funktion, bei der jeweils das erste mit dem letzten Wort (jeweils der erste und jeweils der letzte Buchstabe miteinander) verglichen  wird.
        wort1 = woerter_list[0]
        wort2 = woerter_list[-1]
        if wort1[0] <= wort2[0] and wort1[-1] <= wort2[-1]:
            woerter_list = woerter_list[1:-1]
            string = ' '.join(woerter_list)
            return gueltiger_Codesatz(string)
        else: 
            return False
        

def feedback2():
    '''
    Diese Funktion überprüft, ob der eingegebene Codesatz gültig ist, indem sie die Funktion gueltiger_Codesatz verwendet. 
    Bei gültigem Codesatz wird die Evaluation des Spielers aktualisiert.
    '''
    tries = 1
    while tries <= 3:
        string = input('Codesatz:')
        if gueltiger_Codesatz(string) is True:
            print("Congratulations you've got the Code")
            spieler1._ev += 80
            spieler1._ev += feedback1.ev
            tries += 3
        else: 
            if tries == 3:
                print("wrong answer. You don#t have anymore tries.")
                tries += 1
            else:
                print("please try again")
                tries += 1