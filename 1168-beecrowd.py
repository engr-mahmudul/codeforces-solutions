led_dictionary = {
    "1":2,
    "2":5,
    "3":5,
    "4":4,
    "5":5,
    "6":6,
    "7":3,
    "8":7,
    "9":6,
    "0":6
}
test_case = int(input())

for i in range(test_case):
    text = input()
    sum = 0
    for i in text:
        sum += led_dictionary[i]

    print(sum,"leds")
