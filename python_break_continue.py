# initialize integer list
int_list = [3,5,7,13,20,8]

# example of break
#for num  in int_list:
#    print("current item in list",num)
#    if num%2 == 0:
#        print("item in list is even",num)
#        #break

counter = 0
while True:
    if counter <= 10:
        counter += 1
        print("continue")
        continue        
    else: 
        print("break point reached:",counter)
        break
