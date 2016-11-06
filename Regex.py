
from NFA import *
from State import *

state_ids = 0

def parse_regex(expression):
    stack = []
    for symbol in expression:
        s = NFA()
        if symbol == '\\':
            s = single_NFA(symbol)
        else:
            s = single_NFA(symbol)
        stack.append(s)

    s0 = stack.pop()
    while stack != []:
        s1 = stack.pop()
        s0 = s1.concat(s0)
    return s0

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


s = single_NFA('a')
print(s.to_string())
s = parse_regex('abcdef')
print(s.to_string())
