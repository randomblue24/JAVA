from PIL import Image
import os
import pathlib
from PIL import ImageFile


#important: https://pillow.readthedocs.io/en/3.2.x/handbook/image-file-formats.html#jpeg
#check the mage file formats to see what's available, i.e. no jpg, but yes jpeg

#converts a single image. Must give full directory, i.e. C:\Users\Admin\Pictures\IntergalacticPics\ship.jpg
def convert_sing(path, convert_type):
    if not convert_type.find('.'):
        # convert_type2=convert_type
        convert_type = convert_type.replace(('.', convert_type))
        print(convert_type)
    
    #open file, need this to edit
    img=Image.open(path)
    
    #save the file extention, in file_type 
    file_type = pathlib.Path(path).suffix
    print("file_type ", file_type)

    #add a '.' to the type you want
    convert_type2 = ".{0}".format(convert_type)
    print("convert type2: ", convert_type2)
    
    #replace the old file extention (file_type) with new file extention, stored in converty_type
    file_name = path.replace(file_type, convert_type2)
    
    print("file_name : ", file_name)

    #to edit the image, need to convert it to RGB mode
    img.convert('RGB')
    
    print("last step ")
    #save the image: save(/...directory../file name.new_extention, new file type )
    img.save(file_name, convert_type)
    
    print(path+" converted \n")