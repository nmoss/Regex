
from NFA import *
from State import *

state_ids = 0

def parse_regex(expression):
    stack = []
    i = 0
    while i < len(expression):
        s = NFA()
        symbol = expression[i]
        if symbol == '\\':
            i += 1
            symbol = expression[i]
            s = NFA.single_NFA(symbol)
        elif symbol == '*':
            s = stack.pop()
            print(stack)
            s = s.kleene()
        else:
            s = NFA.single_NFA(symbol)
        stack.append(s)
        i += 1

    s0 = stack.pop()
    while stack != []:
        s1 = stack.pop()
        s0 = s1.concat(s0)
    return s0

'''
def get_next_id():
    global state_ids
    x = state_ids
    state_ids += 1
    return x

def single_NFA(c):
    s = NFA()
    s0 = State([],get_next_id())
    s1 = State([],get_next_id())
    s0.add_transition(c, s1)
    s.add_state([s0,s1])
    return s;
'''

s = NFA.single_NFA('a')
print(s.to_string())
s = parse_regex('a*')
print(s.to_string())
