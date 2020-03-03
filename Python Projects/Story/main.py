from specsheet import Character

def create_char():
    name=input("What is the name of your character? \n")
    age=input("What is the age of your character? \n")
    upbringing=input("What is the upbringing of your character, i.e. peasant, royal?\n")

    Hero=Character(name,age, upbringing)

    print(Hero.age)

create_char()