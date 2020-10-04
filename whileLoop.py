a = 5
while a > 1:
    print('hello')
    a -= 1

userInput = ''
while userInput != 'Lee':
    userInput = input('Enter a name: ')
    print('hello {}'.format(userInput)) #great option for single inputs
    print(f'Nice to meet you, {userInput}') #great in general   

print('program ended because you entered the name %s' %(userInput)) #requires more

n = 1
while True:
    n += 1
    print('n: ', n)
    userName = input('Enter a name: ')
    if userName == 'Lee':
        break
    else:
        continue
    