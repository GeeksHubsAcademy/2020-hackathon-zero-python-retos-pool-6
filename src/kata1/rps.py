from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if player == ai:
        return "Empate!"
    elif player == 'Piedra' and ai == 'Papel':
        return "Perdiste!" 
    elif player == 'Papel' and ai == 'Tijeras':
        return "Perdiste!" 
    elif player == 'Tijeras' and ai == 'Piedra':
        return "Perdiste!" 
    return "Ganaste!"

# Entry Point
def Game():
    player = input("Elige Piedra, Papel, Tijeras: ")
    ai = options[randint(0, 2)]
    
    winner = quienGana(player, ai)
    print(winner)

#Game()