ls=[]
while(True):
    inp=int(input("Enter A Number!"))
    if inp == 0:
        break
    else:
        ls.append(inp)
        
    st = set(ls)
    ls = list(st)
print(ls)
