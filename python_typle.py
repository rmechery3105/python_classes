tuple1 = (1,6,3)

print("tuple1:",tuple1)

# tuple1[2] = 8 assignment not allowed in tuple

print("value at index 2 in tuple1",tuple1[2])

print(tuple1[0:])

for i in range(0,len(tuple1)) :
    print("value at index",i,"is:",tuple1[i])
