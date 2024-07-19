# Note : Instance attributes, take preference over class attributute during assignment and retrivak
class employe :
    language = "python"     #This is the class attribute
    salary = 1500000

piyush = employe()          #object of employee class
piyush.name = "piysuh Mishra"

piyush.language = "Java"            # This is the instance attribute
print(piyush.salary, piyush.name, piyush.language)
