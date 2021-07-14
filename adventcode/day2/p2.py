#Extract list of passcodes from file and place in dictionary
def extract_list_file(the_file):
    opened_file = open(the_file)
    passcodes = []
    
    for line in opened_file:
        line = line.rstrip()
        words = line.split(' ')
        
        position_one, position_two = words[0].split('-')
        position_one = int(position_one) 
        position_two = int(position_two) 
        letter = words[1][:-1]
        passcode = words[2]
        passcodes.append({'position_one': position_one, 'position_two': position_two, 'letter': letter, 'passcode': passcode})

    opened_file.close()
    return passcodes

def code_checker(passcodes):
    count_correct = 0
    for line in passcodes:
        if line['passcode'][line['position_one'] - 1] == line['letter'] and line['passcode'][line['position_two'] -1] == line['letter']:
            print('nope')
        elif line['passcode'][line['position_one'] - 1] == line['letter']:
            count_correct += 1
        elif line['passcode'][line['position_two'] -1] == line['letter']:
            count_correct +=1
        else: 
            print('nope')        
    return count_correct
            
passcodes = extract_list_file("passcodes.txt")

print(code_checker(passcodes))
