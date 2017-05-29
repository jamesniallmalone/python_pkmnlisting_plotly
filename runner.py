import json
from pprint import pprint

from Pokedex import *



json_data = open('pokemon-list.json')

data = json.load(json_data)

listdata = data["list"]

json_data.close()

Pokedex('Kanto', listdata).print_details()
Pokedex('Johto', listdata).print_details()
Pokedex('Hoenn', listdata).print_details()
Pokedex('Sinnoh', listdata).print_details()
Pokedex('Unova', listdata).print_details()
Pokedex('New Unova', listdata).print_details()
Pokedex('Central Kalos', listdata).print_details()
Pokedex('Coastal Kalos', listdata).print_details()
Pokedex('Mountain Kalos', listdata).print_details()
Pokedex('Alola', listdata).print_details()
Pokedex('Melemele Alola', listdata).print_details()
Pokedex('Akala Alola', listdata).print_details()
Pokedex('Ulaula Alola', listdata).print_details()
Pokedex('Poni Alola', listdata).print_details()