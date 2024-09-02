import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    planet_data = []

    for planet in planets:
        if planet['isPlanet']:
            planet_info = {
                'name': planet.get('englishName', 'Unknown'),
                'mass': planet['mass']['massValue'] if planet['mass'] else 'Unknown',
                'orbit_period': planet.get('sideralOrbit', 'Unknown')
            }
            planet_data.append(planet_info)
    return planet_data

planets = fetch_planet_data()

for planet in planets:
    print(f"Planet: {planet['name']}, Mass: {planet['mass']}, Orbit Period: {planet['orbit_period']} days")
