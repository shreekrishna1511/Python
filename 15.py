import numpy as np
import pandas as pd
planet_distances = {
    'Mercury': 57.9,
    'Venus': 108.2,
    'Earth': 149.6,
    'Mars': 227.9,
    'Jupiter': 778.6,
    'Saturn': 1433.5,
    'Uranus': 2872.5,
    'Neptune': 4495.1,
    'Pluto': 5906.4
}

moon_data = {
    'Planet': ['Jupiter', 'Jupiter', 'Saturn', 'Saturn', 'Uranus', 'Neptune'],
    'Moon': ['Io', 'Ganymede', 'Titan', 'Rhea', 'Titania', 'Triton'],
    'Diameter (km)': [3642, 5262, 5150, 1528, 1578, 2707],
    'Orbital Period (days)': [1.77, 7.15, 15.95, 4.52, 8.71, 5.88]}
series=pd.Series(planet_distances)
df=pd.DataFrame(moon_data)

print(series)
print(df)