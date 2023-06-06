import pandas as pd
import csv
from person import Person, Test


def doesExist(persons, id):
    for person in persons:
        if (person.id == id): return person
    return False

def list2String(list):
    res = ""
    for entry in list:
        if(isinstance(entry, float)):
            res += str(entry) + ", "
        else:
            res += entry


df = pd.read_csv("data.csv")
df = df.drop(columns = ["Unnamed: 21", "Unnamed: 12", "Unnamed: 25"])

persons = []
for index, row in df.iterrows():
    ## Testergebnis erstellen
    t_values = [row["T1"], row["T2"], row["T3"], row["T4"]]
    t_clicks = [row["T1Klicks"], row["T2Klicks"], row["T3Klicks"], row["T4Klicks"]]
    q_scores = [row["Q1"], row["Q2"], row["Q3"]]
    test = Test(row["System(P/O)"], t_values, t_clicks, q_scores)
    
    
    #schauen, ob Person mit ID existiert
    if(doesExist(persons, row["ID (auf Zettel)"])):
        person = doesExist(persons, row["ID (auf Zettel)"])
        person.addTest(test)
    else:
        person = Person(row["ID (auf Zettel)"], row["Gruppe(PO/OP)"], row["Alter"], row["Uhrzeit"], row["Datum"], row["Vorerfahrung"], row["Stimmung"], row["Aufnahmefähigkeit"], row["Stresslevel"], row["inside/outside(i/o)"], row["Umgebungsgeräusche"], test)
        persons.append(person)

csv1 = [", ".join(person.toCsv1()) for person in persons]
csv1 = [entry.replace("nan,", ",").split(", ") for entry in csv1]
[print(entry) for entry in csv1]

with open ("data1.csv", "w", newline="") as file1:
    writer = csv.writer(file1)
    writer.writerow("ID, Gruppe, Alter, Zeit, Datum, Erfahrung, Stimmung, Aufnahmefähigkeit, Stress, Ort, Noise, OT1, OT2, OT3, OT4, OK1, OK2, OK3, OK4, OQ1, OQ2, OQ3, PT1, PT2, PT3, PT4, PK1, PK2, PK3, PK4, PQ1, PQ2, PQ3".split(", "))
    for entry in csv1:
        writer.writerow(entry)






