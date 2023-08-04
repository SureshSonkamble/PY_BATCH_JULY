from datetime import datetime
from datetime import date
today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("test")
#print(x)
#x=2
try:
    print(x)
except:
    print("value of is not defined")    
finally:
    print("exp1 file accssed at",current_time,today)
    
print("normal flow")
