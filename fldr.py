import os
try:
    for i in range(1,50):
        os.makedirs('D:\Files\Flder'+str(i))
        print("Folder created",i)
except Exception as e:
    print(e)
