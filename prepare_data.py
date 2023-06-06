import pandas as pd
from person import Person, Test


def doesExist(persons, id):
    for person in persons:
        if (person.id == id): return person
    return False


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

[print(person.toString()) for person in persons]

