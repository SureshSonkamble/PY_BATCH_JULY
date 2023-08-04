dit={
    "name":"suresh",
    "age":"30",
    "mobile":"8485070453",
    "pwd":"123"
    
    }
n=int (input("Enter no of element you want to add"))
for i in range(n):
    k=input("Enter key")
    v=input("enter value")
    dit.update({k: v})

print(dit)

s=input("Enter key to be serch")
if(s=='pwd'):
    x=dit.get(s)
    print("pwd lenght",len(x))

    
x=dit.get(s)
if(x==None):
    print("No Value Found")
else:
    print("Value Found",x)




    
    
