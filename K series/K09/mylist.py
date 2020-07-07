class mylist(list):
    def product(self):
        res = 1
        for i in self:
            res *= i
        return res
    def __add__(self,other):
        res = mylist()
        if(len(self) != len(other)):
            raise ValueError
        for i,j in zip(self,other):
            res.append(i+j)
        return res
    def __mul__(self,other):
        res = mylist()
        if(len(self) != len(other)):
            raise ValueError
        for i,j in zip(self,other):
            res.append(i*j)
        return sum(res)

        
        
