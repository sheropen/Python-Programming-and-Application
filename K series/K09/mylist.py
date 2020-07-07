class mylist(list):
    def product(self):
        res = self[0]
        for i in self[1:]:
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

        
        
