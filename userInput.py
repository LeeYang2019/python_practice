def tempChecker(temp):
    if temp > 5:
        return 'hot'
    return 'cold'

#userInput = input('Enter input: ') #input is str, has to be converted
#print(tempChecker(float(userInput)))

name = input('Enter name: ')
surName = input('Enter surName: ')

message = "hello %s %s" % (name, surName) #older way to format string

qmessage = f'hello {name} {surName}' #new way to format string post python 3.8

print(message) #older way to format string
