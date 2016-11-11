class State(object):
    
    def __init__(self, transitions=[], name=0, states=set()):
        self.transitions = transitions
        self.name = name
        self.states = states

    def next(self, character):
        next_states = []
        for (x, y) in self.transitions:
            if x == character:
                next_states.append(y)
        return next_states

    def alphabet(self):
        alphabet = []
        for (x, y) in self.transitions:
            alphabet.append(x)
        return alphabet

    def add_transition(self, character, state):
        self.transitions.append((character, state))

    def to_string(self):
        s = ""
        for (key, value) in self.transitions:
            s += "\t" + str(self.name) + " -> " + str(value.name) + " [label=" + "\"" + key + "\"" + "];" + "\n"
        return s

    
t = {}
t['a'] = 1
t['b'] = 2
s = State(t,0)

