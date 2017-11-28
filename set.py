k={4,6,7,123,999,456}

print(k)
print(type(k))

k={1:3,4:6,8:10}

print(type(k))

d={}
print(type(d))

e=set()
print(e)

#List to set conversion
s = set([345,6667,435,90,345])
print(s)

#List to set, set not allow duplicate
t=[1,4,2,1,7,9,7]
print(set(t))

#iteration
for x in t:
    print(x)

#adding

k={82,65}
print(k)

k.add(88)
print(k)

k.update([34,55,11,245])
print(k)
#remove method and discard method
#k.remove(78)  AttributeError: 'set' object has no attribute 'dicard'
print(k)

#k.dicard(23) AttributeError: 'set' object has no attribute 'dicard'
print(k)

j=k.copy()
print(j)

m=set(j)

s.union(t)

s.intersection(t)

s.difference(t)
s.symmetric_difference(t)
s.issubset(t)

s.issuperset(t)

s.isdisjoint(t)
