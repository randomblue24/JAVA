from distutils.tests.test_sdist import SDistTestCase

class Info:

    global name
    global race
    global gender
    global age
    global rank
    global Class


    def __init__(self, name, race, gender, age):
        name=str(name)
        race=str(race)
        gender=str(gender)
        age=int(age)

    def description (self, rnk, Class):
        rank=str(rnk)
        Class=str(Class)

    def setClass(self, Class):
        Class=str(Class)
    
    def getClass(self):
        print("%s class:%s", name, Class)


if __name__ == "__main__":

    char1=Info('james','noble','male', 22)

    char1.setClass('Mage')

    char1.getClass()



        

    
    