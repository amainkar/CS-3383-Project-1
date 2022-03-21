import parse

filename = input("Please input the file name:")

f = open(filename, "r")
file_inp = ""
for x in f:
    file_inp += x

file_inp = file_inp.replace("\n","").replace(" ","")

alphabet = parse.get_alphabet(file_inp)
states = parse.get_states(file_inp)
start_state = parse.get_start_state(file_inp)
end_states = parse.get_end_states(file_inp)
transitions = parse.get_state_transitions(file_inp)
computation_strings = parse.get_computation_strings(file_inp)

transition_dictionary  = {}

for state in states:
    transition_dictionary[state] = {}

for transition in transitions:
    if transition[1] not in transition_dictionary[transition[0]]:
        transition_dictionary[transition[0]][transition[1]] = [transition[2]]
    else:
        transition_dictionary[transition[0]][transition[1]].append(transition[2])

def NFA_process(input_str, state):
    if input_str == "" and  state not in end_states:
        return False
    if input_str == "" and state in end_states:
        return True
    current_char = input_str[0]
    if current_char not in transition_dictionary[state]:
        return False
    valid_tree = False
    for next_state in transition_dictionary[state][current_char]:
        valid_tree = valid_tree or NFA_process(input_str[1:],next_state)
    return valid_tree

def empty_beta():
    while True:
        input_str = input("Please input a string:")
        if input_str == "":
            print("Bye bye.")
            break
        if (NFA_process(input_str,start_state)):
            print("Accepted.")
        else:
            print("Rejected.")

if computation_strings == None:
    empty_beta()
else:
    out_str = "("
    for string in computation_strings:
        if (NFA_process(string,start_state)):
            out_str += " accepted,"
        else:
            out_str += " rejected,"
    print(out_str[:-1]+")")
        

#print(transitions, computation_strings)
#print(states, start_state, end_states)