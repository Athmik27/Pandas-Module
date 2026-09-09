# Write Pandas code to display only the Pokémon whose Weight is greater than 0.5
import pandas as pd

# df = pd.read_csv("sample.csv")
# heavy_pokemon=df[df[('Weight')]>50]
# print(heavy_pokemon)

# Display Pokémon whose Height is greater than 1 AND Weight is greater than 50
# df = pd.read_csv("sample.csv")
# pokemon_select = df[(df["Height"] > 1) & (df["Weight"] > 50)]
# print(pokemon_select)

# Syntax: df[(df["Column1"] > value) & (df["Column2"] > value)]

# Display all Pokémon whose Type1 is either "Fire" OR "Water".
# df = pd.read_csv("sample.csv")
# pokemon_select = df[(df["Type1"] == 'Fire') | (df["Type1"] == 'Water')]
# print(pokemon_select)

#  Display the 5 heaviest Pokémon, with the heaviest one appearing first very imp
# df = pd.read_csv("sample.csv")
# print(df.sort_values("Weight", ascending=False).head(5))

# Find the average Weight of Pokémon for each Type1.
# df = pd.read_csv("sample.csv")
# group=(df.groupby("Type1"))
# print(group['Weight'].mean())

# # Find how many Pokémon belong to each Type1
# df=pd.read_csv("sample.csv")
# print(df["Type1"].value_counts())

# Find the maximum Weight among all Pokémon.
