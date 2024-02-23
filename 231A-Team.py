iteration = int(input())
counter = 0
for i in range(iteration):
    a, b, c = map(int, input().split())
    if ( a == 1 and b==1 ) or (b==1 and c==1) or (c==1 and a==1):
        counter += 1
print(counter)
