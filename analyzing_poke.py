import requests
import fetch_poke

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    pokemon_data = response.json()
    return pokemon_data

def calculate_average_weight(pokemon_list):
    total_weight = sum([pokemon['weight'] for pokemon in pokemon_list])
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_list = [fetch_pokemon_data(name) for name in pokemon_names]

for pokemon in pokemon_list:
    name = pokemon['name']
    abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
    print(f"Name: {name}")
    print("Abilities:", ", ".join(abilities))
    print()

average_weight = calculate_average_weight(pokemon_list)
print(f"Average Weight: {average_weight}")
