import platform
import os


class Diary:
    def __init__(self, name, date):
        name=self.filename


    def add_entry(self):      
        filename=input("Enter a title for the Diary: ")

        def new_line(self, diary):
            string = diary
            string=list(string)

            for x in string:
                if(string[x]=='.'):
                    string.insert(x, '\n')
            ''.join(string)
            return string
            

        #successfully creates a file named whatever, but can't create it under the /Diary/ folder
        f = open('{}.txt'.format(filename), 'w+')

        subject=input("Enter a subject for the diary: ")

        f.write("{}".format(subject))

        body=input("Enter text to write in diary. Press 'Enter' when done: \n")

        f.write("{}".format(body))

        new_line(self, f)

        #print("Write your entry.", '\n')

        print(f)

        f.close()

    def view(self, filename):
        f=open("{}".format(filename), 'r')
        print(f)
