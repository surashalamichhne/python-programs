maths={'john':88.0, 'sam':77.0}
for key,value in maths.items():
    print(key,value)
d={'john':88.0, 'sam':77.0}
d2={'shahil':70.0,'adi':84.0}
d.update(d2)
print(d)
d={'john':88.0, 'sam':77.0}
d2={'shahil':70.0,'adi':84.0}
dic4={'elisha':66.0}
for d in (d,d2): dic4.update(d)
print(dic4)
if 'saurav' in dic4:
    print('key is present in the dictionary')
else:
    print('key is not present in the dictionary')