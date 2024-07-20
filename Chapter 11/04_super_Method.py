# Super Method -- > super() method is used to access the method of a super class in the derived class


class one : 
    a = 1

    def __init__(self):
        print("This is class one constructor")


    def top(self) :
        print(F"This is top level class and the value is {self.a}")
    

class two(one) :
    b = 2    

    def __init__(self) :
        print("This is class two constructor")
        super().__init__()

    def middle(self) :
        print(F"This is middle level class and the value is {self.b}")

class three(two) : 
    c = 3
    def __init__(self) :
        print("This is class three constructor")
        super().__init__()

    def lower(self) :
        print(F"This is lower level class and the value is {self.c}")

x = three()
print(x.a, x.b, x.c)




