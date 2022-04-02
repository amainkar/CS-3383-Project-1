#Group Members: Atharva Mainkar, Jaziel Contreras, Andrew Garcia, Juan Avalos
import parse

filename = input("Please input the file name:")

f = open(filename, "r")
file_inp = ""
for x in f:
    file_inp += x                                                               #appends contents of file to a string

file_inp = file_inp.replace("\n","").replace(" ","")                            #removes spaces and new lines

alphabet = parse.get_alphabet(file_inp)                                            
states = parse.get_states(file_inp)
start_state = parse.get_start_state(file_inp)
end_states = parse.get_end_states(file_inp)
transitions = parse.get_state_transitions(file_inp)
computation_strings = parse.get_computation_strings(file_inp)

transition_dictionary  = {}

for state in states:
    transition_dictionary[state] = {}                                           #instantiate a dictionary of dictionaries

for transition in transitions:
    if transition[1] not in transition_dictionary[transition[0]]:               #creates possible routes of NFA
        transition_dictionary[transition[0]][transition[1]] = [transition[2]]
    else:
        transition_dictionary[transition[0]][transition[1]].append(transition[2])

def NFA_process(input_str, state):
    if input_str == "" and  state not in end_states:                            ##end of the input string and the state we are on is not an end state
        return False
    if input_str == "" and state in end_states:                                 ##end of the input string and the state we are on is not an end state
        return True
    current_char = input_str[0]
    if current_char not in transition_dictionary[state]:                        #if current character is not in our dictionary
        return False
    valid_tree = False
    for next_state in transition_dictionary[state][current_char]:               #assuming our next state is in our dictionary 
        valid_tree = valid_tree or NFA_process(input_str[1:],next_state)        #then we recurse until we reach the end of our input string
    return valid_tree

##this function is used in the case that our beta is empty
def empty_beta():
    while True:
        input_str = input("Please input a string:")                             #user input
        if input_str == "":
            print("Bye bye.")
            break
        if (NFA_process(input_str,start_state)):                 
            print("Accepted.")
        else:
            print("Rejected.")

if computation_strings == None:                                                 #if beta is empty call empty_beta()
    empty_beta()
else:
    out_str = "("                                                               #out_str will contain all boolean values of strings in beta
    for string in computation_strings:
        if (NFA_process(string,start_state)):
            out_str += " accepted,"
        else:
            out_str += " rejected,"
    print(out_str[:-1]+")")   