l=[1,2,3,4,5,6,7,8,9]
b=len(l)
for items in l:
    if items%2==1:
        l.remove(items)
print(l)
