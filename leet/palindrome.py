x = 1234321

def palindrome(x):

    return False if x < 0 else x == int(str(x)[::-1])


    # x = str(x)
    # length = len(x)
            
    # if length == 1:
    #     return True    
    # if int(x) < 0:
    #     return False    

    # if length % 2 != 0:
    #     odd = 1

    # middle = int(length/2) + odd        
    # first_half = x[:middle]   
    # print(first_half)     
    # second_half = x[middle - odd:] 
    # print(second_half[::-1])     

    # if first_half == second_half[::-1]:
    #     return True
    # else:
    #     return False