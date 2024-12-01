mission_duration = 10  # Duration of the mission in hours
fuel_level = 1000  # Initial fuel level in gallons
distance_to_destination = 500000  # Distance to the destination in kilometers
mission_time = 0  # Initialize mission time
fuel_consumption_rate = 50  # gallons per hour
distance_traveled_per_hour = 50000  # kilometers per hour

i=1
while mission_time >= mission_duration:
     distance_to_destination =distance_to_destination-distance_traveled_per_hour
     fuel_level=fuel_level-fuel_consumption_rate
     print(fuel_level,mission_time,fuel_level)
     if fuel_level<=0:
         break
         i=i+1
