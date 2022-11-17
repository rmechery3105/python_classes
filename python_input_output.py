# declare and assign variables in python

int_var =  100
float_var =  1.3254
bool_var = True
string_var =  'welcome to python programming'

print('hellow world')
print('int variable :',int_var)
print('float variable :',float_var)
print('bool variable :',bool_var)
print('string variable :',string_var)

# check type of variable

print('type of variable :',type(int_var))
print('type of variable :',type(float_var))
print('type of variable :',type(bool_var))
print('type of variable :',type(string_var))

# how to do type cast
# int(),float(),bool(),string()

cast_float_int = int(float_var)
cast_int_float = float(int_var)

print('float to int: ',cast_float_int)
print('int to float: ',cast_int_float)

str_to_int = int("123")

print('string to int: ',str_to_int+20)

#input values using input()

print('input name:')
nam = input()
print('input age:')
ag = input()

print ('name=',nam,'age=',ag)
# watched till 01:41:55

