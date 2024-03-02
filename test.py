def pow2(max_val):
    powers_string =''
    i = 0
    while True:
        if 2 ** i <= max_val:
            if i == 0:
                powers_string += str(2 ** i)

            else:
                powers_string += ' ' + str(2 ** i)

            i += 1

        else:
            break

    return powers_string


print(pow2(64))