import csv
import pandas as pd

df = pd.read_csv('dwarf_star.csv')

df["Mass"] = pd.to_numeric(df["Mass"], downcast="float")
df["Radius"] = pd.to_numeric(df["Radius"], downcast="float")

df["Radius"] = df["Radius"]*0.102763
df["Mass"] = df["Mass"]*0.000954588

df = df.rename({
    "Radius":"solar_radius",
    "Mass":"solar_mass",
    "name":"Star_name",
}, axis='columns')

del df['Unnamed: 0']
df.to_csv('new_dwarf.csv', index = True)