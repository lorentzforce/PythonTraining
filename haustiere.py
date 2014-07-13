'''import sys
import os
def restart_program():
	"""Restarts the current program. 
	Note: this function does not return. Any cleanup action (like
	saving data) must be done before calling this function."""
	python = sys.executable
	os.execl(python, python, * sys.argv)

if __name__ == "__main__":
	answer = raw_input("Do you want to restart this program ? ")
	if answer.lower().strip() in "y yes".split():
		restart_program()'''

# Sagenumwobenes Haustier-Beispiel von BSW

class pet:
	"This is a class called pet"
	
	# noise = "no noise" # Variablen braucht man hier nur, wenn er sich daten merken muss. die methode merkt sich nix.
	
	def make_noise(self):		
		"make_noise delivers the noise string of the pet"
		return "no noise" # self.noise	
		
	def get_nr_legs(self):		
		"get_nr_legs delivers the number of legs of the pet"
		return "no legs"

		
class dog(pet):
	"This is a derived class dog from pet"
	
	# def __init__(self): # Variablen koennen mit der Spezialvariablen __init__ bei der instanziierung auf einen defaultwert initiiert werden.
		# self.noise = "bark"
		
	def make_noise(self):		# make_noise delivers the noise string of a pet
		"make_noise delivers the noise string of a pet"
		return "bark" # self.noise
	
class cat(pet):
	"This is a derived class cat from pet"
	
	def make_noise(self):		# make_noise delivers the noise string of a pet
		"make_noise delivers the noise string of a pet"
		return "miau" # self.noise
	
class bird(pet):
	"This is a derived class bird from pet"
	
	def make_noise(self):		# make_noise delivers the noise string of a pet
		"make_noise delivers the noise string of a pet"
		return "piep" # self.noise
	
class spider(pet):
	"This is a derived class spider from pet"
	
	def get_nr_legs(self):		
		"get_nr_legs delivers the number of legs of the pet"
		return 8
	
d = dog()		# instantiiert den hund d
c = cat()		# instantiiert die katze c
b = bird()		# instantiiert den vogel b
dd = dog()
cc = cat()
bb = bird()
sp = spider()


d.farbe = "gelb"	# weist dem hund d eine farbe zu, die "gelb" ist.

print(d.make_noise())				# gibt den noise vom hund d aus
print(d.farbe)				# gibt die farbe vom hund d aus. per klassendefinition haben hunde aber keine farbe?
print(bb.get_nr_legs())
print(sp.get_nr_legs())

petlist = [d, c, b, dd, cc, bb, sp]

index = 0	# index fuer spaetere indizierung der pet liste
index = int(raw_input('Enter index of petlist:'))
toprint = pet()				# toprint muesste jetzt ein objekt der klasse pet sein
toprint = petlist[index] 	# toprint wird mit dem objekt aus index ueberschrieben
print(toprint.make_noise()) # gibt den gewuenschten noise von dem objekt der petliste aus

# main loop
textbuffer = "empty"
petnumber = 0 # petnumber soll index +1 sein, damit man nicht pet nr. 0 eingeben muss.
	
while(True):
	
	textbuffer = raw_input("Enter the pet-number (to stop press 's'):")
	
	if textbuffer == "s":
		stop = True		# obsolete
		break

	elif textbuffer.isdigit(): # isnumeric() ist nur for unicode. isdigit() geht. beide erkennen keine negativen zahlen!
		
		petnumber = int(textbuffer)
			
		if petnumber <= len(petlist):
			if petnumber <= 0:
				print("you entered zero or a negative number")
			else:
				print (petnumber)
				index = petnumber-1
				toprint = petlist[index] 	#toprint wird mit dem objekt aus index ueberschrieben
				print(toprint.__class__.__name__)
				print(toprint.make_noise())
		else:
			print("you entered a value bigger than the number of pets")
			print("there are only " + str(len(petlist)))

	elif len(textbuffer) >= 2:
		if bool(textbuffer[0] == "-"): # bool() konvertiert den inhalt zum typ bool
			if textbuffer[1:].isdigit(): # mit der slice [1:] erhalten wir den string bis zum ende, ausser den ersten character
				print("you entered a negative number") #
			else:
				print("you entered a minus sign and not a integer number afterwards")
		else:
			print("you entered two or more characters which are not a number")

	else:
		print("you entered a single character which is not a number")