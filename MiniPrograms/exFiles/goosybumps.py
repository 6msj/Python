# Pokemon Interactive Text Game #

def intro():
    print "This is a Pokemon game."
    print "You've arrived in town and met with Professor Oak, he gives you three choices, Bulbasaur (1), Squirtle (2), Charmander (3)."
    print "Which do you choose?"
def trainerName():
    print "What is your name?"
    name = raw_input("> ")
    return name
def starterPokemon():
    choice = raw_input("> ")
    if choice == "1":
        print "You've chosen Bulbasaur."
    elif choice == "2":
        print "You've chosen Squirtle."
    elif choice == "3":
        print "You've chosen Charmander."
    else:
        print "Before you could choose, the Pokemons were stolen and all you have left is a Pikachu."
    return choice
def rival_appears():
    print "Your rival has appeared."
    print "His name is "
    rivalName = raw_input("> ")
    return rivalName





intro() #starts the game
pokemon = starterPokemon() #pokemon will be the choice of trainer
name = trainerName() #users name
rivalName = rival_appears() #rival gets his name here
