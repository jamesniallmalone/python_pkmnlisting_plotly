import json
from pprint import pprint

from Pokedex import *



json_data = open('pokemon-list.json')

data = json.load(json_data)

listdata = data["list"]

json_data.close()

Pokedex('Kanto', listdata).print_details_to_file()
Pokedex('Johto', listdata).print_details_to_file()
Pokedex('Hoenn', listdata).print_details_to_file()
Pokedex('Sinnoh', listdata).print_details_to_file()
Pokedex('Unova', listdata).print_details_to_file()
Pokedex('New Unova', listdata).print_details_to_file()
Pokedex('Central Kalos', listdata).print_details_to_file()
Pokedex('Coastal Kalos', listdata).print_details_to_file()
Pokedex('Mountain Kalos', listdata).print_details_to_file()
Pokedex('Alola', listdata).print_details_to_file()
Pokedex('Melemele Alola', listdata).print_details_to_file()
Pokedex('Akala Alola', listdata).print_details_to_file()
Pokedex('Ulaula Alola', listdata).print_details_to_file()
Pokedex('Poni Alola', listdata).print_details_to_file()