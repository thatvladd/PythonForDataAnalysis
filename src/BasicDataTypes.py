#This is a simple exemplification of what basic data types we have
# are in python (that are used in data analysis) and what you can
# do with them

height = 1.79 #? float
string = "test" #? string 
string1 = 'test' #?string
number = 282 #? int
verify = True #? boolean

type(height) #? variable type
str(number) #? convert to string
int(height) #? convert to int
bool(1) #? convert to boolean
float(282) #? convert to float

#!LISTS
listOfInts = [1,2,3,4,5] #? list
#! subsetting
listOfInts[3] #? returns 4th value
listOfInts[-1] #? returns last value
listOfInts[1:4] #? returns values from 1 to 4
listOfInts[:4] #? returns values from 0 to 4
listOfInts[3:] #? returns values from 3 to last
listOfInts[:] #? returns all values from list

listOfLists = [["dad", 180], 
               ["brother", 168]] #? list of lists
#! subsetting
listOfLists[1][1] #? returns element 6
#* all subsetting methods work the same

#! manipulation
listOfInts[3] = 99 #? changing values
new_element = listOfLists + ["me", 174] #? adding values
# del listOfLists[1] #? deleting values

#! create new independent list
new_list = list(listOfInts) #? changes on new_list will not affect listOfInts
new_list1 = listOfLists[:] #? changes on new_list1 will not affect listOfLists

#! Built-In functions
max(listOfInts) #? returns the max value from list
round(1.68, 1) #? = 1.7 #rounds to one decimal place
round(1.68) #? = 2 #rounds to the nearast
#help(pow) #? get info on function

#TODO - more built-in functions https://docs.python.org/3/library/functions.html

#! Object methods
listOfLists.index(["dad",180]) #? returns index of the value from list
"mom".index("o") #? returns index of first appearance
listOfLists.count(['dad',180]) #? returns number of occurances
"python".capitalize() #? capitalizes string
listOfInts.remove(1) #? removes first occurence of value
print("string".replace("str", "do")) #? replaces parts of string
# help(str)