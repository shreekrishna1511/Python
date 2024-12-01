# Dictionary of celestial objects with their luminosities
celestial_objects = {
    "Sirius": 25,
    "Andromeda Galaxy": 1000000,
    "Jupiter": 6.0e-05,
    "Pleiades": 100,
    "Orion Nebula": 10000,
}

# 1. Print out all the names of the celestial bodies using a for loop
print("Names and luminosities of celestial bodies:")
for obj in celestial_objects.items():
    print(obj[0] + ":", obj[1], "solar units")

# 2. Initialize an array variable to contain only the luminosities of the solar objects
import numpy as np
luminosities = np.array(list(celestial_objects.values()))

# 3. Iterate over the luminosities using a while loop
#    Use a conditional to print out all the celestial bodies with a luminosity of less than 200 solar units
print("\nCelestial bodies with luminosity less than 200 solar units:")
index = 0
keys = list(celestial_objects.keys())
while index < len(luminosities):
    if luminosities[index] < 200:
        print(keys[index])
    index += 1
