lst=[1,7,9,4,2,6,3,8,9]#index start with 0
print(lst)
print(lst[0])# first
print(lst[-1])#last
print(lst[3:])#print val 3 to onward
print(lst[:3])#print val strat 0 to 3
print(lst[1:5])#print val bwt 1 to 5
#add
lst.append(11)
print(lst)
#add at index
lst.insert(5,12)
print(lst)
#remove
lst.remove(7)
print(lst)
#remove
lst.pop(5)
print(lst)

n=int(input("Enter element to be search"))
ind=0
for i in lst:
    ind=ind+1
    if(i==n):
        print("Found at index",ind-1)
        break
    else:
        print("Not Found")







