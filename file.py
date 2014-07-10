

# Main loop ----------------------------------------------------------------

#print "mainloop.."
#while(True):

print "this is python"

# new class
class Roboter():   # (Oberklasse 1, Oberklasse 2):
    "Doc von Roboter, make it your habit"
    pass            # pass bedeutet nix, ist nur Platzhalter

if __name__ == "__main__": # when this code is in main, the special variable __name__ will have the value "__main__". If this file is being imported from another module, __name__ will be set to the module's name. It's done so that code is only executed when run as a script and not when you import the module.

    x = Roboter()   # x ist nun ein Roboter
    y = Roboter()   # y ist auch ein Roboter
    y2 = y          # y2 ist nur eine Referenz auf y, was ein Roboter ist.
    print(y == y2) # man sieht, mit y und y2 ist das gleiche objekt gemeint
    print(y == x)  # x und y sind unterschiedliche objekte

    # x.name = input("Geben Sie den Roboter Namen ein: ")

print(x.__doc__)    # prints the Documentaiton string of the Robot class
                    # the __doc__ is meta-data
