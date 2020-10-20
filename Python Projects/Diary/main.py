import diary


print("Welcome to Le Diary. \n Please Select a Choice: ")
x=print("1: Create a New Diary 2: Open an existing Diary: ")

if(x=='1'):
    filename=input("Enter a title for the Diary: ")

    d1=diary.Diary('James','9-16-2031')
    d1.add_entry()
    d1.view('Nono')

