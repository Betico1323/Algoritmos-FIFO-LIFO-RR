class Actividad:
    def __init__(self, id, ti, t):
        self.id = id  
        self.ti = ti  
        self.t = t    
        self.tf = 0   
        self.T = 0    # (T = tf - ti)
        self.E = 0    # (E = T - t)
        self.I = 0    # (I = t / T)



