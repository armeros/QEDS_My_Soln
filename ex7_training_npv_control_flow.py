class training:
    def __init__(self, cost=25_000, r=0.01, added_value=2_500, n_months=0, npv=0.0):
        self.cost, self.r, self.added_value, self.n_months, self.npv = cost, r, added_value, n_months, npv
    
    def train(self):
        while self.npv < self.cost:
            self.npv += self.added_value/(1+self.r)**self.n_months
            print(self.n_months, self.npv)
            self.n_months += 1
            

if __name__=="__main__":            
    w = training()
    w.train()
