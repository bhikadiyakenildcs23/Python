Definition:- Write a Python program to create a file of elements of 
	     any data type (mixed data type, i.e. some elements maybe 
	     of type int, some elements of type float and some elements
	     of type string). Split this file into three file containing 
	     elements of same data type (i.e. 1st file of integers only, 
	     2nd file of float only and 3rd file of strings only). Take 
	     input from the user to create the file. 

import ast
x=[]
integers=[]
f=open('Demo4.txt','w')
floats=[]
strings=[]
print("Enter 0 for you want to quit")
while True:
    line=ast.literal_eval(input("enter data:"))
    if line==0:
        break
    x.append(line)
print(x)
f.writelines(str(x))
f.close()
f=open('Demo4.txt','r')
for data in x:
    if type(data)== str:
        strings=open('Demo4strings.txt','a')
        strings.write(data)
        strings.write('\n')
        strings.close()
    elif type(data)== float:
        floats=open('Demo4floats.txt','a')
        floats.write(str(data))
        floats.write('\n')
        floats.close()
    else:
        integers=open('Demo4integers.txt','a')
        integers.write(str(data))
        integers.write('\n')
        integers.close()
f.close()    
