l1=[1,"red",2,3]
l2=["apple","orange"]
l3=["php","python","java"]
l4=[]
l1.extend(l2)
l2.extend(l1)
l3.append("OBASIC")
l4.extend(l1)
l1.remove("red")
print(l4)
print(l3)
print(l2)
print(l1)