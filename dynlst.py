from tabulate import tabulate

l=[]
nm=[]
br=[]
print(l)
n=int(input("Enter number  and name and branch of Student you want to add"))
print("====================================")

for i in range(0,n):
    print("Student",i+1,"marks")
    m=int(input("Entre marks\n"))
    l.append(m)
    
    print("Student",i+1,"Name")
    mn=input("Entre Name\n")
    nm.append(mn)

    print("Student",i+1,"branch")
    b=input("Enter Branch\n")
    br.append(b)
    
print(l)
print(nm)
print(br)
#l=l+nm
print(l)
print("====================================")
print("| Marks |Name|Branch|")
print("___________________")
y=0
for i in l:
    y=y+1
    print("|",i," "*(6),"|",nm[y-1]," "*(3),"|",br[y-1]," "*(3),"|")
    print("_________________")    

