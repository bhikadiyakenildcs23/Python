Definition:- Write a Python program to create a file of numbers by 
	     taking input from the user. Split this file into two 
	     files where one file contains odd numbers, and the other 
	     file contains even numbers from the file. You can take 
	     input of non-zero numbers, with an appropriate prompt, 
	     from the user until the user enters a zero to create the 
	     file assuming that the numbers are non-zero.



f=open('Demo3.txt','a')
while True:
    no=int(input("Enter Numbers:"))
    if no==0:
        break
    else:
        if(no%2==0):
            even=open('Demo3even.txt',"a")
            even.write(str(no))
            even.write("\n")
            even.close()
        else:
            odd=open('Demo3odd.txt',"a")
            odd.write(str(no))
            odd.write("\n")
            odd.close()
    f.write(str(no))
    f.write('\n')
f.close()
