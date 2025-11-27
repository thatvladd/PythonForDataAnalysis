# This is a simple representation of what is an array and how to use it

#! NumPy array
import numpy as np #? importing numpy
#from numpy import array #? importing specific subpackage 

np.array([1,2,23,3]) #? create array
#array([1,1,1,1]) #? create array (for basic use cases)

weight = [1,2,2,34,5] # list
height = [123,532,123,431,234] # list
np_weight = np.array(weight) #? converting list to array
np_height = np.array(height) 
bmi = np_weight / np_height ** 2 #? performing operations on arrays (a[i] / b[i] ** 2)

#! subsetting
bmi > 23 #? return a list of boolean values
bmi[bmi > 23] #? returns the element that match the criteria
bmi[2] #? returns the corresponding value
bmi[2:4] #? returns a subarray

#! Array 2D
np_2d = np.array([[1,1,2],[5,6,7]]) #? creating 2d array with 2 rows and 3 cols
np_2d.shape #? attribute that gives info: (2 rows, 5 cols)
np_2d[0] #? returns first row
np_2d[0][2] #? returns specific value
np_2d[0,2] #? returns specific value 
np_2d[:, 1:3] #? returns specific cols from all rows 
np_2d[1, :] #? returns first row from all columns

#! np functions
family = np.array([180, 53.5], 
                  [178, 45.3])
np.mean(family[:, 0]) #? returns mean (avg height) of height column
np.median(family[:, 0]) #? return the middle if you sort from small to tall
np.corrcoef(family[:, 0], family[:, 1]) #? returns data that shows if height and weight are corelated
np.std(family[:, 0]) #? returns the standard deviation

