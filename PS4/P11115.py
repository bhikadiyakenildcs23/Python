"""
Q.1. Write a Python program to create a file of numbers by taking input from the user and then
display the content of the file. You can take input of non-zero numbers, with an appropriate
prompt, from the user until the user enters a zero to create the file assuming that the numbers
are non-zero.
"""

file = open("Tst4P1.txt","r+")
while(True):
    inp = int(input("Enter A Number! : "))
    if inp == 0:
        break
    
    file.write(str(inp))
    file.write(" ")

file = open("Tst4P1.txt","r")
print(file.read())
file.close()

    
