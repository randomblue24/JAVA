import platform
from getpass import getpass

users={}

def start_page():
    prompt=input("Do you have an account? Y or N \n").lower()
    if(prompt=='y'):
        login()
    
    elif(prompt=='n'):
        create_login()


def create_login(): 
    login=input("Create a Username \n")
    password=getpass()

    users[login]=password 

    prompt=input("Do you want to see your pass? Y or N \n").lower()

    if(prompt=='y'):
        prompt2=input("Enter your username: \n")
        if prompt2 in users:
            print(users[prompt2])
        else:
            print("User not found. \n")
    else:
        if(prompt=='y'):
            return


def login():
    prompt1=input("Username: \n")
    


        