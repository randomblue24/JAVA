import platform

class Diary:
    def __init__(self, name, date):
        name=name
        date=date

    def add_entry(self):
        print("Add your entry: ", "\n")
        f= open("guru99.txt","w+")

        filename=input("Enter a title for the Diary: ")

        f = open('{}.txt'.format(filename), 'w+')

        #print("Write your entry.", '\n')

        try:
            while True:
                x=input("Write your entry.", '\n')
        except KeyboardInterrupt:
            pass


d1=Diary('James','9-16-2031')
d1.add_entry()