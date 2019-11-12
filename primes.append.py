primes=[] #empty list
n=int(input('enter one variable:'))
for n in range(2,n):
    ans =True
    for i in range(2,n):
        if n%i==0:
            ans= False
            break
    if ans== True:
        primes.append(n) #add to list of prime
print(primes)