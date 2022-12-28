dic={}

while(True):

    rno=int(input("Enter Roll No :"))
    if(rno == 0):
        break
    else:
        marks=[]
        dic[rno]=marks

        for i in range(3):
            m1=int(input("Enter Marks :"))
            marks.append(m1)

        for key , val in dic.items():

            if(key==rno):
                
                print("Roll No  Mark1  Mark2 Mark3  Total")
                print("  " ,key , "   " ,val[0],"   " ,val[1],"   " , val[2] , "  " ,sum(val))

'''
for i in range(len(marks)):
    
        s=s+marks[i]
print("Sum",s)
''' 