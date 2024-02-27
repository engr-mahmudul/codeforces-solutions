salary = float(input())
if 0 <= salary <= 2000:
    print("Isento")
elif salary > 2000 and salary <= 3000:
    tax = (salary - 2000) * (0.08)
    print("R$ {:.2f}".format(tax))

elif salary > 3000 and salary <= 4500:
    tax = (salary-3000)*(0.18) + 80
    print("R$ {:.2f}".format(tax))
else:
    tax = (salary-4500)*(0.28) + 270 + 80
    print("R$ {:.2f}".format(tax))
