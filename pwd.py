import numpy as np
import matplotlib.pyplot as plt
import sys
import time

# env: exit
def exit(user):
    print(' Goodbye, {}!'.format(user))
    print(' System shutdown ...')
    time.sleep(1)
    sys.exit()

# env: start
def start():
    user = input(' Please enter your name: ')
    time.sleep(1)
    print(' Hi, {}. Welcome.'.format(user))
    time.sleep(0.3)
    print((' This small program will challenge you with some questions.\n'
           ' If you answer the question correctly, the system will give\n'
           ' you some hints that will help you decrypt the PDF as rewards.'))
    time.sleep(1)
    response = input(' Are you ready for the challenge? [yes/no] '.format(user))
    time.sleep(1)
    if response == 'yes':
        print(' Great! Let us get started.')
        time.sleep(1)
        print(' hint: Type `help` to find out more information about commands.')
        return user, 0, 0
    else:
        exit(user)

# env: finish
def finish():
    print(' You are ready to decrypt PDF.')

# func: display image in figure/
def display_img(fname):
    img = plt.imread('./figure/'+fname)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

# cmd: ls
def ls(now_at):
    if now_at == 0:
        print('')
    elif now_at == 1:
        print(' decode.png')
    elif now_at == 2:
        print(' decode.png    cipher.png')
    else:
        print(' decode.png    cipher.png    pwd.txt')

# cmd: display
def display(fname, unlock_level):
    if not fname:
        print(' Usage: display [image.png]')
    elif fname == 'decode.png':
        if unlock_level < 1:
            print(' The image is locked. Please unlock it.')
        else:
            print(' displaying {}...'.format(fname))
            display_img(fname)
    elif fname == 'cipher.png':
        if unlock_level < 2:
            print(' The image is locked. Please unlock it.')
        else:
            print(' displaying {}...'.format(fname))
            display_img(fname)
    else:
        print(' Image does not exist.')

# cmd: cat
def cat(fname):
    if not fname:
        print(' Usage: cat [file.txt]')
    elif fname == 'pwd.txt':
        print(' altair')
    else:
        print(' File does not exist')

# cmd: unlock 
def unlock(fname, unlock_level):
    key1 = 'I Zwicky 18'
    key2 = 'Demo-2'
    quit = 'quit'
    if not fname:
        print(' Usage: unlock [image.png]')
        return unlock_level
    elif fname == 'decode.png':
        if unlock_level >= 1:
            print(' The image is already unlocked.')
            return unlock_level
        else:
            print(' key to unlock {}: I ______ 18  (enter quit to quit)'.format(fname))
            key = input(' > ')
            if key == key1:
                print(' Unlock {}.'.format(fname))
                return unlock_level + 1
            elif key == quit:
                return unlock_level
            else:
                print(' Incorrect key.')
                return unlock_level
    elif fname == 'cipher.png':
        if unlock_level >= 2:
            print(' The image is already unlocked.')
            return unlock_level
        else:
             print(' key to unlock {}: D___-_  (enter quit to quit)'.format(fname))
             key = input(' > ')
             if key == key2:
                 print(' Unlock {}.'.format(fname))
                 return unlock_level + 1
             elif key == quit:
                 return unlock_level
             else:
                 print(' Incorrect key.')
                 return unlock_level
    else:
        print(' Image doese not exist.')
        return unlock_level

# action: write
def write():
    with open('decryption.txt','w') as f:
        f.write('\n')
        f.write('pllsefro bs BfAwmaqiFchmAzlgxrufoy')

# challenge 1
def challenge1(user):
    correct = '20 05 1990'
    var = False
    print(' Challenge 1:')
    print(' When is the Hubble first light? (DD MM YYYY) ')
    while not var:
        ans = input(' > ')
        if ans == 'exit':
            exit(user)

        if ans == correct:
            print(' Correct!')
            print(' 09 34 0.9  +55 14 34.19  14Mpc') # I Zwicky 18
            var = True
        else:
            print(' Incorrect. Try again~')

# challenge 2
def challenge2(user):
    correct = 'Falcon 9'
    var = False
    print(' Challenge 2:')
    print(' World first orbital reusable rocket? ')
    while not var:
        ans = input(' > ')
        if ans == 'exit':
            exit(user)

        if ans == correct:
            print(' Correct!')
            print(' 20:33 UTC  LC-39A, Kennedy Space Center, Florida')
            var = True
        else:
            print(' Incorrect. Try again~')

# challenge 3
def challenge3(user):
    correct = 'Aquila'
    var = False
    print(' Challenge 3:')
    print(' What constellation NGC 6803 locates in?')
    while not var:
        ans = input(' > ')
        if ans == 'exit':
            exit(user)

        if ans == correct:
            print(' Correct!')
            var = True
        else:
            print(' Incorrect. Try again~')
    
    print(' Generating file...')
    write()
    time.sleep(2)
    print(' ...done.')

# condition
def condition(now_at, unlock_level, user):
    if now_at == 0:
        challenge1(user)
        return now_at + 1
    elif (now_at == 1) & (unlock_level == 1):
        challenge2(user)
        return now_at + 1
    elif (now_at == 2) & (unlock_level == 2):
        challenge3(user)
        return now_at + 1
    elif (now_at == 3):
        time.sleep(1)
        finish()
        return now_at + 1
    else:
        return now_at

# command
def command(cmd, now_at, unlock_level, user):
    space = cmd.split()
    if len(space) > 1:
        cmd, fname = cmd.split()
    else:
        fname = ''

    if cmd == 'help':
        display_img('help.png')
    elif cmd == 'ls':
        ls(now_at)
    elif cmd == 'display':
        display(fname, unlock_level)
    elif cmd == 'unlock':
        unlock_level = unlock(fname, unlock_level)
    elif cmd == 'exit':
        now_at = exit(user)
    elif cmd == 'cat':
        cat(fname)
    return now_at, unlock_level, fname

# main
if __name__ == '__main__':
    user, now_at, unlock_level = start()
    while True:
        cmd = input(' > ')
        now_at, unlock_level, fname = command(cmd, now_at, unlock_level, user)
        now_at = condition(now_at, unlock_level, user)
