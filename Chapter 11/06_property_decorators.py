# property decorators

class engineer : 

    @property
    def name(self) :
        return f"{self.firstName} {self.lastName}"


    @name.setter
    def name (self, value) :
        self.firstName = value.split(" ")[0]
        self.lastName = value.split(" ")[1]


eng = engineer()

eng.name = "piyush Mishra"
print(eng.firstName)
print(eng.lastName)