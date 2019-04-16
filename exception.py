import sys

try:
    s = raw_input('Enter something -->')
except EOFError:
    print('\nWhy did you do an EOF on me?')
    sys.exit()
except:
    print('some exception occurred')

print('done')
