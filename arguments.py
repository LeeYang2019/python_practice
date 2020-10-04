# a, b are non-keyword arguments or positional arguments 
# where the first argument is a and the second is b
def returnSum(a, b): #default argument always go after non-defauly arguments, b has to go before a
    return a + b

# a, b are keyword arguments 
def returnProduct(a = 2, b = 5):
    return a * b

print(returnProduct(6, 2))
print(returnProduct(b = 5, a = 2))
print(returnProduct()) #can be empty in which case a = 2 and b = 5

def mean(a, b, c, d, e, f): #messy way to write this
    return (a + b + d + e + f) / 6

print(mean(1,2,3,4,5,6))

def meaner(*args): #function with arbitrary # of argument
    return sum(args)/len(args) 

#print(meaner(2,5,6,7,8,8,12))
print(meaner(2,5,6,7,8,8,12, 3))

def returnSome(**kwargs):
    return kwargs

# error below since it requires keyword arguments
# print(returnSome(1,2,3,4))
print(returnSome(a = 1, b = 2, c = 3)['a']) #this returns a dictionary; i'm accessing the set

def find_sum(**kwargs):
    return sum(kwargs.values()) #since we get dictionary, to sum values we need to access the dictionary values
    
print(find_sum(a = 2, b = 3, c = 4))