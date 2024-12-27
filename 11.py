
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
orbital_periods =[0.24, 0.62, 1.0, 1.88, 11.86, 29.46, 84.01, 164.8]
axial_tilts =[0.03, 177.36, 23.44, 25.19, 3.13, 26.73, 82.23, 28.32]


file = open("Orbital_details.txt","w")

for i in range(len(planet_names)):
    file.write(planet_names[i] + " ")
    file.write("Orbital Periods : " + str(orbital_periods[i]) + " ")
    file.write("Axial Tilts: " + str(axial_tilts[i]) + " \n")
file.close()