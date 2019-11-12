dict={'rollno':[1,2,3,4],'name':['ram','hari','adi','elisha']}
roll=dict['rollno']
nam=dict['name']
data=input('3')
for i in range(len(3)):
    if roll[i]==data:
        temp=i
print(nam[temp])