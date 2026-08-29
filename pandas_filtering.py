#FILTERING is keeping the rows that match the condition

import pandas as pd

df=pd.read_csv("sample.csv")

tall_pokemon =df[df["Height"] >=1] # here we print the data's who's heigh>=1
heavy_pokemon=df[df["Weight"]>=5] # here we print the data's who's weight>=5
print(heavy_pokemon)

#this prints  the pokemon that is legendary 
legendary_pokemon=df[df["Legendary"]==1] #instead of 1 we can also give True
print(legendary_pokemon)

water_pokemon=df[(df["Type1"]=="Water") | (df["Type1"]=="Water")]
print(water_pokemon)
# here | is 'or' operator we can also use & "and" operation