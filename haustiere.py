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

x=10
y=11
print (x+y)

stop = False # bool to stop the code, not implemented yet

class pet:
	"This is a class called pet"
	
	noise = "no noise"
	
	def make_noise(self):		# make_noise delivers the noise string of a pet
		"make_noise delivers the noise string of a pet"
		return self.noise


		
class dog(pet):
	"This is a derived class dog from pet"
	
	def __init__(self):
		self.noise = "bark"
	
	#noise = "bark"
	

class cat(pet):
	"This is a derived class cat from pet"
	noise = "miau"
	

class bird(pet):
	"This is a derived class bird from pet"
	noise = "piep"
	

p = pet()		# instantiiert das haustier p

d = dog()		# instantiiert den hund d
c = cat()		# instantiiert die katze c
b = bird()		# instantiiert den vogel b

d.farbe = "gelb"	# weist dem hund d eine farbe zu, die "gelb" ist.

print(d.noise)	# gibt den noise vom hund d aus
print(c.noise)
print(d.farbe)	# gibt die farbe vom hund d aus. per klassendefinition haben hunde aber keine farbe?
print(d.make_noise())
print(c.make_noise())


# main loop
	
#while(True):
	
#	print(d.make_noise)
	
#	if stop == True:
#		break 