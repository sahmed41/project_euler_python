def  multiplesOf3Or5(number):
    total = 0

    for i in range(3,number):
        if (((i  % 3) == 0) or ((i % 5) == 0)): 
            print(i)           
            total += i
    
    return total


print("Total:", multiplesOf3Or5(1000))