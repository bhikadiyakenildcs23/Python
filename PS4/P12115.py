while(True):
    inp = input("Enter 1 to show Entire File! \nEnter 2 to Show 'n' Line \nEnter 3 to display 'm' Lines From 'n'th Line \nEnter 4 to find number of words in each line! \n              Enter Here...: ")
file = open("Tst4P1.txt","r")
print(file.read())
