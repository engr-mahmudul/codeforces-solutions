test_case = int(input())
total_c = 0
total_r = 0
total_s = 0
total = 0

for i in range(test_case):
    amount, animal_type = map(str, input().split())
    amount = int(amount)
    total += amount

    if animal_type == "C":
        total_c += amount
    elif animal_type == "R":
        total_r += amount
    elif animal_type == "S":
        total_s += amount

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(total_c))
print("Total de ratos: {}".format(total_r))
print("Total de sapos: {}".format(total_s))
print("Percentual de coelhos: {:.2f} %".format((total_c / total) * 100))
print("Percentual de ratos: {:.2f} %".format((total_r / total) * 100))
print("Percentual de sapos: {:.2f} %".format((total_s / total) * 100))