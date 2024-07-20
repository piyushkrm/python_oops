'''
Operators in Python can be overloaded using dunder methods.

These methods are called when a given operator is used on the objects.

Operators in Python can be overloaded using the following methods:
'''

class number:
    def __init__(self, n) :
        self.n = n


    def __add__(self, num) :
        return self.n + num.n
    
    def __sub__(self, num) :
        return self.n - num.n
        
    def __mul__(self, num) :
        return self.n * num.n
    
    def __truediv__(self, num) :
        return self.n / num.n
    
    def __floordiv__(self, num) :
        return self.n // num.n
        
'''
p1+p2 # p1 ._ add_(p2)
p1-p2 # p1 ._ sub_(p2)
p1*p2 # p1 ._ mul_(p2)
p1/p2 # p1. truediv_(p2)
p1//p2 # p1. floordiv_(p2)
'''



n = number(10)
m = number(10)

print(n + m)
print(n - m)
print(n * m)
print(n / m)
print(n // m)