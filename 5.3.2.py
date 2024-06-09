a=int(input())
lst=[]
for i in range (0,a):
    c=int(input())
    lst.append(c)
print("The elements of array:")
for i in range(0,a):
    print(lst[i],end=" ")
b = len(lst)
c = 2**b
print("\nTotal number of subsets:", c)

