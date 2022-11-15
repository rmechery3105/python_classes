s1 = set()
print(type(s1))

list1 = [1,2,3,4,3,2,3,5,3]
s1 = set(list1)

print(s1)

s3 = {1,2,3,4,3,3543}
print('type:',type(s3),'values:',s3)

# iterate elements in set
for num in s1:
    print(num)

print('convert set into list')    
list2 = list(s3)
print('type of list2:',type(list2))
print(list2)

# add elements into set

cities = set()
cities.add("bangalore")
cities.add("delhi")
cities.add("hyderabad")
cities.add("newyork")
cities.add("moscow")
cities.add(1)

print(cities)

# use of update in sets
temp = [4343,2343,23423]
cities.update(temp)

print('set citites after adding temp:',cities)
print('length of set cities:',len(cities))

# set operations

set_a={1,2,3,4,5}
set_b={3,5,7,2343}

# union operation

print('union:' , set_a | set_b)

# intersection operation

print('intersection' , set_a & set_b)

# minus operation

print('a-b' , set_a - set_b)
print('b-1' , set_b - set_a)

#comparison in sets

print(set_a == set_b)
print(set_a == set_a)
