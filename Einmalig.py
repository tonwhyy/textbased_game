'''
Tony Baude
18.08.23

Dieses Dokument enthält eine globale Variable und eine Funktion zur einmaligen Ausführung einer Funktion.
Folgende Variablen/Funktionen sind enthalten:
    - einmalige_funktion_ausgefuehrt (bool):
            Wenn False, wurde die Funktion noch nicht ausgeführt.
            Wenn True wurde die Funktion bereits ausgeführt.
    - einmalige_funktion (func): Gegebene Funktion wird durch diese nur einmal ausgeführt.
'''

einmalige_funktion_ausgefuehrt = False

def einmalige_funktion(func):
    '''
    Gegebene Funktion wird durch diese nur einmal ausgeführt.
    
    Parameters: 
        func (func): Eine  bereits existierende Funktion.

    Returns:
        func or str: Die Funktion wird ausgeführt oder eine Nachricht, bei bereits ausgeführter Funktion, wird ausgegeben.
    '''
    global einmalige_funktion_ausgefuehrt
    if not einmalige_funktion_ausgefuehrt:
        print('Aktion wird einmal ausgeführt')
        func()
        einmalige_funktion_ausgefuehrt = True
    else:
        print('Aktion wurde bereits einmal ausgeführt!')