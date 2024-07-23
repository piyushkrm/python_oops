'''Question 1 : Create a class (2-D vector) and use it to create another class representing a 3-D vector.'''

class twoDVector : 
    def __init__(self, p, q) :
        self.p = p
        self.q = q

    def show(self) :
        print(f"The 2-D vector is {self.p}p + {self.q}q")


class threeDVector(twoDVector) :
    def __init__(self, p, q, r):
        super().__init__(p, q)    
        self.r = r

    def show(self) :
        print(f"The 3-D vector is {self.p}p + {self.q}q + {self.r}r")

vec = twoDVector(10, 20)
vec.show()

vc = threeDVector(45, 20, 56)
vc.show()