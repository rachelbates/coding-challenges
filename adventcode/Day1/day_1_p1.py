

#Extract list of numbers from file
def extract_list_file(the_file):
    opened_file = open(the_file)
    numbers = []
    
    for line in opened_file:
        numbers.append(line.rstrip())

    opened_file.close()
    return numbers


#Find 2 entries that total to the sum
def find_two_entries(numbers, target_sum):
    for num in numbers:
        for num2 in numbers:
            if int(num) + int(num2) == int(target_sum):
                print('yes')
                return num, num2

#multiply 2 numbers
def multiply(a, b):
    return int(a) * int(b)

numbers_list = extract_list_file("./testdata.txt")

num1, num2 = find_two_entries(numbers_list, '2020')

print(multiply(num1, num2))