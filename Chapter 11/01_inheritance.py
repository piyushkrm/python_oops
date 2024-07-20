class Employee:
    company = "ITC"
    def show(self) :
        print(f"The name is {self.name} and the salary is {self.salary}")


# class Programmer :
#     company = "ITC Infotect"
#     def show(self) :
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def show_language(self) :
#         print(f"The name is {self.name} and he is good with {self.language} language")
    
#  Instant of writing these code we use inheritance and redure line of code and error mistakes

class Programmer(Employee) :            # This is the inheritance
    company = "ITC Infotect"
    def show(self) :
        print(f"The name is {self.name} and the salary is {self.salary}")


a = Employee()
b = Programmer()

print(a.company, b.company)