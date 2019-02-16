# Dependencies
import matplotlib.pyplot as plt
from stats import median
import numpy as np

### Data Points
arr = np.array([2.3, 10.2,11.2, 12.3, 14.5, 14.6, 15.0, 15.1, 19.0, 24.0])
arr

# Find the median
median(arr)

# Use numpy to create quartiles
q0 = np.quantile(arr,0)
q1 = np.quantile(arr,.25)
q2 = np.quantile(arr,.5)
q3 = np.quantile(arr,.75)
q4 = np.quantile(arr,1)

# Print the quartiles
print(q0)
print(q1)
print(q2)
print(q3)
print(q4)

# Calculate the interquartile range
iqr = q3-q1
iqr

# Find lower boundary
low = q1 - 1.5 * iqr

# Find upper boundary
upper = q3 + 1.5 * iqr

# Check for any lower outliers
for num in arr:
    if num <= low:
        print(str(num) + " lower")
    elif num <= upper:
        print(str(num)+ " upper")
