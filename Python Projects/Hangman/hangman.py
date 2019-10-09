import platform
import random

from PIL import Image
from Hangman.body import strike

F=open('C:\\Users\\Node 1\\Documents\\Python Prc\\Hangman\\words.txt','r')

#for line in F:
    #for word in line.split():
        #print(word)      
global game_Over=False
global strike=6
global count
count=0

#End the game with printing the full picture
def end_game():
    if game_Over==True:
        print("Game over!")
        end.show()
        inp=input("Do you want to play another game? Enter Y or N")
#        if inp=='Y'or'y':
#            start_game()

def guess():
    while(strike>0):
        x=input("What letter is in the word? ")
        #if strike==0:
         #   end_game()
        for wor in word:
            if word[wor]==x:
                print("Correct!")
                count=count+1
        if count==0:
            strike=strike-1
        count=0

def start_game():
    print("Your word is ", len(word) , "characters long")
    print("The word begins with an ", word[0])
    print("The word ends with an ", word[len(word)-1])
    guess()



#Start the game with printing the image
if game_Over==False: 
    #Generate the word at random using the random library
    #split() splits the string into a list. readline()reads one entire line from the file, while read() reads all lines
    word= random.choice(open('C:\\Users\\Node 1\\Documents\\Python Prc\\Hangman\\words.txt').read().split())
    #Test if code works. It works! 
    #print(word)

    #Initializing the strike. You have 4 strikes.
    #strike=6
    #count=0
    start=Image.open('C:\\Users\\Node 1\\Documents\\Python Prc\\Hangman\\start.png')
    end=Image.open('C:\\Users\\Node 1\\Documents\\Python Prc\\Hangman\\man.jpg')
    start.show()
    start_game()


