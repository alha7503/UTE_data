import pandas as pd
from person import Person

p1 = Person(34)
print(p1)

df = pd.read_csv("data.csv")
df = df.drop(columns = ["Unnamed: 21", "Unnamed: 12", "Unnamed: 25"])



for column in df:
    print("'" + column + "'")