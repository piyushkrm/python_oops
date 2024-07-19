'''Can you change the self-parameter inside a class to something else (say "pihu"). Try changing self to "slf" or "pihu" and see the effects.'''

from random import randint

class Train :

    def __init__(pihu, trainNo) :
        pihu.trainNo = trainNo
        
    def book(pihu, fro, to) :
        print(f"Ticket is booked in the train no : {pihu.trainNo} from {fro} to {to}")

    def getStatus(pihu) :
        print(f"Train no : {pihu.trainNo} is running on the time")

    def getFare(pihu, fro, to) :
        print(f"Ticket are conformed in the train no : {pihu.trainNo} from {fro} to {to} and your seat number is {randint(1, 500)}")

train = Train(22449)
train.book("Delhi", "Katihar")
train.getStatus()
train.getFare("Delhi", "Katihar")