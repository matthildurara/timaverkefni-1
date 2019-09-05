# get an integer input for the lenght of the sequence
# create a loop that happens as many times as the input says
# figure out a rule that calculate the numbers you want to print out

n = int(input("Enter the length of the sequence: "))
sum_num = 0
for i in range(1,n + 1):
    if i == 1:
        first = 1
        second = 0
        third = 0
        sum_num = first + second + third
        print(sum_num)
    elif i == 2:
        first = 0
        second = 2
        third = 0
        sum_num = first + second + third
        print(sum_num)
    elif i == 3:
        first = 1
        second = 2
        third = 3
        sum_num = first + second
        print(sum_num)
    else: 
        first =  second
        second = third
        third = sum_num
        sum_num = first + second + third
        print(sum_num)
        



