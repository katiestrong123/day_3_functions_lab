# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

# for number in numbers:
#     print(number)

# 2. Print the difference between the largest and smallest value:

# for number in numbers:
#     smallest_num = min(numbers)
#     largest_num = max(numbers)
#     difference = (largest_num - smallest_num) 
    
# print(difference)

# 3. Print True if the list contains a 2 next to a 2 somewhere.

# for number in numbers:
#     if [number == 2 and numbers[-1] == 2]:
#         print(True)
#         break


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

total = 0 
found_6 = False

for number in numbers:
    if number == 6:
        found_6 = True
    elif found_6:
        if number == 7:
            found_6 = False
    else:
        total += number

print(total)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

found_13 = False
for number in numbers:
    if [number == 13 an

 find the index of 13,   add one to that index






