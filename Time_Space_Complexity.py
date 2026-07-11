integer=[]
for i in range(10):
    integer.append(int(input("Enter integer ")))
max,min=integer[0],integer[0]
sum=0
for i in range(1,len(integer)):
    if(i>max):
        max=i
    if(i<min):
        min=i
    sum+=i
avg=sum/10
print(f"Max {max}")
print(f"Min {min}")
print(f"Sum {sum}")
print(f"Average {avg}")