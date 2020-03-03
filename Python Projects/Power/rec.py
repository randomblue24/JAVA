
from pynput.keyboard import Key, Listener

#Recursive Power function 

x=int(input("Enter the base: "))
y=int(input("Enter the power: "))

def recurse(number, power):
    if(power==0):
        return 1
    if(power==1):
        return(number)
    #elif (power==0):2
        #return 1
    elif (power!=1):      
        return(number*recurse(number,power-1))

print("Result:", recurse(x,y))

#z=input("Press r to restart: ")

#def on_press(r):
 #   x=input("Enter the base: ")
  #  y=input("Enter the power: ")

#    print("Result:", recurse(x,y))

        


    