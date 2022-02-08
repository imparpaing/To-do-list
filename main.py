print('Hello')

storeUserName = input('Enter you name: ')

print('\nWelcome, ' + storeUserName)
print('What would you like to do?\n')

print('[ 1] Display tasks')
print('[ 2] Write to file')
print('[ 3] Exit')
print('\n')

storeUserSelection = input('Selection: ')

if (storeUserSelection != '1' and storeUserSelection != '2' and storeUserSelection != '3'):
    print('Incorrect input')

elif storeUserSelection == '1':
    print('One')

elif storeUserSelection == '2':
    print('Two')

elif storeUserSelection == '3':
    print('Three')