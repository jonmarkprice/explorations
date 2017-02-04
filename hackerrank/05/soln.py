def is_matched(string):
    pair = dict()
    pair[')'] = '('
    pair[']'] = '['
    pair['}'] = '{'
    
    stack = []
    i = len(string) - 1
    while i >= 0:
        if string[i] in (')', ']', '}'):
            stack.append(string[i])
        elif len(stack) > 0 and pair[stack[-1]] == string[i]:
            stack.pop()
        else:
            return False
        i -= 1
    return stack == []
    
