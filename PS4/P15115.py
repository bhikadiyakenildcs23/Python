Definition:- Write a Python program to create a file containing 
	     student records where each record contain rollno 
	     and marks in 3 subjects separated by a comma (marks 
	     to be considered as list of 3 values).
	     e.g. records of students: 1, [45, 40, 35], 2, [41, 
	          38, 39], 3, [35, 30, 37] (each line of the file
	     containing record of only 1 student). Prepare mark list 
	     in the following format:

	Roll No. Mark-1 Mark-2 Mark-3 Total
 	   1 	   45     40     35     120


f=open('Demo5.txt','w')
students=[]
total=0
count=0
s=[]
n=int(input("How many students are there:"))
for i in range(n):
    srno=input("Enter Roll no of students")
    students.append(srno)
    marks=[]
    for j in range(3):
        mark=int(input("Enter marks:"))
        marks.append(mark)
    f.write(students[i])
    print(students)
    f.write(str(marks))
    f.write('\n')
    s.append(srno)
    s.append(marks)
print(s)
f.close()
f=open('Demo5.txt','r')
print("File data")
print(f.read())
f.close()
f=open('Demo5.txt','r')
for i in f:
    k=i.split('[')[0]
    k1=i.split('[')[1][0]
    k2=i.split('[')[1][3]
    k3=i.split('[')[1][6]
    print("Roll no:",k)
    print("Marks 1:",k1)
    print("Marks 2:",k2)
    print("Marks 3:",k3)
f.close()
