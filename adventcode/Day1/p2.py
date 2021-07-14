

#Extract list of numbers from file
def extract_list_file(the_file):
    opened_file = open(the_file)
    numbers = []
    
    for line in opened_file:
        numbers.append(int(line.rstrip()))

    opened_file.close()
    return numbers


# #Find 2 entries that total to the sum
# def find_three_entries(numbers, target_sum):
#     for num in numbers:
#         for num2 in numbers:
#             if int(num) + int(num2) == int(target_sum):
#                 print('yes')
#                 return num, num2, num3

def part2(entries):
    rests = {}
    for x in entries:
        for y in entries:
            rests[x + y] = x * y

    for x in entries:
        rest = 2020 - x
        if rest in rests:
            print(x * rests[rest])
            return x * rests[rest]
            
#multiply 2 numbers

numbers_list = extract_list_file("./testdata.txt")

part2(numbers_list)
