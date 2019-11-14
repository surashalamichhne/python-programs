a={'apple','mango','banana'}
b={'orange','apple','banana','pineapple'}
c={'coconut','apple','pineapple'}
total={}
union=a.union(b)

print(a.intersection(b).intersection(c))
print(union.union(c))
print(len(union.union(c)))