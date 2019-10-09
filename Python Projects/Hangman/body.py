import platform

strike=6
count=0

def end_game():
    if game_Over==True:
        print("Game over!")
        end.show()
        inp=input("Do you want to play another game? Enter Y or N")
        if inp=='Y'or'y':
            start_game()


def guess():
    while(strike>0):
        x=input("What letter is in the word? ")
        if strike==0:
            end_game()
        for wor in word:
            if word[wor]==x:
                print("Correct!")
                count=count+1
        if count==0:
            strike=strike-1
        count=0


def start_game():
    strike=6
    count=0
    print("Your word is ", len(word) , "characters long")
    print("The word begins with an ", word[0])
    print("The word ends with an ", word[len(word)-1])
    guess()