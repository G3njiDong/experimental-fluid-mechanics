# Using the data from previous calculation
frequencies = [254.75, 134.93, 45.81]  # Hz
diameter = 0.01  # diameter
velocity = 12.659380  # m/s

# calculate Strouhal number
strouhal_numbers = [f * diameter / velocity for f in frequencies]
print(strouhal_numbers)


velocity = 12.659380  # m/s
diameter = 0.01  # m
# room temperature viscosity
kinematic_viscosity_air = 1.5e-5  # m^2/s

# Renolds number
reynolds_number = (velocity * diameter) / kinematic_viscosity_air
print(reynolds_number)
