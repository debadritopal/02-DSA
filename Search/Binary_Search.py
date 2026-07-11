print("Enter integers in ascending order:")
numbers=[]
for i in range(10):
    numbers.append(int(input()))
target=int(input("Enter target: "))
found=False
low=0
high=len(numbers)-1
while low<=high:
    mid=(low+high)//2
    if numbers[mid]==target:
        found=True
        print(f"{target} found at index {mid}")
        break
    elif numbers[mid]<target:
        low=mid+1
    else:
        high=mid-1
if not found:
    print("Target not found....")