data="What is a paragraph?Paragraphs a are the a buildingblocks of papers. Manystudents define paragraphs"
print(data.find("p"))
s=input("Enter word to be found")
n=0
for i in data.split() :
    if(i==s):
        n=n+1
        print("found",n,"time")
  


