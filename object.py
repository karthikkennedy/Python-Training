a=500
print(id(a))
b=1000
print(id(b))
b=a
print(id(b))
print(id(a)==id(b))

