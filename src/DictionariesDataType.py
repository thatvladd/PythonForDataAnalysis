#This is a simple representation of the Dictionary and DataFrame data types
# and what you can do with them.

#DICTIONARIES
#? key-value pairs
world = {"rom":21.33,
         "ita":34.52, 
         "gre":2.39}
world["ita"] #? returns the value based on key

world.keys()  #? returns the keys 
print(world.values()) #? returns the values
world["sealand"] = 0.0000027 #? insert new pair
"sealand" in world #? check key presence
world["sealand"] = 0.0000028 #? updating a value
del(world["sealand"]) #? deleting entry 

#TODO: list vs dict
#?use list where you need to use a collection of values where the order matters for selecting entire subsets
#?use dict where you need a lookup table where looking for data should be fast and where you can specify unique keys

#! Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

europe["france"]["capital"] #? access value from internal dictionary

#! PANDAS - DataFrame 
#? tabular form stored in dataframe
#? rows contain observations (different info about smth) and columns represent variables
dict = {"country": ["Romania", "Polonia", "Austria"],
        "capital": ["Bucuresti", "Cracovia", "Viena"],
        "area": [8.234, 2.345, 9.42], 
        "population": [19.08, 2349, 754.43]}
import pandas as pd #? importing pandas
brics = pd.DataFrame(dict) #? creating a DataFrame from Dictionary
brics.index = ["RO", "PL", "AU"] #? change vertical indexes from 0|1|2 to labels
brics = pd.read_csv("path/to/brics.csv") #? creating DataFrame from CSV files  
brics = pd.read_csv("path/to/brics.csv", index_col = 0) #? creating DataFrame from CSV files with index on first row

#! subsetting
brics["country"] #? returns an entire column called Series
brics[["country"]] #? DataFrame with one column - sub dataframe
brics[["country", "capital"]] #? DataFrame two columns - sub dataframe

brics[1:3] #? returns DataFrame from first to third excluding third

#! label-based identification (loc)
brics.loc["RU"] #? returns a Series using first row 

#          [rows, columns]
brics.loc[["RU", "CH", "IN"]] #? returns DF of rows using labels
brics.loc[["RU"], ["country", "capital"]] #? returns DF of rows, based on columns using labels
brics.loc[:, ["country", "capital"]] #? returns DF of columns from all rows using slicing and labels

#! integer position-based identification (iloc)
brics.iloc[1] #? returns Series
brics.iloc[[1,2,3]] #? returns DF of rows using indexes 
brics.iloc[[1,2,3], [0,1]] #? 3? returns DF of rows, based on columns using indexes
brics.iloc[:, [0,1]] #? returns DF of columns, from all rows using slicing and indexes