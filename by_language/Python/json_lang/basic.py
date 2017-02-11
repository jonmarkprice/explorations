import json

def set_fn(rest):
    var, val = rest
    variables.update({var: val})

def incr_fn(rest):
    var = rest[0]
    variables.update({var: variables[var] + 1})

def and_fn(rest):
    a, b, store = rest
    ans = True if (a and b) else False
    variables.update({store: ans})

def decl_fn(rest):
    for var in rest[0]:
        variables.update({var: None})

program   = [
    ["set", "x", 3],
    ["incr", "x"],
    ["decl", ["a", "b", "c"]],
    ["set", "a", True],
    ["set", "b", True],
    ["and", "a", "b", "c"]

]
known = {
    'set'   : set_fn,
    'incr'  : incr_fn,
    'decl'  : decl_fn,
    'and'   : and_fn
}

variables   = dict()

for line in program:
    print('-' * 30)
    command = line[0]
    rest    = line[1:]
    if command in known:
        result = known[command](rest)
    else:
        print('ERROR: Unkown command')

    for var in variables:
        print(var + ' : ' + str(variables[var]))

