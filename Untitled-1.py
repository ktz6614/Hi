#first question
import re
import numpy as np
"""n=int(input("Please enter your place in line:"))
c=int(input("Please enter how many cars the train has:"))
p=int(input("Please enter how many people can fit into the car:"))

if n<=c*p:
    print("yes")
else:
    print("No")"""

"""d=int(input("Please enter the number of donuts availible:"))
e=int(input("Please enter the number of trasactions:"))
final=d
while e!=0:
    plusminus=input("Please enter plus or minus:")
    number=int(input("please enter number:"))
    if plusminus =="+":
        final=final+number
        e=e-1
    elif plusminus=="-":
        final=final-number
        e=e-1
    else:
        print("Error, invalid input. Please try again")
print(final)"""
"""ef uppercaseornot(code):
    final=""
    finalnum=0
    num=""
    char=list(code)
    for c in char:
        charbefore=""
        if c.isupper():
            final=final+c
        elif c=="-":
            charbefore="-"
        elif c.isdigit():
            if charbefore !="-":
                num=num+c  

    print(final)
    print(num)
n=int(input("Please enter the number of lines:"))
def regexupper(code):
    uppercase_letters = ''.join(re.findall(r'[A-Z]', code))
    
    # Extract all integers (positive and negative) using regex
    integers = re.findall(r'-?\d+', code)
    
    # Sum all integers
    total = sum(int(num) for num in integers)
    
    # Construct the new product code
    new_code = uppercase_letters + str(total)
    print(new_code)
while n>0:
    code=input("Please enter original code:")
    regexupper(code)
    n=n-1"""
"""def switching(total):
    max_days = maxs(total)
    for i in range(len(total)):
        if total[i] == "P":
            total[i] = "S"   
            max_days = max(max_days, maxs(total))
            total[i] = "P"
    return max_days

def maxs(total):
    s=0
    max_streak=0
    for i in total:
        if i=="S":
            s+=1
            max_streak = max(max_streak, s)
        else:
            s=0
    return max_streak

n=int(input("Enter n:"))
total=[]

while n>0:
    value=input("Enter Value:")
    total.append(value.upper())
    n=n-1

print(total)
print(switching(total))"""

r=int(input("Please enter number of rows:"))
c=int(input("Please enter number of columns:"))
m=int(input("Please enter max number:"))
currentnum=0

startingnumber=1
Table=np.empty((r,c))
for i in range(r):
    for j in range(c):
        Table[i,j]=startingnumber
        startingnumber=startingnumber+1
        if startingnumber==m+1:
            startingnumber=1
def findleast(Table):
    row, col = Table.shape
    prev = Table[0, :].tolist()
    for r in range (1, row):
        curr = [float('inf')] * col
        for c in range (1, col):
            cost=Table[r,c]
            variable = prev[c]
            if c > 0:
                variable=min(variable,prev[c-1])
            if c < col - 1:
                variable=min(variable,prev[c+1])
            curr[c]=cost+variable
        prev=curr
    return min(prev) 
print(findleast(Table))