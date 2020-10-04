def check_sentence(strg):
    strlist = []
    checks = ('.', '?', '!')
    if strg.endswith(checks):
       strlist = list(strg) #convert to str
       strlist.remove(strlist[-1]) #remove last element
       return ''.join(strlist) #rejoin as string
    
def sentence_maker(phrase):
    interrogatives = ["what", "why", "how", "who", "when"]
    interro = tuple(interrogatives)
    capitalized = phrase.capitalize()

    if phrase.startswith(interro):
        return '{}?'.format(check_sentence(capitalized))
    else:
        return '{}.'.format(check_sentence(capitalized))

msg = ''
while True:
    userInput = input('say something: ')
    
    if userInput == 'end':
        break
    else:
        msg += sentence_maker(userInput) + ' '

print(msg)