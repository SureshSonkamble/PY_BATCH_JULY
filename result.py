s1=int(input("Enter sub1 marks"))
s2=int(input("Enter sub2 marks"))
s3=int(input("Enter sub3 marks"))
if(s1>100 or s2>100 or s3>100):
    print("invalid marks")
else:
    ttl=s1+s2+s3
    avg=ttl/3
    res=""
    if(avg>=75):
        res="A+"
    elif(avg<75 and avg>=60):
        res="A"
    elif(avg<60 and avg>=50):
        res="B"
    elif(avg<50 and avg>40):
        res="C"
    elif(avg==40):
        res="PASS"
        
    else:
        res="FAIL"
       
    print("Total=",ttl)
    print("Percentage (%)=",avg)
    print("Result=",res)



