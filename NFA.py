from State import *
from Counter import *

class NFA:

    eps = "$"
    counter = Counter()
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

    @classmethod
    def single_NFA(cls, c):
        s = NFA()
        s0 = State([],NFA.counter.get_next_id())
        s1 = State([],NFA.counter.get_next_id())
        s0.add_transition(c, s1)
        s.add_state([s0,s1])
        return s
    
    def closure(self, start):
        out = []
        out.append(start)
        nexts = start.next(NFA.eps)
        for s in nexts:
            out.append(s)
            out += closure(s)
        return set(out)
    
    def move(self, start, c):
        return set(start.next(c))

    def toDFA(self):
        alphabet.remove("$")
        result = DFA(self.get_accept_state().id)
        new_start = State(closure(self.get_start_state()))
        result.add_state(new_start)
        visited.append(closure(self.get_start_state())
        self.dfa_next(closure(self.get_start_state()),new_start,result,visited)

        return result

    def dfa_next(states, start, result, visited):
        for c in self.alphabet:
            nexts = []
            closed = []
            for s in states:
                nexts += self.move(s,c)
                for sj in nexts:
                    closed += self.closure(sj)
            nexts = set(nexts)
            closed = set(closed)
            if closed == states:
                start.add_transition(c, start)
            elif not len(closed) == 0:
                if closed not in visited:
                    s1 = State(closed)
                    start.add_transition(c, s1)
                    result.add_state(s1)
                    visited.append(closed)
                    self.dfa_next(closed,s1,result,visited)
                else:
                    s1 = get_state_containing(closed,result)
                    start.add_transition(c,s1)

    def get_state_containing(self, closed, dfa):
        for s in dfa.states:
            if s.states == closed:
                return s
        return None


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
        start = State([], NFA.counter.get_next_id())
        done = State([], NFA.counter.get_next_id())
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

    def union(self, nfa):
        result = NFA()
        start = State([], NFA.counter.get_next_id())
        done = State([], NFA.counter.get_next_id())
        start.add_transition(NFA.eps, self.get_start_state())
        start.add_transition(NFA.eps, nfa.get_start_state())
        accept = self.get_accept_state()
        b_accept = nfa.get_accept_state()
        accept.add_transition(NFA.eps, done)
        b_accept.add_transition(NFA.eps, done)
        result.add_state([start])
        for s in self.states:
            result.add_state([s])
        for s in nfa.states:
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

