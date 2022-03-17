import parse

filename = input("Please input the file name:")

f = open(filename, "r")
file_inp = ""
for x in f:
    file_inp += x

file_inp = file_inp.replace("\n","").replace(" ","")
print(file_inp)

alphabet = parse.get_alphabet(file_inp)
states = parse.get_states(file_inp)
start_state = parse.get_start_state(file_inp)
end_states = parse.get_end_states(file_inp)

transitions = parse.get_state_transitions(file_inp)

print(states, start_state, end_states)