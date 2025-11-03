'''
Tony Baude
18.08.23

Dieses Dokument enthält Klassen zum Ausführen von Feedback 1.
Folgende Klassen sind enthalten:
    - Category : Eine Klasse repräsentiert das Thema des gezeigten Satzes.
    - Feedback1 : Diese Klasse repräsentiert das Feedback 1.
'''

import nltk
nltk.download('reuters')
#Countdown mithilfe von https://www.delftstack.com/de/howto/python/python-countdown-timer/#:~:text=Als%20erstes%20m%C3%BCssen%20Sie%20das%20Modul%20time%20importieren%2C,der%20Sekunden%20%28num_of_secs%29%2C%20auf%20die%20der%20Timer%20herunterz%C3%A4hlt.
import Einmalig
from nltk.corpus import reuters
import random
import re
import time
import threading

class Category:
    '''
    Eine Klasse repräsentiert das Thema des gezeigten Satzes.

    Attribute:
        category (str): Eine zufällig ausgewähltes Thema aus dem Reuters-Korpus.
        Sätze (list): Eine Liste von Sätzen zum ausgewählten Thema.
        index (int): Eine Zahl als Index, um die Einzelsätze zu benutzen.
        index_list (list): In dieser Liste werden die bereits genutzten Indexe gespeichert.
    '''

    def __init__(self):
        '''
        Initialisiert ein Thema.
        
        Parameter:
            category (str): Eine zufällig ausgewähltes Thema aus dem Reuters-Korpus.
            Sätze (list): Eine Liste von Sätzen zum ausgewählten Thema.
            index (int): Eine Zahl als Index, um die Einzelsätze zu benutzen.
            index_list (list): In dieser Liste werden die bereits genutzten Indexe gespeichert.
        '''
        self.category = random.choice(reuters.categories())
        self.Sätze = reuters.sents(categories=self.category)
        self.index = 0
        self.index_list = []

    def Satz(self):
        '''
        Diese Funktion gibt einen passenden Satz aus der Satzliste wieder.
            Kriterien:
                - Nur Sätze mit weniger als 20 Token werden akzeptiert.
                - Sätze mit mehr als 3 numerischen Token werden aussortiert.
                - Der Themenname muss zensiert werden.
        '''
        sinnvoll = False
        while sinnvoll is False:
            if self.index < len(self.Sätze):
                '''
                Kriterium 1:
                    Sätze mit mehr als 20 Token werden aussortiert.
                '''
                if len(self.Sätze[self.index]) > 20:
                    self.index += 1
                else:
                    """
                    Kriterium 2:
                        Bei mehr als 3 numerischen Token wird der Satz aussortiert.
                    """
                    Satz = ' '.join(self.Sätze[self.index])
                    #Int/Floats finden
                    pattern1 = r"\b\d+\b" or r"\b\d+\.\d+\b" or r"\b\d+\,\d+\b"
                    numbers = re.findall(pattern1, Satz)
                    if len(numbers) > 3:
                        self.index += 1

                    else:
                        '''                     
                        Kriterium 3:
                            Wenn der Themenname gefunden wird, wird dieser maskiert.
                        '''
                        pattern2 = self.category
                        new_satz = re.sub(pattern2, '[HIDDEN]', Satz)
                        self.index_list.append(self.index)
                        sinnvoll = True
                        return new_satz
            else:
                print('Keine passenden Sätze im Datensatz.')
                    
    def clarify(self):
        '''
        Diese Funktion gibt ein weiteren gültigen Satz für das Thema aus.
        
        Returns:
            Satz (func): Diese Funktion gibt einen passenden Satz aus der Satzliste wieder.
        '''
        last_index = self.index_list[-1]
        if last_index + 1 < len(self.Sätze):
            self.index = last_index + 1
            return self.Satz()
        else:
            return ('Keine Tipps im Datensatz mehr.')
        
#Feedback 1 Bewertung

class Feedback1:
    '''
    Diese Klasse repräsentiert das Feedback 1.
    
    Attribute:
        ev (str): Die erspielten Evaluationspunkte des Spielers (anfangs 0) werden zunächst nur im Feedback 1 gespeichert und nicht auf die Spieler EV übertragen.
        theme (int): Gibt an bei welchem Thema der Spieler ist.
        countdown_abgelaufen (bool):
            False, wenn der Countdown nicht abgelaufen ist.
            True, wenn der Countdown abgelaufen ist.
    '''

    def __init__(self):
        '''
        Initialisierung des Feedbacks 1.
        
        Parameter:
            ev (str): Die erspielten Evaluationspunkte des Spielers (anfangs 0).
            theme (int): Gibt an bei welchem Thema der Spieler ist.
            countdown_abgelaufen (bool):
                False, wenn der Countdown nicht abgelaufen ist.
                True, wenn der Countdown abgelaufen ist.
        '''
        self.ev = int()
        self.theme = 1
        self.countdown_abgelaufen = False

    def first_try(self):
        '''
        Wenn beim ersten Versuch das Thema erfolgreich erraten wurde, bekommt der Spieler 40 Evaluationspunkte (EV).
        '''
        self.ev += 40

    def second_try(self):
        '''
        Wenn beim zweiten Versuch das Thema erfolgreich erraten wurde, bekommt der Spieler 30 Evaluationspunkte (EV).
        '''
        self.ev += 30

    def third_try(self):
        '''
        Wenn beim dritten Versuch das Thema erfolgreich erraten wurde, bekommt der Spieler 20 Evaluationspunkte (EV).
        '''
        self.ev += 20

    def countdown(self):
        '''
        Diese Funktion ist ein Countdown von 1 Minute, welcher bei der späteren Themenabfrage jeweils runterzählt.

        https://www.delftstack.com/de/howto/python/python-countdown-timer/#:~:text=Als%20erstes%20m%C3%BCssen%20Sie%20das%20Modul%20time%20importieren%2C,der%20Sekunden%20%28num_of_secs%29%2C%20auf%20die%20der%20Timer%20herunterz%C3%A4hlt.    
        
        Returns:
            countdown_abgelaufen (bool):
                False, wenn der Countdown nicht abgelaufen ist.
                True, wenn der Countdown abgelaufen ist. 
            Wenn countdown_abgelaufen = True:
                ev: Die erspielten Punkte werden auf 0 zurückgesetzt.
        '''    
        num_of_secs = int(60)
        while num_of_secs and not self.input_received:
            m, s = divmod(num_of_secs, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            time.sleep(1)
            num_of_secs -= 1
        if num_of_secs == 0:
            print('Timer abgelaufen!\nBitte die Entertaste drücken.')
            self.ev = 0
            self.countdown_abgelaufen = True
        else:
            self.countdown_abgelaufen = False   

    def Durchführung(self):
        '''
        Mit dieser Funktion wird Feedback 1 ausgeführt.

        Parameters:
            Category (class): Eine Klasse repräsentiert das Thema des gezeigten Satzes.
            einmalige_funktion (func): Gegebene Funktion wird durch diese nur einmal ausgeführt.
        '''
        #Initalisierung einzelner Themen.
        category = Category()
        category1 = Category()
        category2 = Category()
        category3 = Category()
        tries = 1
        Einmalig.einmalige_funktion_ausgefuehrt
        max_clarify_calls = 1

        # Schleife für Themenabfrage
        while self.theme <= 3:

            clarify_calls = 0
            Einmalig.einmalige_funktion_ausgefuehrt = False

            if self.theme == 1:
                category = category1
            elif self.theme == 2:              
                category = category2
            elif self.theme == 3:
                category = category3

            if tries > 3:
                break

            print('If you need a tip you can use clarify(c) once per topic.')  

            while tries <= 3:

                Satz = category.Satz()
                print(Satz)
                #print(category.category)
                "print('Can you identify this topic?')"
                self.input_received = False

                # Input-Countdown-Thread starten
                #https://stackoverflow.com/questions/51123971/a-simple-way-to-run-a-piece-of-python-code-in-parallel
                countdown_thread = threading.Thread(target=self.countdown)
                countdown_thread.start()

                user_input = input('Your answer: ')
                self.input_received = True
                if self.countdown_abgelaufen == True:
                    tries += 3
                    self.theme += 3

                countdown_thread.join()

               #Betrachtung User-Input
                if user_input == 'c' and clarify_calls < max_clarify_calls:
                    if not Einmalig.einmalige_funktion_ausgefuehrt:
                            Einmalig.einmalige_funktion(category.clarify)
                            clarify_calls += 1
                else:
                    
                    if tries == 1:
                        if  user_input == category.category:
                            self.first_try()
                            self.theme += 1
                            tries = 1
                            break
                        else:
                            print('Try again')
                        tries += 1

                    elif tries == 2:
                        if  user_input == category.category:
                            self.second_try()
                            self.theme += 1
                            tries = 1
                            break
                        else:
                            print('Try again')
                        tries += 1

                    elif tries == 3:
                        if  user_input == category.category:
                            self.third_try()
                            self.theme += 1
                            tries = 1
                            break
                        else:
                            print('You have lost. Unfortunately, your monster adventure is over.')
                        tries += 1
                        break
        #Nach 3 missglückten Versuchen hat der Spieler verloren.
        if self.theme > 3:
            if tries >= 1:
                print('Spiel beendet.')
#Initialisierung Feedback 1
feedback1 = Feedback1()