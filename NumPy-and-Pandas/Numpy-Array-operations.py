# Numpy Array Operations:
# 1. Create a 1D NumPy Array:
import numpy as np;
temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])
print(temperatures_w1)
# 2. Inspection and Properties:
Shape = temperatures_w1.shape
print("Shape of the array:", Shape)
Size = temperatures_w1.size 
print("Size of the array:", Size)
data_type = temperatures_w1.dtype
print("Data type of the array:", data_type)
# 3. Array Operations:
Fahrenheit = (temperatures_w1 * 9/5) + 32
print("Temperatures in Fahrenheit:", Fahrenheit)
Mean_temp = np.mean(temperatures_w1)
print("Mean temperature:", Mean_temp)   
max_temp = np.max(temperatures_w1)
print("Maximum temperature:", max_temp)
min_temp = np.min(temperatures_w1)
print("Minimum temperature:", min_temp)
# 4. Array Slicing and Indexing:
# Extract the temperatures for the first three days of the week.
first_three_days = temperatures_w1[:3]
print("Temperatures for the first three days:", first_three_days)
# Extract the temperatures for the weekend (last two days).
weekend_temps = temperatures_w1[-2:]
print("Temperatures for the weekend:", weekend_temps)
#  Extract the temperatures for the middle three days of the week.
middle_three_days = temperatures_w1[2:5]
print("Temperatures for the middle three days:", middle_three_days)
# 5. Create a 2D Array:
temperatures = np.array([[22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9], [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]])
print("2D Array of temperatures:\n", temperatures)
# 6. Inspect and Slice the 2D Array:
shape_2d = temperatures.shape
print("Shape of the 2D array:", shape_2d)
data_type_2d = temperatures.dtype
print("Data type of the 2D array:", data_type_2d)
size_2d = temperatures.size
print("Size of the 2D array:", size_2d)
# Extract the temperatures for each week and the weekends (last two days) for both weeks.
week1_temps = temperatures[0, :3]
week2_temps = temperatures[1, :3]
weekend_week1 = temperatures[0, -2:]
weekend_week2 = temperatures[1, -2:]
print("Temperatures for the first week (first three days):", week1_temps)
print("Temperatures for the second week (first three days):", week2_temps)
print("Temperatures for the first week (weekend):", weekend_week1)
print("Temperatures for the second week (weekend):", weekend_week2)