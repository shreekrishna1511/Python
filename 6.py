thrust=input("Enter value of thrust?")
mass_flow_rate=input("Enter the value of mass flow rate")
thrust_float=float(thrust)
mass_float=float(mass_flow_rate)
specific_impulse= thrust_float/(mass_float*9.81)
exhaust_velocity= specific_impulse*9.81
print(specific_impulse,exhaust_velocity)