counter = int(input())
container = [None] * counter
for i in range(counter):
    container[i] = input()
for i in container:
    if len(i)< 10:
        print(i)
    else:
        print("{}{}{}".format(i[0],len(i)-2,i[-1]))