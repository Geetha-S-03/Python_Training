lst=[]
c=0
a=int(input())
d=int(input())
print("Entered the size: ",a)
for i in range(0,a):
    b=int(input())
    lst.append(b)
print("Enter elements ")
for i in range(1,a+1):
    if lst[i]==d:
        c=1
        break
if c==1:
    print(f"{d} is found at position {i}")
else:
    print(f"{d} is not found")
        
        







