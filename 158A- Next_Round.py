input_number , position = map(int,input().split())
scores = list(map(int, input().split()))
threshold_value = scores[position - 1]
advancer = 0
for i in scores:
    if (i > 0 and i>= threshold_value):
        advancer += 1
print(advancer)