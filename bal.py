bal=12000

def view_bal():
    pin=int(input("Enter Pin To View Bal"))
    if(pin==123):
        print("Balance =",bal)
    else:
        print("Invalid user")
    
#view_bal()  #func call
