# import random
import random


# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6,7,8,9,10]
rnm=random.choice(list1)
n=0
cnt=0
cnh=3
while n<=3: 
    ch=int(input("Gues your number between [1..10] "))
    print("You have chnase",cnh)             
    if(rnm==ch):
        print("Match Found")
        cnt=cnt+100
    else:
        print("Not match")
        n=n+1
        cnh=cnh-1
        
#print("You have enter number",ch)
print("Actual Number: ",rnm)
print("Score: ",cnt)

