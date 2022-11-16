# funcitons in python
list1 = [342432,2344,22,35335,-1343]
print('max of list1:',max(list1))
print('min of list1:',min(list1))
print('sum of list1:',sum(list1))

# first function
def welcome_mes():
   # print('welcome to python programming')
    return 'welcome to python programming'
    


print('simply call function')
welcome_mes()
stg1 = welcome_mes()
print('value returned by function:',stg1)

 # Now Playing - 13th Nov Live Class Python Part 3 watched till 2:08:48 hours 

 # example function which accepts parameters

def avg_of_two_num(n1,n2):
    avg_res = (n1 + n2)/2
    return (avg_res)

n1 = 12
n2 = 13
print('average of n1 & n2 is : ',avg_of_two_num(n1,n2))  

# if we pass incorrect number of arguments then error is returned
#print('average of n1 & n2 is : ',avg_of_two_num(n1)) 

# function to find factorial of a number

def factorial(n):
    fac_res=1
    for i in range(1,n+1):
        fac_res= fac_res * i
    return(fac_res)  

print('factorial of 6 is : ',factorial(6))

# how to return multiple values from function

a,b,c = 1,2,3
print('a:',a,'b:',b,'c:',c)

# return multiple items from function

def square_and_cube(a):
    sqr = a*a
    cbe = a*a*a
    return sqr,cbe
   

n=4
sqr_ans,cub_ans =     square_and_cube(n)
print('square of 4: ',sqr_ans,'cube of 4',cub_ans)

# create optional arguments
def multiply_two_numbers(a,b=3):
    return a*b

print('result of multiplying two numbers 6,7:',multiply_two_numbers(6,7))
print('result of multiplying two numbers 2,3:',multiply_two_numbers(2))  

# optional parameters should be defined at last 

#def multiply_two_numbers2(a1=3,b1):
    return a1*b1

#print('result of multiplying two numbers 6,7:',multiply_two_numbers2(6,7))
# error returned
#[Running] python -u "/config/workspace/python_funcion.py"
#  File "/config/workspace/python_funcion.py", line 70
#    def multiply_two_numbers2(a1=3,b1):
                              ^
#SyntaxError: non-default argument follows default argument
     
# wathed till 3:00:07
