
from PIL import Image
import os
import pathlib
from PIL import ImageFile
from single import convert_sing

# from the tkinter library
import tkinter as Tk
# import filedialog module
#from tkinter import filedialog
import tkinter.filedialog

#from tkinter import * as tk
#import tkinter as tk

#Need this else, it stops because image file too big
ImageFile.LOAD_TRUNCATED_IMAGES = True



# Design Idea: Give a directory, and the script will go through every image type
# and convert to type PNG

def convert_dir(path, convert_type):

    # scandir() takes an object with path mapped to iter(object, subclass)
    # scanning the directory linked for files that don't end with the name type you want
    # to convert to

    # if Remove the '.', remove the dot. This will be used in a function call later.
    if not convert_type.find('.'):
        # convert_type2=convert_type
        convert_type = convert_type.replace(('.', convert_type))
        print(convert_type)

    for file in os.scandir(path):
        if not file.name.endswith(convert_type):

            print("file name begin: ", file.name)
            # to open an image you need the path, which is what's being done here
            # we are getting the absolute file path
            file_path = os.path.abspath(file)

            # open the image for modification
            image = Image.open(file_path)

            # get the file extention of the current file
            # can't print this without converting to str first
            file_type = pathlib.Path(file_path).suffix


            # ***DONT DELETE***
            # add a . to the file_type. Won't save as PNG without adding the '.'
            convert_type2 = ".{0}".format(convert_type)

            print("converty type: ", convert_type)
            print("convert type2: ", convert_type2)
            # file_type=y.replace(('.',''))
            print("file type: ", str(file_type))

            # setting file_name = file_path to replace the current file_type w/ desired type
            # if you don't, end result is a nonspecified file type (literally unknown, but opens in paint)
            file_name = file_path.replace(file_type, convert_type2)

            print("file name: ", file_name)
            image.convert('RGB')

            # file_name has the filepath AND name of the file, i.e. \users\docs\superman.PNG
            # saving image as a PNG
            print("convert type last: ", convert_type)
            image.save(file_name, convert_type)
            # closing the image we opened. Not sure if this is necessary
            # image.close()
            print(file.name+" converted \n")


def remove_origin(path, convert_type):
    # if user did not enter a '.'
    if not convert_type.find('.'):
        # convert_type2=convert_type
        convert_type = convert_type.replace(('.', convert_type))
        print(convert_type)

    for file in os.scandir(path):
        if not file.name.endswith(convert_type):
            os.remove(file)
            print(file.name+" removed \n")

#TK file.dialog file browser prompt
def browser(option):
    
    if(option=='1'):
        file_name = Tk.filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Images",
                                                            "*.JPG* *.PNG* *.JPEG* "),
                                                        ))                                                                                        
        return file_name
    
    elif(option=='2'):
        folder_name = Tk.filedialog.askdirectory()                                                                                        
        return folder_name   
                                             

def main():
    print("\nWelcome to Image Converter by Randomblue24. \nSupported File Types: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html \n\nSelect an option from the list: ")
    choose=input("1: Convert a single Image \n2: Convert a folder of Images \n\nSelection: ")
    delete = input("Delete old file(s) after conversion? Enter Y or N: ").upper()

    if(choose=='1'):
        print("Browse to file location")
        path = browser(choose)
        convert_type = input("Enter convert type: ").upper()
        convert_sing(path, convert_type)
        
    else:
        if(choose=='2'):
            print("Browse to folder location")
            path = browser(choose)
            convert_type = input("Enter convert type: ").upper()
            convert_dir(path, convert_type)
            
    #if user wants to delete original files
    if(delete=='Y'):
        remove_origin(path, convert_type)

main()
