tmpList = [3, 7.8, 9.5, 10.2]
tmpList = tuple(tmpList)
print(type(tmpList))

for temp in tmpList:
    print(round(temp))

for letter in 'hello':
    print(letter.upper())

def celsius_to_fahrenheit(cels):
    return round((cels * 5/9) + 53)

for temperature in tmpList:
    print(celsius_to_fahrenheit(temperature))

# --------------------------------------------------
contacts = {"lee" : 4166483567, "mao" : 4166482197}

for key,value in contacts.items(): #returns both the key and value in the items
    print('{} has phone {}'.format(key, value))

#OR

for pair in contacts.items():
    print('{} has phone {}'.format(pair[0], pair[1]))

for key in contacts.keys(): #returns the key
    print(key)

for value in contacts.values(): #returns the value
    print(value)

a = 5


