def write():
    try:
        #f = open('test.txt', 'r')#open file
        #f = open('Files/test.txt', 'r')#open file
        f = open('vspi.txt', 'w')#open file
        data=input("Enter data to be write")
        print (f.write(data))#read file
    except:
        print("File not found")
