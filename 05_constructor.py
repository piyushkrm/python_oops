class employe :
    language = "python" 
    salary = 1500000
    def getInfo(self) :
        print(f"The language is {self.language}.\nAnd the salary is {self.salary}")

    @staticmethod           #Tell him to no need of arguments as a self
    def greet() :
        print("Hey Good Evening")

    def __init__(self):             # dunder(__) method which is automatically called
        print("This is an constructor that called automatically when main class was calling")


piyush = employe()         
piyush.getInfo()
piyush.greet()
