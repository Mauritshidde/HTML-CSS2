import random

menu = '''
_________________________________________________________
| typ . om een woordenlijst te bekijken.                |
| typ . om een nieuwe woorden lijst te maken.           |
| typ . om van woordenlijst te veranderen.              |
| typ . om woorden toe te voegen aan de woordenlijst.   |
| typ . om een woordenlijst naar keuze te overhoren.    |
| typ . om het overhoor programma te stoppen            |
|_______________________________________________________|
'''

def print_menu():
    print(menu)

def input_gebruiker():
	print_menu()
	return input()

def runner_code():
	menu_keuze = input_gebruiker()
	if menu_keuze == "1":
		print("")
	elif menu_keuze == "2":
		print("")
	elif menu_keuze == "3":
		print("")
	elif menu_keuze == "4":
		print("")
	else:
		print("")

	wil_je_doorgaan = input("Druk q om te stoppen of druk y om doortegaan ")
	if wil_je_doorgaan == "q":
		print("doei")
	else:
		print("Nog een keer ")
		runner_code()
