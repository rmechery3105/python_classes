L2 = []
print(type(L2))

L2.append("rajesh")
L2.append(20)
L2.append("som")
L2.append(203)

print(L2)
List1 = L2
print(List1)

for num in range(1,21):
     L2.append(num)

print(L2)  

len_of_list = len(L2)
print("length of list:",len_of_list)

print("compare lists")
List2=List1
if List1 == List2:
    print("list1 and list2 are same")

List3 = ["dsjflsdjkf",23]
if List1 == List3:
    print("list1 and list3 are same")
else: print("list1 and List3 are not same",List1,List3)    

list4 =  List1 + List3
print(list4)

for num in list4:
    print(num)
    print("\n")

list7 = [23,"sashank",234,"fsjdlkj"]   
print("list7",list7)
list7[3]="rajesh"
print("updated list",list7)

print("print list using for loop and index")

for index in range(0,len(list7)) :
    print("index value",index,"list element",list7[index])


list8 = [1,2,3]    
list9 = [7,8,9]

list8.append(list9)

list9.extend(list7)


print("result append",list8)
print("result extend",list9)

print("length of list 8",len(list8))
print("length of list 9",len(list9))

print(list8[0:])
print(list9[3:])
print(list8[:])
print(list8[2:4])
print(list8[:3])
print(list8[0::3])
print(list9[-2:])
print(list9[-2])
