strg1 = "hello world"
print(strg1)

strg2 = 'he is "good" boy'
print(strg2)

print("length of strg2",len(strg2))

strg3 = '''line1
line2
line3'''

print(strg3)

print("conctact")
print(strg1+strg2+strg3)

print(strg1 == strg1)
print(strg1 == strg3)

print("string using for loop")

for i in range(0,len(strg1)) :
    print(strg1[i],"\n")

strg1[0]='t'
print(strg1)
print(strg1.upper())
   
