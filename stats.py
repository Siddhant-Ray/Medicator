import json

a=open("disease.txt","r+")

b=a.read().split("    ")
c=[]
for i in b:
    if i!='':
        c.append(i)


d=[]
for i in c:
    [x,y]=(i,c.count(i))
        
    d.append([x,y])

#print(d)

unique=[]

for i in d:
    if i not in unique:
        unique.append(i)

#print(unique)

for i in unique:
    if (i[1]>6):
        print("Probable epidemic of",i[0])
    
    ###
