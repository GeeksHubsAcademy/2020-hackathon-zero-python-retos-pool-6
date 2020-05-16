from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if player.lower() == ai.lower():
        return "Empate!"
    elif player.lower() == 'piedra' and ai.lower() == 'papel':
        return "Perdiste!" 
    elif player.lower() == 'papel' and ai.lower() == 'tijera':
        return "Perdiste!" 
    elif player.lower() == 'tijera' and ai.lower() == 'piedra':
        return "Perdiste!" 
    return "Ganaste!"

# Entry Point
def Game():
    player = input("Elige Piedra, Papel, Tijeras: ")
    ai = options[randint(0, 2)]
    
    winner = quienGana(player, ai)
    print(winner)

#Game()