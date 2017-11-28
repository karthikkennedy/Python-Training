disc={1:'firstkey',2:'secondkey',1:'overridekey'}
print(disc)
print(disc[1])
#dictionary with mixed keys
disc={'hi':'hello',1:[2,3,4]}
print(disc['hi'])
print(disc[1])
#using distinct value
disc=dict({1:'apple',2:'orange','three':'banana',1:'mango'})
print(disc)
#accessing element from dicsc
print(disc['three'])
print(disc.get('three'))
print(disc)
#add item
disc['four']='strwbery'
print(disc)
#using pop method
squares={2:4,1:1,3:9,4:16,5:25}
print(squares.pop(4))
print(squares)

#using update method
stock={'EmpId':'100','name':'karthik','age':31}
stock.update({'EmpId':'100abc','age':32})
print(stock)

#remove all item
stock.clear();
print(stock)
print(2 in squares)
print(7 in squares)

for i in squares:
    print(squares[i])

print(len(squares))
print(sorted(squares))

names_and_ages = [('Alice', 32), ('Bob', 48), ('charlie', 32)]
d = dict(names_and_ages)
print(d)

