# Sometimes we need a function that does not use the self-parameter. We can define a static method like this:

class employe :
    language = "python" 
    salary = 1500000
    def getInfo(self) :
        print(f"The language is {self.language}.\nAnd the salary is {self.salary}")

    @staticmethod           #Tell him to no need of arguments as a self
    def greet() :
        print("Hey Good Evening")

piyush = employe()         
piyush.getInfo()
piyush.greet()
