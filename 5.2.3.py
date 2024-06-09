n=int(input())
b=[]
for i in range(0,n):
    print(f"Enter the value of a[{i}]")
    a=int(input())
    b.append(a)
summ=0

for i in range(0,n):
    summ=summ+b[i]
print("The sum of array elements=",summ)

