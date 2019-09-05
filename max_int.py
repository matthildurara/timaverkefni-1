#Get an integer in input
#declare max_int to 0
#check to see if the input is a negative number, 
# then the loop will end and print out max_int
##compare the input to the max_int to see if is is higher, 
# if it is higher then it will get the value of the input

number = int(input("Enter an input: "))
max_int = 0

while number > 0:
    if number > max_int:
        max_int = number
        number = int(input("Enter an input: "))
print(max_int)