# 
# Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.
# 
# input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]
# 
# output: [3, 6, 7] # since only these three values are both in arr1 and arr2
# 
# */

#                          V
arr1 = [1, 2, 3, 5, 6, 7, 20]
arr2 = [3, 6, 7, 8, 20]
#                    ^           

#if I'm comparing 1 & 3, I should know that the rest of the numbers in arr2, are larger than that, and I should move to the next number in arr1
# if I'm comparing 3 & 3 or a match, I should append it to the duplicates array and move to the next number in arr1
# if I'm comparing number 5 & 3, and 5 > 3, we check the next number in array 2


def findDuplicates(arr1, arr2):
    
    duplicates = []
    tracker1 = 0
    tracker2 = 0
    
    while tracker1 < len(arr1) or tracker2 < len(arr2):
        if arr1[tracker1] < arr2[tracker2]:
            tracker1 += 1
        if arr1[tracker1] == arr2[tracker2]:
            duplicates.append(arr1[tracker1])
            tracker1 += 1
            tracker2 += 1
        if arr[tracker1] > arr2[tracker2]:
            tracker2 += 1
    
    return duplicates
#     duplicates = []
    
#     for item in arr1: 
#         if item in arr2:
#             duplicates.append(item)
    
#     return duplicates

print(findDuplicates(arr1, arr2))

