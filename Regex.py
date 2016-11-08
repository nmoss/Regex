
from NFA import *
from State import *

def parse_regex(expression):
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


#s = NFA.single_NFA('a')
#print(s.to_string())
s = parse_regex("z(a|b)j")
print(s.to_string())
