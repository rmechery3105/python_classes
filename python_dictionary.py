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
