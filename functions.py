def getMean(obj):
    if type(obj) == dict:
        return sum(obj.values()) / len(obj)
    return sum(obj) / len(obj)

#getting th mean with a list, otherwise known as an array
print(getMean([1,2,3,5]))

#getting the mean with a dictionary
print(getMean({"tom": 20, "cathy": 35}))

#getting the mean with a tuple
print(getMean((1,2,3,4)))

def getValue(num):
    if type(num) == str:
        return 'value is a string. try again'
    else:
        if num <= 5:
            return 'less than 5'
        return 'equal to or greater than 5'


print(getValue(7))
print(getValue('age'))

def foo(x, array):
    if x in array:
        return True
    else:
        return False
 
print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3])) #there is no implicit conversion

def getInstance(x):
    if isinstance(x, int) or isinstance(x, float) or x=='1':
        return "Valid type!"
    elif isinstance(x, list) or isinstance(x, dict):
        return "structure"
    return "Not valid!"

# expect list to return structure
print(getInstance([1,2,3]))

# expect tuple to return not valid
print(getInstance((24, 25)))