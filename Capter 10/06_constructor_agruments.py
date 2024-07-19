class employe :
    language = "python" 
    salary = 1500000

    def getInfo(self) :
        print(f"The language is {self.language}.\nAnd the salary is {self.salary}")

    def __init__(self, salary, language):   
        self.salary = salary
        self.language = language
        


piyush = employe(2000000, "JavaScript")         
piyush.getInfo()
