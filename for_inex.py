'''n=int(input("Enter range"))
for i in range(n):
    print(i)'''

'''name="CodingSeekho"
for s in name:
    print(s)'''

name="CodingoSeekho"
cnt=0
c=input("Enter char to be search")
for s in name:
    if(s==c):
        cnt=cnt+1
        
print("Count=",cnt)
