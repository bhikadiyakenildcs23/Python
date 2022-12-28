std = dict()
inp = input("Enter A String:")

for i in inp:
    if i in std:
        std[i] += 1
    else:
        std[i] = 1
print(std)
        
    
    


