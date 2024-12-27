import numpy as np
time=np.arange(0, 101, 1)
altitude=100*time
velocity1=np.divide(altitude,time)
velocity=np.multiply(velocity1,100)


acceleration=np.multiply(velocity1,9.81)

print("The time array shape",time.shape, "Data Type ", time.dtype)
print("The altitude array shape",altitude.shape, "Data Type ", altitude.dtype)
print("The velocity array shape",velocity.shape, "Data Type ", velocity.dtype)
print("The acceleration array shape",acceleration.shape, "Data Type ", acceleration.dtype)