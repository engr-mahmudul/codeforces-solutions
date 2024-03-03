import math
test_case = int(input())
array_container = [None]*test_case
for i in range(test_case):
    array_container[i] = int(input())
for number in array_container:
    flag = 0
    if number == 0 or number == 1:
        flag = 0
    elif number == 2:
        flag = 1
    else:
        for j in range(3, int(number ** 0.5) + 1, 2):
            if number!= j and number % j == 0:
                flag = 1
                break
    if flag > 0:
        print("Not Prime")
    else:
        print("Prime")
