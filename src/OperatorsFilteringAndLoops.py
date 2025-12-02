#This is a simple representation of the operators, 
# how to filter data and looping through different
# data types

#! comparison operators
2<3 #? returns True
"carl" < 'chris' #? returns True

#! boolean operators
2 < 3 and 4 < 5 #? returns True
"carl" < "chris" or 3 >= 4 #? returns True
not 2 > 4 #? returns True
    
#? conditional functions to iterate over arrays
import numpy as np
days = [[1,2,3,4,5,6,7]]
np.logical_and(days > 3, days < 6) #? returns array of boolean values
days[np.logical_and(days > 6, days < 7)] #? returns array of values

#! conditional structures:
#! if condition
z = 8 
if z % 2 == 0: #? simple verification if the condition is met
    print("z is even")
elif z % 2 != 0:
    print("z is odd")
else :
    print("nothing")


#! while loop
error = 50.0 
while error > 1: #? simple iteration while a condition is met
    error = error / 4
    print(error)

#! for loop
heights = [1.2, 4.3, 22, 0.5]
#? iteration over lists
for height in heights: #? printing all elements
    print(height)

for index, height in enumerate(heights):
    print(str(index) + str(height)) #? printing all elements preceded by indexes

#? iterating over string 
for c in "family":
    print(c.capitalize()) #? iteration can be done over strings too

house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
   
#? iterating over list of lists
for index, (room, area) in enumerate(house): #? to get the sublist of elements use a tuple
    print("the " + room + " is " + str(area) + " sqm")

#? iterating over dictionaries
world = {"rom":21.33, "ita":34.52, "gre":2.39}
for key, value in world.items(): #? to iterate over dictionaries use the .items() method
    print(key + " --- " + str(value))

#? iterating over array
for val in bmi:
    print(val)

#? iterating over 2d array
for val in np.nditer(meas): #? to iterate over 2d array use the .nditer() function
    print(val)

brics = pd.read_csv("path/to/brics.csv", index_col = 0)
is_huge = brics["area"] > 8 #? returns Series containing booleans
brics[is_huge] #? returns Series containing int/float/str values
brics[brics["area"]] #? returns Series containing int/float/str values
#? conditional functions to iterate over pandas DataFrames
np.logical_and(brics["area"] > 8, brics["area"] < 10) #? returns boolean Series
brics[np.logical_and(brics["area"] > 8, brics["area"] < 10)] #? returns int/float/str dataframe

for val in brics:
    print(val) #! prints only the column names (NOT RECOMENDED)
#? row lable = lab; row data = row
for lab, row in brics.iterrows(): #? to iterate over data frames use the .iterrows() function
    print(lab) #? returns the ROW LABEL as String 
    print(row) #? returns the ROW DATA as Series (all rows returned)

#! extracting data
for lab, row in brics.iterrows():
    print(lab + ": " + row['capital']) #? returns only a column value for each labeled row

#! inserting data
for lab, row in brics.iterrows():
    #! create series on every iteration (NOT RECOMENDED)
    brics.loc[lab, "name_length"] = len(row["country"])

#?creates and then appends the new column on which is applied a function (RECOMENDED)
brics["name_lenght"] = brics["country"].apply(len) #? ex: apply(str.upper) for string uppercase