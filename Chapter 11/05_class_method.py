# Class Method - > A class method which is bound to the class and not the object of the class
#  @classmethod decoder is used to create a class method
#  this is used to use class attribute not a instance attribute

class engineer : 
    name = "Piyush"

    def show(self) :
        print(F"The name of an enhinner is {self.name}")

eng = engineer()
eng.name = "Pihu"
eng.show()


# This program is print th ename of pihu because this is use instance attribue not a class attribute


# now i make a code to use class attribute not a instance attribute

class engineer : 
    name = "Piyush"

    @classmethod
    def show(cls) :
        print(F"The name of an enhinner is {cls.name}")

eng = engineer()
eng.name = "Pihu"
eng.show()

# this code is print the name is piyush not a Pihu because @classmethod are use class attribute not a instance attribute