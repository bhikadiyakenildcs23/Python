Intlst = []
Fltlst = []
Strlst = []
lst=["apple",2,3.4,5,6.7,8,9.0,"Cherry"]
while(True):
    inp = input("Enter A Value // Enter N To Exit! :")
    if inp == 'N':
        break;
    if inp.isdigit():
        Intlst.append(int(inp))
    elif '.' in inp and not inp.isalpha():
        Fltlst.append(float(inp))
    else:
        Strlst.append(inp)
        
itup= tuple(Intlst)
ftup = tuple(Fltlst)
stup = tuple(Strlst)

print("Integers are : ",itup)
print("Floats ..are : ",ftup)
print("Strings are  : ",stup)
    
        
        
