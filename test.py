def print_array(given_array, array_name):
    for i in range(len(given_array)):
        print("{}[{}] = {}".format(array_name,i,given_array[i]))
    given_array.clear()

store = [None]*15
par = []
impar = []
for i in range(15):
    store[i] = int(input())


for i in range(15):
    if (store[i] % 2 == 0):
        if len(par) < 5:
            par.append(store[i])
        else:
            print_array(par,"par")
            par.append(store[i])

    else:
        if len(impar) < 5:
            impar.append(store[i])
        else:
            print_array(impar,"impar")
            impar.append(store[i])

if len(impar) != 0:
    print_array(impar, "impar")
if len(par) != 0:
    print_array(par, "par")