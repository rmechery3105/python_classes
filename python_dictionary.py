dict1 = {}
print(type(dict1))

# insert values into dictionary

dict1['name'] = 'Rajesh Mechery'
dict1['age'] = 43
dict1["places_visited"] = ["kerala","karnataka","tamilandu","Bangalore"]
dict1["skills"] = ["python","informatica","unix","spark"]

print('dict1 before adding dic2: ' , dict1)
dict2 = {'nationality': 'Indian','colour':'black'}
dict1['other details'] = dict2



print("dict1 after adding dict2",dict1)

# check lenght of dictionary

print('length of dict1:',len(dict1),'length of dict2',len(dict2))

# access particular value in dicionary

print('name element from dict1:',dict1['name'])
print('other details element from dict1:',dict1['other details'])

print('display list in dictionary:',dict1["skills"][1])
temp1 = dict1['skills']
print('display list in dictionary using variable:',temp1[1])

# access dictionary inside a dictionary

temp2 = dict1['other details']
print('display nationality inside dict1:',temp2['nationality']) 

# wrong way print('second way display nationality inside dict1:',dict1['skills']['nationality'])

# update dicitonary elements
dict1['age'] = 40

print ('updated element in dictionary',dict1['age'])

# get keys in a dictinary
print('tot_no_keys in dict1 = ',  dict1.keys())
print('tot_no_keys in dict1 in list form = ',  list(dict1.keys()))

# get dict values
print('values in dict1 in list form = ',  list(dict1.values()))

print('how to iterate dictionary')

for k,v in dict1.items():
    print('key is: ',k,' and value is',v)

# compare dictionary

dict3 = { '1' : 'a','2':'b','3':'c'}
dict4 = { '2':'b','1' : 'a','3':'c'}
dict5 = { '5' : 'a','2':'7','3':'c'}

print(dict3 == dict4)
print(dict4 ==  dict5)

del dict3['1']
del dict4['3']

print(dict3)
print(dict4)

print('check key in dictioanry')

dict_keys = list(dict1.keys())

if 'skills' in dict_keys:
    print('true')
else:
     print('true')   
     
