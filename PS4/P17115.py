Definition:- Write a Python program to create a text file of multiple lines.
	     Take input of a word from the user and then display all the lines 
	     from the file containing this word along with the frequency of
	     the word in that line.


f=open('Demo7.txt','w')
print('Enter multiple line data')
while True:
    line=input()
    if line=='END':
        break
    f.write(line)
    f.write('\n')
f.close()
f=open('Demo7.txt','r')
word=input("Enter the word:")
s=" "
count=1
l=f.readlines()
for i in l:
    l2=i.split()
    if word in l2:
        print(i)
    count+=1

f=open('Demo7.txt','r')
word=input("Enter the word:")
d1=dict()
j=0
l=f.readlines()
for i in l:
    j=j+1
    l2=i.split()
    if word in l2:
        l2.count(word)
    count+=1
    print("line no",str(j),":",l2.count(word))
f.close()

 