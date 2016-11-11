from DFA import *
from NFA import *
from State import *

def parse_regex(expression):
    expression = expand_classes(expression)
    stack = []
    i = 0
    print('expression', expression)
    while i < len(expression):
        s = NFA()
        symbol = expression[i]
        print(symbol)
        if symbol == '\\':
            i += 1
            symbol = expression[i]
            s = NFA.single_NFA(symbol)
        elif symbol == '*':
            s = stack.pop()
            s = s.kleene()
        elif symbol == '|':
            s = crush(stack)
            i += 1
            sub = expression[i:]
            s1 = parse_regex(sub)
            s = s.union(s1)
            stack.append(s)
            break
        elif symbol == '(':
            pos = match_parens(i, expression)
            i += 1
            sub = expression[i:pos]
            s = parse_regex(sub)
            i = pos
        else:
            s = NFA.single_NFA(symbol)
        stack.append(s)
        i += 1

    s0 = stack.pop()
    while stack != []:
        s1 = stack.pop()
        s0 = s1.concat(s0)
    return s0

def crush(stack):
    s0 = stack.pop()
    while stack != []:
        s1 = stack.pop()
        s0 = s1.concat(s0)
    return s0

def match_parens(start, expression):
    close = start
    count = 1
    while count > 0:
        close += 1
        c = expression[close]
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
    return close

def expand_classes(regex):
    lowers = 'a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z'
    uppers = 'A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z'
    digits = '0|1|2|3|4|5|6|7|8|9'

    if '[a-zA-Z0-9]' in regex:
        regex = regex.replace('[a-zA-Z0-9]', '(' + lowers + '|' + uppers + '|' + digits + ')')
    if '[a-zA-Z]' in regex:
        regex = regex.replace('[a-zA-Z]', '(' + lowers + '|' + uppers + ')')
    if '[0-9]' in regex:
        regex = regex.replace('[0-9]', '(' + digits + ')')
    if '[a-z]' in regex:
        regex = regex.replace('[a-z]', '(' + lowers + ')')
    if '[A-Z]' in regex:
        regex = regex.replace('[A-Z]', '(' + uppers + ')')

    return regex

#s = NFA.single_NFA('a')
#print(s.to_string())
s = parse_regex("z(a|b)j")
print(s.to_string())
s = s.toDFA()
print(s.to_string())
print(s.match('zaj'))
