def read():
    try:
        f = open('D:/Files/test.txt', 'r')#open file
        data=f.read()
        print (data)#read file
        
        p = open('Files/test.txt', 'w')#open file
        print(data)
        print (p.write(data))#read file
        print("File Copied")
    except:
        print("File not found")

def write():
    try:
        #f = open('test.txt', 'r')#open file
        f = open('Files/test.txt', 'w')#open file
        data=input("Enter data to be write")
        print (f.write(data))#read file
    except:
        print("File not found")


        
