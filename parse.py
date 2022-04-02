#Group Members: Atharva Mainkar, Jaziel Contreras, Andrew Garcia, Juan Avalos
from collections import deque

#parses out accepted alphabet from file
def get_alphabet(inp):
    stack = deque()
    count = -2
    out = ""
    for char in inp:
        if char == "(":
            stack.append(char)                          #stack appends open parentheses              
            count += 1
        elif char == ")":                               #stack pops out the previous parentheses
            stack.pop()
        elif count == 1:
            out += char
        if count > 1:
            alphabet = out.split(",")
            while("" in alphabet):                      #removes emptys in alphabet list
                alphabet.remove("")
            return alphabet

#parses out states from file
def get_states(inp):
    stack = deque()
    count = -2
    out = ""
    for char in inp:
        if char == "(":
            stack.append(char)                          #appends open parentheses to stack
            count += 1
        elif char == ")":
            stack.pop()                                 #pops most recent open parentheses
        elif count == 2:
            out += char
        if count > 2:
            states = out.split(",")
            while("" in states) :
                states.remove("")                       #removes emptys in states list
            return states[:-1]

#parses out start state from file
def get_start_state(inp):
    stack = deque()
    count = -2
    out = ""
    for char in inp:
        if char == "(":
            stack.append(char)                          #appends open parentheses to stack
            count += 1
        elif char == ")":
            stack.pop()                                 #pops most recent parentheses from stack
        elif count == 2:
            out += char
        if count > 2:
            states = out.split(",")
            while("" in states) :
                states.remove("")                       #removes emptys in from start state
            return states[-1]

#parses out end states from file
def get_end_states(inp):
    stack = deque()
    count = -2
    out = ""
    for char in inp:
        if char == "(":                                #appends open parentheses to stack
            stack.append(char)
            count += 1
        elif char == ")":                              #pops most recent open parentheses from stack
            stack.pop()
        elif count == 3:
            out += char
        if count > 3:
            end_states = out.split(",")
            while("" in end_states) :
                end_states.remove("")                  #removes emptys from end states
            return end_states

#parses out state transitions from file
def get_state_transitions(inp):
    stack = deque()
    count = 0
    out = ""
    for char in inp:
        if char == "(":
            stack.append(char)                          #appends open parenthses to stack
            count += 1
        elif char == ")":
            stack.pop()                                 #pops most recent open parentheses from stack
            count -= 1
        if count >= 4:
            out += char
    str_list = out.split("(")
    while("" in str_list) :
        str_list.remove("")                             #removes emptys from str_list
    transition_list = []
    for i in str_list:
        temp = i.split(",")
        transition_list.append(temp)
    return transition_list                              #transition list is a list of lists which contains possible transitions from state to state

#parses out beta from file
def get_computation_strings(inp):
    stack = deque()
    count = 0
    out = ""
    for char in reversed(inp):
        if char == ")":                                        #appends close parentheses
            stack.append(char)
            count += 1
        elif char == "(":                                      #appends open parentheses
            stack.pop()
        if count == 2:
            out += char
        if count > 2:
            out = out[::-1]
            out = out.replace(")", "")
            out = out.replace("(", "")
            computation_strings = out.split(",")
            if computation_strings == ["", ""]:                 #if our computation_strings contains nothing return None
                return None
            while("" in computation_strings) :                  
                computation_strings.remove("")                  #removes emptys from computation_strings
            return computation_strings                          #assuming commputation_strings contains inputs they will be returned here