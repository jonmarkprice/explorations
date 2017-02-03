from subprocess import call

prompt = '> '
line = input(prompt)
while line != 'exit':
    args = line.split(' ')
    call(args)
    line = input(prompt)

