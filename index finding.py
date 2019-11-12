names=['john','sam','anna','ben','jeff']
maths=[88.0,77.0,67.0,87.0,90.0]
english=[86.0,67.0,65.0,78.0,80.0]
for i in range(len(names)):
    if names[i]=="anna":
        a=i
print('marks in maths',maths[a])
print('marks in english',english[a])
