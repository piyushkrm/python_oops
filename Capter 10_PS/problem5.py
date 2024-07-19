'''Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.'''

from random import randint

class Train :

    def __init__(self, trainNo) :
        self.trainNo = trainNo
        
    def book(self, fro, to) :
        print(f"Ticket is booked in the train no : {self.trainNo} from {fro} to {to}")

    def getStatus(self) :
        print(f"Train no : {self.trainNo} is running on the time")

    def getFare(self, fro, to) :
        print(f"Ticket are conformed in the train no : {self.trainNo} from {fro} to {to} and your seat number is {randint(1, 500)}")

train = Train(22449)
train.book("Delhi", "Katihar")
train.getStatus()
train.getFare("Delhi", "Katihar")