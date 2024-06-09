a=input()
b=list(a)
target=input()
replace=input()
for i in range(len(a)):
    if(b[i]==target):
        b[i]=replace
        
a=''.join(b)
print(a)

