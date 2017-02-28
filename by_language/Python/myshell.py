from subprocess import call
from functools import reduce

def main():
    print('Welcome to my shell, type "exit" to quit.')
    prompt()

def prompt():
    # Read a line from stdin
    prompt = '> '
    line = input(prompt)

    while line != 'exit':
        print('You entered "' + line + '".')
        args = line.split(' ')
        
        #print(reduce(lambda w, ws: ws + '[' + str(w) + ']', args))
        #for arg in args:
        #    print('[' + arg + ']', end="")
        
        #lex(line)
        print() # print a newline
        call(args)

        line = input(prompt)
    print('Goodbye!')
                                  
def lex(string):
    # split chars
    for c in list(string):                                                                 print('[' + c + ']', end='')

if __name__ == '__main__':
    main()

# TODO
'''
    [ ] shell expansions (e.g. "*.txt")
        | Can use something in `os` I think
    [ ] history
    [ ] line editing
    [ ] custom syntax (lisp like or my custom syntax)
    [ ] ability to end blank lines (without trying to excute!)
'''

