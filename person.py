class Person:
    def __init__(self, id, gruppe, alter, uhrzeit, datum, vorerfahrung, stimmung, aufnahmefähigkeit, stresslevel, place, noise, test):
        self.id = id
        self.gruppe = gruppe
        self.alter = alter
        self.uhrzeit = uhrzeit
        self.datum = datum
        self.vorerfahrung = vorerfahrung
        self.stimmung = stimmung
        self.aufnahmefähigkeit = aufnahmefähigkeit
        self.stresslevel = stresslevel
        self.place = place
        self.noise = noise
        self.original = None
        self.prototyp = None
        if (test.type == "O"): self.original = test
        else: self.prototyp = test

    def addTest(self, test):
        if(test.type == "O"): self.original = test
        elif(test.type == "P"): self.prototyp = test
    
    def toString(self):
        return self.id, self.gruppe, self.vorerfahrung, self.vorerfahrung, self.place
        

class Test:
    def __init__(self, type, t_values, t_clicks, q_scores):
        self.type = type
        self.t_values = t_values
        self.t_clicks = t_clicks
        self.q_scores = q_scores

    def toString(self):
        return "t-values", self.t_values, "t_clicks", self.t_clicks, "q_scores", self.q_scores
  