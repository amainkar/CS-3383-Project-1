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
    str_list = out.split("(")
    while("" in str_list) :
        str_list.remove("")
    transition_list = []
    for i in str_list:
        temp = i.split(",")
        transition_list.append(temp)
    return transition_list


def get_computation_strings(inp):
    stack = deque()
    count = 0
    out = ""
    for char in reversed(inp):
        if char == ")":
            stack.append(char)
            count += 1
        elif char == "(":
            stack.pop()
        if count == 2:
            out += char
        if count > 2:
            out = out[::-1]
            out = out.replace(")", "")
            out = out.replace("(", "")
            computation_strings = out.split(",")
            if computation_strings == ["", ""]:
                return None
            while("" in computation_strings) :
                computation_strings.remove("")
            return computation_strings