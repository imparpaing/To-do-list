from os.path import exists

file_exists = exists('userName.txt')

# WELCOME SCREEN
if file_exists == False:
    print('Hello')
    storeUserName = input('Enter your name: ')

    f = open('userName.txt', 'w')
    f.write(storeUserName)

    with open('userName.txt', 'r') as f:
        storeUserName = f.read().rstrip()
        
    print('\nWelcome, ' + str(storeUserName))
    print('What would you like to do?\n')

    f.close()

# IF 'USERNAME.TXT' FILE WAS FOUND SKIP CREATING THE USERNAME
else:
    with open('userName.txt', 'r') as f:
        storeUserName = f.read().rstrip()

    print('\nWelcome, ' + str(storeUserName))
    print('What would you like to do?\n')
    f.close()
    
# MENU
print('[ 1] Display tasks')
print('[ 2] Write to file')
print('[ 3] Clear file')
print('[ 4] Exit')
print('\n')

storeUserSelection = input('Selection: ')

# TASK SELECTION
if (storeUserSelection != '1' and storeUserSelection != '2' and storeUserSelection != '3' and storeUserSelection != '4'):
    print('Incorrect input')

elif storeUserSelection == '1':
    print('SELECTED => [Read from file]\n')
    print('TASKS:\n')
    f = open('tasks.txt', 'r')
    print(f.read())

elif storeUserSelection == '2':
    print('SELECTED => [Write to file]\n')
    f = open('tasks.txt', 'a')
    writeToFile = input('Input: ')
    f.write(writeToFile + '\n')
    print('Writing to file...')
    f.close()

elif storeUserSelection == '3':
    print('SELECTED => [Clear file]\n')
    f = open('tasks.txt', 'w')
    f.write('')
    print('Clearing file...')
    f.close()

elif storeUserSelection == '4':
    print('SELECTED => [Exit]\n')
    print('Exiting...')