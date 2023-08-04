def read():
    try:
        #f = open('test.txt', 'r')#open file
        #f = open('Files/test.txt', 'r')#open file
        f = open('D:/Files/test.txt', 'r')#open file
        print (f.read())#read file
    except:
        print("File not found")

def write():
    try:
        #f = open('test.txt', 'r')#open file
        #f = open('Files/test.txt', 'r')#open file
        f = open('D:/Files/test.txt', 'w')#open file
        data=input("Enter data to be write")
        print (f.write(data))#read file
    except:
        print("File not found")

def append():
    try:
        #f = open('test.txt', 'r')#open file
        #f = open('Files/test.txt', 'r')#open file
        f = open('D:/Files/test.txt', 'a')#open file
        data=input("Enter data to be write")
        print (f.write(data))#read file
    except:
        print("File not found")








    

