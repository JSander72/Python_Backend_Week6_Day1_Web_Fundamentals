import fetch_planet 
import requests
from fetch_planet import planets

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda p: p['mass'] if p['mass'] != 'Unknown' else 0)
    return heaviest_planet['name'], heaviest_planet['mass']

# Assuming 'planets' is a list of planet dictionaries
planets = [{'name': 'Earth', 'mass': '5.972e24'}, {'name': 'Mars', 'mass': '6.4171e23'}, {'name': 'Jupiter', 'mass': '1.8982e27'}]
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")
