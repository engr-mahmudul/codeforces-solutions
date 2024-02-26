while True:
    new_string = ''
    d, n = map(int, input().split())
    if (d == 0 and n == 0):
        break
    number_string = str(n)
    for i in number_string:
        if i != str(d):
            new_string = new_string + i

    if (new_string == ''):
        new_string = 0
    else:
        new_string = int(new_string)
    print(new_string)




