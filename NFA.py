
class NFA:

    eps = "$"

    def __init__(self):
        self.regex = ""
        self.alphabet = set()
        self.states = []

    def add_state(self, states):
        for s in states:
            self.states.append(s)
            for c in s.alphabet():
                self.alphabet.add(c)

    def get_accept_state(self):
        if self.states == []:
            return "empty"
        return self.states[-1]

    def get_start_state(self):
        return self.states[0]

    # Concatenates this NFA with another nfa
    # adds an epsilon transition between this accept state and new start state.
    def concat(self, nfa):
        result = NFA()
        for state in self.states:
            result.add_state([state])
        f = result.get_accept_state()
        s = nfa.get_start_state()
        f.add_transition(NFA.eps, s)
        for state in nfa.states:
            result.add_state([state])
        return result

    def kleene(self):
        result = NFA()
        start = State()
        done = State()
        start.add_transition(NFA.eps, done)
        start.add_transition(NFA.eps, self.get_start_state())
        accept = self.get_accept_state()
        accept.add_transition(NFA.eps, done)
        accept.add_transition(NFA.eps, self.get_start_state())
        result.add_state([start])
        for s in self.states:
            result.add_state([s])
        result.add_state([done])
        return result

    def to_string(self):
        nfa = "digraph g {\nrankdir = LR;\nedge [arrowsize=0.8];\n"
        nfa += "label=\"" + self.regex + "\";\n"
        accept_state = self.get_accept_state()
        print(accept_state)
        nfa += "node [shape=doublecircle]; " + str(accept_state.name) + ";\n"
        nfa += "node [shape=circle];\n"
        for s in self.states:
            nfa += s.to_string()
        nfa += "}"
        return nfa


