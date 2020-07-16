import numpy as np
class bond:
    def __init__(self, C=5, M=100, i=0.03):
        self.C, self.M, self.i = C, M, i
        
    def __str__(self):
        return f'Coupon payment = {self.C}, Face value = {self.M}, and Yield to aturity = {i}'
    
    def pricing_loop(self, n):
        C, M, i = self.C, self.M, self.i
        payment = 0
        for j in range(1, n+1):
            payment += C/(1+i)**j
        payment += M/(1+i)**n
        return payment
    
    def pricing_formula(self, n):
        C, M, i = self.C, self.M, self.i
        return C*(1-(1+i)**(-n))/i +M*(1+i)**-n
    
if __name__=="__main__":
    b = bond()
    N = [b.pricing_loop(n) for n in np.arange(1,11)]
