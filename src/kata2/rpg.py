#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    password = ""
    #Generamos la contraseña
    # Caracteres Ascii de 33 al 126
    for x in range(passLen):
        password += chr(random.randint(33,126))
    
    return password

print(RandomPasswordGenerator())