a=int(input('enter first variable:'))
b=int(input('enter second variable:'))
c=int(input('enter third variable'))
# a, b, c =input('enter no').split(',')

if (a>b) and (a>c):
    temp = a
elif (b>a) and (b>c):
    temp = b
else:
    temp = c

print ('the greatest number is', temp)
    