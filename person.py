import math
class Person:
    def __init__(self, id, gruppe, alter, uhrzeit, datum, vorerfahrung, stimmung, aufnahmefähigkeit, stresslevel, place, noise, test):
        self.id = id
        if(gruppe == "OP"): self.gruppe = 0
        else: self.gruppe = 1
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
        #return self.id, self.gruppe, self.vorerfahrung, self.vorerfahrung, self.place
        res = []
        for key, value in vars(self).items():
            if isinstance(value, Test):
                t_string = [str(v) for k, v in vars(value).items()]
                res.append(", ".join(t_string))
            else:
                res.append(str(value))
        return res
    
    def toCsv1(self):
        #return self.id, self.gruppe, self.vorerfahrung, self.vorerfahrung, self.place
        res = []
        for key, value in vars(self).items():
            if isinstance(value, Test):
                test = [v for k, v in vars(value).items()]
                for entry in test:
                    #nur t_values, t_klicks, q_scores --> Listen
                    if(isinstance(entry, list)):
                        #nur für t_values, t_clicks
                        if(isinstance(entry[0], float)): 
                            for val in entry:
                                if(not math.isnan(val)):
                                    res.append(str(int(val)))
                                else: res.append(str(val))
                        else: [res.append(str(val)) for val in entry]
                    
            else:
                if(isinstance(value, float)): 
                    if(not math.isnan(value)): 
                        res.append(str(int(value)))
                else: res.append(str(value))
        return res
    
    
    ##Klicks, Q-Scores usw...zusammenfassen
        

class Test:
    def __init__(self, type, t_values, t_clicks, q_scores):
        self.type = type
        self.t_values = t_values
        self.t_clicks = t_clicks
        self.q_scores = q_scores

    def toString(self):
        return "t-values", self.t_values, "t_clicks", self.t_clicks, "q_scores", self.q_scores
  