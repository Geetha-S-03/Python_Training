a = input()
result = ""
for i in range(len(a)):
    char = a[i]
    f=0
    for i in range(i):
        if a[i] == char:
            f=1 
            break
    if not f:
        result += char
print("String with repeated characters removed:", result)

