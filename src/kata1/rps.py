from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if player == ai:
        return "Empate!"
    elif player == 'piedra' and ai == 'papel':
        return "Perdiste!" 
    elif player == 'papel' and ai == 'tijera':
        return "Perdiste!" 
    elif player == 'tijera' and ai == 'piedra':
        return "Perdiste!" 
    return "Ganaste!"

# Entry Point
def Game():
    player = input("Elige Piedra, Papel, Tijeras: ").lower()
    ai = options[randint(0, 2)].lower()
    
    winner = quienGana(player, ai)
    print(winner)

Game()