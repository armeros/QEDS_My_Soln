class HK:
    def __init__(self, y2=50_000, y1=40_000, r=0.05,T=40, tution=5_000) :
        self.r, self.y1, self.y2, self.T, self.tuition = r, y1, y2, T, tution
        
    def worknow(self):
        return sum((self.y1)/(1+self.r)**t for t in range(self.T))
    
    def worklater(self):
        return sum((self.y2)/(1+self.r)**t for t in range(self.T))-sum((self.tuition)/(1+self.r)**t for t in range(4))
    
if __name__=="__main__"            
    student = HK()
    print(student.worknow())
    print(student.worklater())
