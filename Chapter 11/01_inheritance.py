class Employee:
    company = "ITC"
    def show(self) :
        print(f"The name is {self.name} and the salary is {self.salary}")


class Programmer :
    company = "ITC Infotect"
    def show(self) :
        print(f"The name is {self.name} and the salary is {self.salary}")

    def show_language(self) :
        print(f"The name is {self.name} and he is good with {self.language} language")
    
a = Employee()
b = Programmer()

print(a.company, b.company)