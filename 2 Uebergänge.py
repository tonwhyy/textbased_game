'''
Tony Baude
01.08.2023
Dies ist die Hauptdatei des Spieles, welches das gesamte Spiel aussführt.
'''
from FunktionClass import spieler1
import Einmalig
from Feedback1 import feedback1
import Feedback2 
import re
import random

name = input('WELCOME!\nWhat is your name?\n')

#Storyline
with open('Storyline_Programmierprojekt.txt', 'r') as story:
    storyline = story.read().split('\n')
    storyline = list(filter(None, storyline))

print(storyline[1])
print(f"{name}! " + '\n\n'.join(storyline[2:6]))

#Initialisierung von Zuständen
zustand= 'Start'
zustandsliste = []
bereits_gedruckt = False
bereits_gedruckt1 = False
bereits_gedruckt2 = False

while spieler1.will_spieler_spielen:

    if zustand == 'Start':
        #Speicherung der Zustände
        zustandsliste.append(zustand)
        pattern = re.compile(r"^'Start'")
        zustandsliste= list(filter(lambda x: pattern.search(x), zustandsliste))
        if not bereits_gedruckt:
            #Storyline und Initialisierung
            print('\n' + storyline[6])
            print(f"{name}! " + '\n\n'.join(storyline[7:10]))
            Einmalig.einmalige_funktion_ausgefuehrt = False
            spieler1.liste_befuellen()
            bereits_gedruckt = True

        #Verarbeitung User-Input
        user_input = input('Optionen: grade(g); inspect report(i); exit game(e): ')
        if user_input == 'g':
            bereits_gedruckt = False
            zustandsliste = []
            zustand = 'Bewertung 1'
        elif user_input == 'i':
            spieler1.inspect_report()
        elif user_input == 'e':
            spieler1.exit()
        elif user_input == 'd' or user_input == 'delay grade':
            bereits_gedruckt = False
            zustandsliste = []
            zustand = 'Feedback 1'
        else: print('Befehl konnte nicht erkannt werden')

    elif zustand == 'Bewertung 1' or zustand == 'Bewertung 2':
        zustandsliste.append(zustand)
    
        if zustand == 'Bewertung 1':
            text = '\n'.join(storyline[26:28])
            length_value = 1
            feedback = 'Feedback 1'
            bewertung_already_printed = bereits_gedruckt1
        elif zustand == 'Bewertung 2':
            zustandsliste = [zustand]
            text = storyline[45]
            length_value = 2
            feedback = 'Feedback 2'
            bewertung_already_printed = bereits_gedruckt2

        #Textausgabe. je nachdem ob Bewertung bereits gedruckt worden ist oder nicht.
        if not bewertung_already_printed:
            print(text)
            if zustand == 'Bewertung 1':
                bereits_gedruckt1 = True
            elif zustand == 'Bewertung 2':
                bereits_gedruckt2 = True
        else:
            print("Let's evaluate further.\n")

        index = 46
        options = storyline[28:44]

        # Bewertung einzelner Schüler.
        for key in spieler1._liste_studenten:
 

            if len(spieler1._liste_studenten[key]) < length_value:
                        
                if zustand == 'Bewertung 1':
                    chosen_option = random.choice(options)
                    print(chosen_option)
                    options.remove(chosen_option)
                    user_input = input(f'How would you rate {key}: ')

                elif zustand == 'Bewertung 2':
                    options = ['\n'.join(storyline[index:index+2]), '\n'.join(storyline[index+2:index+4])]
                    print(random.choice(options))
                    index += 4
                    user_input = input(f'How would you rate {key} essay?:')

                # Überprüfung User-Input  
                input_gueltig = False

                while not input_gueltig:
                    pattern = r'[1-4]\,[0|3|7]|[5]\,[0]'
                    gueltig = bool(re.search(pattern, user_input))
                    if gueltig == False:
                        print('Ungültige Eingabe!')
                        user_input = input('Erneute Eingabe: ')
                    else:
                        spieler1._liste_studenten[key].append(user_input)
                        spieler1.Bewertung()
                        input_gueltig = True

                if spieler1._ep < 0:
                    zustand = 'Niederlage'  
                    break
            
                elif 0 <= spieler1._ep < 10:
                    user_input = input('Optionen: rest(r); eat snack(s); inspect report(i); exit game(e); continue(tab): ')
                    if user_input == 'r':
                        zustand = 'Freizeit'
                        break
                    elif user_input == 'i':
                        spieler1.inspect_report()
                        user_input = input('Optionen: rest(r); eat snack(s); exit game(e); continue(tab): ')
                        if user_input == 'r':
                            zustand = 'Freizeit'
                            break
                        elif user_input == 'e':
                            spieler1.exit()
                        elif user_input == 's':
                            zustand = 'Snack'
                            break
                    elif user_input == 'e':
                        spieler1.exit()
                    elif user_input == 's':
                        zustand = 'Snack'
                        break

        #Überprüfung, ob alle Bewertungen abgeschlossen sind
        if all(len(values) == length_value for values in spieler1._liste_studenten.values()):

            pattern = re.compile('^[rsief]$')  
            valid = bool(re.match(pattern, user_input))
        
            user_input = input(f'Optionen: rest(r); eat snack(s); give {feedback.lower()}(f); inspect report(i); exit game(e): ')

            while not re.search(pattern, user_input):
                print('Befehl konnte nicht erkannt werden.')
                user_input = input(f'Optionen: rest(r); eat snack(s); give {feedback.lower()}(f); inspect report(i); exit game(e): ')
            
            if user_input == 'r':
                zustand = 'Freizeit'
            elif user_input == 'i':
                spieler1.inspect_report()
            elif user_input == 'e':
                spieler1.exit()
            elif user_input == 's':
                zustand = 'Snack'
            elif user_input == 'f':
                zustand = feedback

    elif zustand == 'Freizeit':
        zustandsliste.append(zustand)

        #Ausführung Storyline und Spielerfunktion.
        print(random.choice(storyline[11:21]))
        spieler1.rest()
        user_input = input('Optionen: rest (r); grade(g); inspect report(i); exit game(e): ')
        
        # Verarbeitung User-Input.
        if user_input == 'r':
            zustand = 'Freizeit'
        elif user_input == 'i':
            spieler1.inspect_report()
        elif user_input == 'e':
            spieler1.exit()
        elif user_input == 'g':
            pattern = re.compile('Bewertung (1|2)')
            zustandsliste= list(filter(lambda x: pattern.search(x), zustandsliste))
            zustand = zustandsliste[0]
        else: print('Befehl konnte nicht erkannt werden')

    # Restliche Zustände (Snack, Feedback 1, Feedback 2, Evaluation, Niederlage) folgen dem gleichen Muster.

    elif zustand == 'Snack':
        zustandsliste.append(zustand)
        if not Einmalig.einmalige_funktion_ausgefuehrt:
            print(random.choice(storyline[22:25]))
            Einmalig.einmalige_funktion(spieler1.chocolate)
        user_input = input('Optionen: grade(g); inspect report(i); exit game(e): ')
        if user_input == 'g':
            pattern = re.compile('Bewertung (1|2)')
            zustandsliste= list(filter(lambda x: pattern.search(x), zustandsliste))
            zustand = zustandsliste[0]
        elif user_input == 'i':
            spieler1.inspect_report()
            zustand = 'Snack'
        elif user_input == 'e':
            spieler1.exit()
        else: print('Befehl konnte nicht erkannt werden')

    elif zustand == 'Feedback 1':
        zustandsliste = []
        if not bereits_gedruckt:
            print(storyline[79])
            feedback1.Durchführung()
            bereits_gedruckt = True
        if feedback1.ev <= 60:
            zustand = 'Niederlage'
        else:
            Einmalig.einmalige_funktion_ausgefuehrt = False
            user_input = input('Optionen: grade(g); inspect report(i); exit game(e): ')
            if user_input == 'g':
                bereits_gedruckt = False
                zustand = 'Bewertung 2'
            elif user_input == 'i':
                spieler1.inspect_report()
                user_input = input('Optionen: grade(g); exit game(e), continue(tab): ')           
                if user_input == 'g':
                    bereits_gedruckt = False
                    zustand = 'Bewertung 2'
                elif user_input == 'e':
                    spieler1.exit()
            elif user_input == 'e':
                spieler1.exit()
            elif user_input == 'd' or 'delay grade':
                bereits_gedruckt = False
                zustand = 'Feedback 2'
            else: print('Befehl konnte nicht erkannt werden')

    elif zustand == 'Feedback 2':
        if not bereits_gedruckt:
            output = []
            for i, line in enumerate(storyline[81:99]):
                output.append(line)
                if (i) % 4 == 0:
                    output.extend(['\n', '\n'])  
                else:
                    output.append('\n')
            print(''.join(output))
            Feedback2.feedback2()
            bereits_gedruckt = True
        if spieler1._ev == 0:
            bereits_gedruckt = False
            zustand = 'Niederlage'
        user_input = input('Optionen: get eval(t); inspect report(i); exit game(e):')
        if user_input == 't':
            bereits_gedruckt = False
            zustand = 'Evaluation'
        elif user_input == 'i':
            spieler1.inspect_report()
            user_input = input('Optionen: get eval(t); exit game(e); continue(tab):')
            if user_input == 't':
                bereits_gedruckt = False
                zustand = 'Evaluation'
            elif user_input == 'e':
                spieler1.exit()
        elif user_input == 'e':
            spieler1.exit()
        else: print('Befehl konnte nicht erkannt werden')

    elif zustand == 'Evaluation':
        if not bereits_gedruckt:
            if spieler1._ev == 140:
                print('\n\n'.join(storyline[101:103]))
            elif spieler1._ev <= 170:
                print('\n\n'.join(storyline[104:106]))
            elif spieler1._ev <= 200:
                print('\n\n'.join(storyline[107:109]))
        bereits_gedruckt = True
        print('What do you wanna do next?')  
        user_input = input('Optionen: play again(p); inspect report(i); exit game(e): ')
        if user_input == 'p':
            bereits_gedruckt = False
            bereits_gedruckt1 = False
            bereits_gedruckt2 = False
            zustandsliste = []
            spieler1.play_again()
            zustand = 'Start'
        elif user_input == 'i':
            spieler1.inspect_report()
        elif user_input == 'e':
            spieler1.exit()
        else: print('Befehl konnte nicht erkannt werden')

    elif zustand == 'Niederlage':
        if not bereits_gedruckt:
            print('\n\n'.join(storyline[110:]))
            bereits_gedruckt = True
        user_input = input('Optionen: play again(p); inspect report(i); exit game(e): ')
        if user_input == 'p':
            bereits_gedruckt = False
            bereits_gedruckt1 = False
            bereits_gedruckt2 = False
            zustandsliste = []
            spieler1.play_again()
            zustand = 'Start'
        elif user_input == 'i':
            spieler1.inspect_report()
        elif user_input == 'e':
            spieler1.exit()
        else: print('Befehl konnte nicht erkannt werden')