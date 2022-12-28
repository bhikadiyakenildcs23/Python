Definition:- Write a Python program to create a file of strings by 
	     taking input from the user and then create a dictionary 
	     containing each string along with their frequencies. (e.g.
	     if the file contains ‘apple’,‘banana’, ‘fig’, ‘apple’, 
	     ‘fig’, ‘banana’, ‘grapes’, ‘fig’, ‘grapes’, ‘apple’ then 
	     the output should be {'apple': 3, 'banana': 2, 'fig': 3, 
	     'grapes': 2}.

f=open('Demo6.txt','w')
x=[]
all_freq={}
while True:
    line=input("enter characters:")
    if line=='END':
        break
    x.append(line)
    f.write(line)
    f.write('\n')
print(x)
for i in x:
    if i in all_freq:
        all_freq[i]+=1
    else:
        all_freq[i]=1

print(str(all_freq))
f.close()
