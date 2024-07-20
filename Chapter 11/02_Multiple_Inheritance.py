# Multiple Inheritance

class Employee:
    company = "ITC"
    salary = 4500000
    def show(self) :
        print(f"The name is the company is {self.company} and the salary is {self.company}")


class Coder :
    language = "Java"
    def lan(self) : 
        print(f"The default languages is {self.language}")


class Programmer(Employee, Coder) :           
    name = "Piyush"
    def info(self) :
        self.lan()
        self.show()
        print(f"The name is {self.name} and the salary is {self.salary}")


a = Employee()
b = Programmer()

# print(a.company, b.company)
# b.show()
# b.lan()
b.info()