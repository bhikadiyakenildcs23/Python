"""
Q.7. Write a Python program to create a list of strings by taking input from the user and then create
a dictionary containing each string along with their frequencies. (e.g. if the list is [‘apple’,
‘banana’, ‘fig’, ‘apple’, ‘fig’, ‘banana’, ‘grapes’, ‘fig’, ‘grapes’, ‘apple’] then output should be
{'apple': 3, 'banana': 2, 'fig': 3, 'grapes': 2}.
"""

std = dict()
while (True):
    inp = input("Enter A String:")
    if inp == 'Exit':
        break
    for i in inp:
        
        if i in std:
            std[i] += 1
        else:
            std[i] = 1

print(std)
