str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

a = ''
for char in str2:
    if char not in str1:
        a = char

print("Extra character in the second string:", a)


