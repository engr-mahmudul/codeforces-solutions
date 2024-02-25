output = 0
iteration = int(input())
for i in range(iteration):
    operation = input()
    if (operation == "++X") or (operation == "X++"):
        output += 1
    elif(operation == "--X") or (operation == "X--"):
        output -= 1
print(output)