text_1 = input().lower()
text_2 = input().lower()

if(text_1 == text_2):
    print(0)
elif (text_1 < text_2):
    print(-1)
else:
    print(1)