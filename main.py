import requests
import random
import time
from pprint import pprint

print(" ____________________________________ ")
print("|                                    |")
print("|         Pokemon Top Trumps         |")
print("|____________________________________|")
print("")
print("Welcome to Top Trumps, Pokemon Edition")


def random_characters():
    pokemon_number = random.randint(1, 151)
    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon_number)
    response = requests.get(url)
    # if response != 200:
    #     quit()
    # else:
    #     print(response)
    pokemon = response.json()
    # print(pokemon['name'])
    # print(pokemon['id'])
    # print(pokemon['height'])
    # print(pokemon['weight'])

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
    }


def run():
    my_pokemon = random_characters()
    print("you were given {} ".format(my_pokemon['name']))
    opponent_pokemon = random_characters()
    stat_choice = input("Which stat would you like to use? [id, height, weight?]")
    print("They were given {} ".format(opponent_pokemon['name']))

    myStats = my_pokemon[stat_choice]
    opStats = opponent_pokemon[stat_choice]
    print("The op stats are {}".format(opStats))
    print("Your stats stats are {}".format(myStats))

    if myStats > opStats:
        print("You win!")
    elif myStats < opStats:
        print("You lose!")
    else:
        print("It's a draw!")

run()
time.sleep(5)

print("Bye now!")
