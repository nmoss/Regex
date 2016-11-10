class DFA:

    def __init__(self, accept_id):
        self.states = []
        self.regex = ''
        self.accept = accept_id

    def add_state(self, states):
        for s in states:
            if s not in self.states:
                self.states.append(s)

    def get_accept_state(self):
        return self.states[-1]

    def get_start_state(self):
        return self.states[0]

    def to_string(self):
        dfa = 'digraph g {\nrankdir = LR;\nedge [arrowsize=0.8;\n'
        dfa += 'label=\"' + self.regex + '\";\n'
        dfa += 'node [shape=doublecircle]; ' + self.accepting() + '\n'
        dfa += 'node [shape=circle];\n'
        for s in self.states:
            dfa += s.to_string()
        dfa += '}'
        return dfa
    
    def accepting(self):
        res = ''
        for s in self.states:
            for s1 in s.states:
                if s1.id == self.accept:
                    res += s.id + '; '
        return res

    def is_accepting(self, state):
        for s in state.states:
            if s.id == accept:
                return True
        return False

    def match(self, string):
        start = self.get_start_state()
        for c in string:
            nexts = start.next_states(c)
            if nexts == []:
                return False
            start  = nexts[0]
        return self.is_accepting(start)

