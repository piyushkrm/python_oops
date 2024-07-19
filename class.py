class employe :
    language = "python"     #This is the class attribute
    salary = 1500000

piyush = employe()          #object of employee class
piyush.name = "piysuh Mishra"
print(piyush.salary, piyush.name, piyush.language)

aayush = employe()
aayush.name = "Aayush"      #This is the instance(object) attribute
print(aayush.name, aayush.salary, aayush.language)

# Here name is instance(object) attribute and salary and langauge are class attribute as they directly belog to the class
