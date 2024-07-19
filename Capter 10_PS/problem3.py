'''Create a class with a class attribute a; create an object from it and set 'a' directly using object.a = o. Does this change the class attribute?'''

class attrubute :
    a = 10

at = attrubute()
at.a = 0
print(at.a)