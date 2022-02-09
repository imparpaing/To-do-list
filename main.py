print('Hello')

storeUserName = input('Enter you name: ')

# WELCOME SCREEN
print('\nWelcome, ' + storeUserName)
print('What would you like to do?\n')

# MENU
print('[ 1] Display tasks')
print('[ 2] Write to file')
print('[ 3] Clear file')
print('[ 4] Exit')
print('\n')

storeUserSelection = input('Selection: ')
print('\n')

# TASK SELECTION
if (storeUserSelection != '1' and storeUserSelection != '2' and storeUserSelection != '3' and storeUserSelection != '4'):
    print('Incorrect input')

elif storeUserSelection == '1':
    print('SELECTED => [Read from file]')
    print('TASKS:\n')
    f = open('tasks.txt', 'r')
    print(f.read())

elif storeUserSelection == '2':
    print('SELECTED => [Write to file]\n')
    f = open('tasks.txt', 'a')
    writeToFile = input('Input: ')
    f.write(writeToFile)
    f.write('\n')
    print('Writing to file...')
    f.close()

elif storeUserSelection == '3':
    f = open('tasks.txt', 'w')
    f.write('')
    print('Clearing file...')
    f.close()

elif storeUserSelection == '4':
    print('SELECTED => [Exit]\n')
    print('Exiting...')