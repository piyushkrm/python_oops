'''Create a Class "Programmer" for storing information of few programmers working at Microsoft.'''
class Programmer():
    company = "Microsoft"
    work_type = "Full time"

    def __init__(self, name, salary, address) :
        self.name = name
        self.salary = salary
        self.address = address


    def ProgramerInfo(self) :
        print(f"Name of the programer is : {self.name}.\nHe work at {self.company} comapany.\n{self.name} job type is {self.work_type}.\nHe has {self.salary} salary.\n{self.name} is from {self.address}")


info = Programmer("piyush Mishra", 45000000, "Delhi")
info.ProgramerInfo()