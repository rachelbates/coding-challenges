#Extract list of passcodes from file and place in dictionary
def extract_list_file(the_file):
    opened_file = open(the_file)
    passcodes = []
    
    for line in opened_file:
        line = line.rstrip()
        words = line.split(' ')
        
        amount_min, amount_max = words[0].split('-')
        letter = words[1][:-1]
        passcode = words[2]
        passcodes.append({'amount_min': amount_min, 'amount_max': amount_max, 'letter': letter, 'passcode': passcode})

    opened_file.close()
    return passcodes

def code_checker(passcodes):
    count_correct = 0
    for line in passcodes:
        count_in_pc = line['passcode'].count(line['letter'])
        if count_in_pc >= int(line['amount_min']) and count_in_pc <= int(line['amount_max']):
            count_correct += 1
    return count_correct
            

passcodes = extract_list_file("passcodes.txt")

print(code_checker(passcodes))
