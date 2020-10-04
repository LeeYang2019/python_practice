temps = [222, 235, 667]

new_temps = []

# this is one approach
for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)

#another approach is to use list comprehension

new_temps = [temp / 10 for temp in temps]
print(new_temps)

tmps = [221, 234, 340, -9999, 230]

new_tmps = [tmp / 10 for tmp in tmps if tmp != -9999]

print(new_tmps)

# this returns a section of a string that is converted into a list then back
def returnStr(strng, x):
    return ''.join([l for l in strng if l != x])

print(returnStr('abcdefg', 'a'))

imm = (25, 26, 27, 28)

def returnNum(list, m):
    return [n for n in list if n != m]

print(returnNum((25, 26, 27, 28), 25))

# with if else

def removeNegative(list):
    return [t if t != -9999 else 0 for t in list]

print(removeNegative([221, 234, 340, -9999, 230]))

# with str formatting

def returnSum(list):
    return sum([l if type(l) != str else float(l) for l in list])

print(returnSum([22.5, '23.4']))