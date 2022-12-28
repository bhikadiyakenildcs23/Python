outer=[]
inner = []
while(True):
    cnf = input("Enter A Value:")
    if int(cnf) == 0 :
        brkcnf = input("Do You Want To Continue Or Not?(Y or N):")
        if brkcnf == 'Y':
            outer.append(len(inner))
            inner = []
            continue
        elif brkcnf == 'N':
            break
        else:
            print("You Have To Enter Y or N.")
    else:
        inner.append(int(cnf))
        print(inner)
outer.append(len(inner))
print(outer)
    
        
        
        
