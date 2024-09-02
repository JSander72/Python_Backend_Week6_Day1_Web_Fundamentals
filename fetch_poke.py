import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    pokemon_data = response.json()
    return pokemon_data

pokemon = fetch_pokemon_data("pikachu")
name = pokemon['name']
abilities = [ability['ability']['name'] for ability in pokemon['abilities']]

print(f"Name: {name}")
print("Abilities:", ", ".join(abilities))
