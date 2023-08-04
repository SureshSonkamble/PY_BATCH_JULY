pwd=input("Enter your password")
n=len(pwd)
u=0
lw=0
d=0
for i in pwd:
          
    if(i.isupper()):
        u=1
    if(i.islower()):
        lw=1
    if(i.isdigit()):
        d=1    

if(u==1 and lw==1 and d==1 and n>=8):
    print("Valid password")
else:
    print("Invalid passowd")
