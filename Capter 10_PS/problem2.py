'''Write a class "calculator" capable of finding square, cube and square root of a number.'''

class calculator :

    def __init__(self, number):
        self.number = number

    def square(self) :
        print(f"Square of your entered number is : {self.number * self.number}")

    def cube(self) :
        print(f"Cube of your entered number is : {(self.number * self.number)*self.number}")

    def squareroot(self) :
        print(f"Squareroot of your entered number is : {self.number ** 1/2}")


cal = calculator(3)
cal.square()
cal.cube()
cal.squareroot()
