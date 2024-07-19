'''Add a static method in problem 2, to greet the user with hello.'''

# Problem 2 is here
class calculator() :


    def __init__(self, number):
        self.number = number

    def square(self) :
        print(f"Square of your entered number is : {self.number * self.number}")

    def cube(self) :
        print(f"Cube of your entered number is : {(self.number * self.number)*self.number}")

    def squareroot(self) :
        print(f"Squareroot of your entered number is : {self.number ** 1/2}")

    @staticmethod
    def greet() :
        print(f"Hello there !")

cal = calculator(3)
cal.square()
cal.cube()
cal.squareroot()
cal.greet()