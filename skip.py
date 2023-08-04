'''x, y = input("Enter two size: ").split()
print("First Size: ", x)
print("Second Size: ", y)'''
a = input("Enter  size:1 ")
s1=int(a[:-2])
b = input("Enter  size:2 ")
s2=int(b[:-2])
sz=s1+s2
#print(sz,"ML")
ml=sz%1000
l=int(sz/1000)
print(ml,"ml")
print(l,"liter")

'''if(sz>1000):
    #l=sz-1000
    print(" 1 lieter",l,"ml")
else:
    print(sz,"ml")'''


    
