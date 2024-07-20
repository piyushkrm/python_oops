# Multilevel Inheritance

class Programmer:
    language = "JavaScript"
    salary = 4500000
    def show(self) :
        print(f"The programmer is used {self.language} to develop the software and the salary is {self.salary}")


class Coder(Programmer) :
    language = "Java"
    def lan(self) : 
        print(f"The coder use languages is {self.language}")


class Customer(Coder) :           
    name = "Piyush"
    def info(self) :
        self.lan()
        self.show()
        print(f"The customer is {self.name}")

# cus = Customer()
# cus.info()

# Another one and this is shortcut to undestand the multilevel inheritance

class one : 
    a = 1

class two(one) :
    b = 2

class three(two) : 
    c = 3

x = three()
print(x.a, x.b, x.c)




