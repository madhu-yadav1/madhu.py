sampletuple= (1,2,3,4,5,6)
def squarecube (i):
    if i%2==0:
        return i**2
    else:
        return i**3
result= map(squarecube,sampletuple)
print(tuple(result))


# dictinory in python

phone_no= {'madhu':123,'shiva':354}
print(phone_no)

# if we want to exess a particuar persons phone number
phone_no= {'madhu':123,'shiva':354}
print(phone_no['madhu'])

#dubilicates are not allowed in dict in dict duplicate will take the last element



phone_no= {'madhu':123,
           'shiva':354,
          'madhu':134

}
print(phone_no)

# values are mututable that means we can change the values but not the key in dictionary

phone_no= {'madhu':123,
           'shiva':354,
           'madhu':134
}
print(phone_no)
phone_no ['kingu']= {8888,333333,4444}
#list is also allowed
print(phone_no)
#dictornay also allowed
phone_no['madhu']={'madhu_home':12345,'madhu_work':7890}
print(phone_no.keys())
print(phone_no.values())
print(phone_no.items)
for i in phone_no:
     print(i)
     print(phone_no[i])
for i in phone_no.items():
    print(i)



data = {
    1:'madhu',

    2:'shiva',
    0:'chottu'
}
del data[2]
data.pop(1)
data.clear()
print(data)




