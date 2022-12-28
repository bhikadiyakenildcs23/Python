lst = []
otpl = ()
ol = list(otpl)
etpl = ()
el = list(etpl)
while(True):
    inp = int(input("Enter A Number Except 0:"))
    if inp == 0:
        break
    else:
        lst.append(inp)

for i in lst:
    if i%2 == 0:
        el.append(i)
        
    else:
        ol.append(i)
        
otpl=tuple(ol)
etpl=tuple(el)
print("Odd Numbers: ",otpl)
print("Even Numbers: ",etpl)
