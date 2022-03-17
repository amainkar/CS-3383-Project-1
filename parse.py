from collections import deque

def get_alphabet(inp):
    stack = deque()
    count = -2
    out = ""
    for char in inp:
        if char == "(":
            stack.append(char)
            count += 1
        elif char == ")":
            stack.pop()
        elif count == 1:
            out += char
        if count > 1:
            alphabet = out.split(",")
            while("" in alphabet):
                alphabet.remove("")
            return alphabet


def get_states(inp):
    stack = deque()
    count = -2
    out = ""
    for char in inp:
        if char == "(":
            stack.append(char)
            count += 1
        elif char == ")":
            stack.pop()
        elif count == 2:
            out += char
        if count > 2:
            states = out.split(",")
            while("" in states) :
                states.remove("")
            return states[:-1]

def get_start_state(inp):
    stack = deque()
    count = -2
    out = ""
    for char in inp:
        if char == "(":
            stack.append(char)
            count += 1
        elif char == ")":
            stack.pop()
        elif count == 2:
            out += char
        if count > 2:
            states = out.split(",")
            while("" in states) :
                states.remove("")
            return states[-1]

def get_end_states(inp):
    stack = deque()
    count = -2
    out = ""
    for char in inp:
        if char == "(":
            stack.append(char)
            count += 1
        elif char == ")":
            stack.pop()
        elif count == 3:
            out += char
        if count > 3:
            end_states = out.split(",")
            while("" in end_states) :
                end_states.remove("")
            return end_states

def get_state_transitions(inp):
    stack = deque()
    count = 0
    out = ""
    for char in inp:
        print(char,end="")
        if char == "(":
            stack.append(char)
            count += 1
        elif char == ")":
            stack.pop()
            count -= 1
        if count >= 4:
            out += char
    print(out)
    return out