numbers=[]
print("Enter Numbers 10: ")
for i in range(10):
    numbers.append(int(input()))
for pass_no in range(1,len(numbers)):
    j=pass_no-1
    key=numbers[pass_no]
    while j>=0 and numbers[j]>key:
        numbers[j+1]=numbers[j]
        j-=1
    numbers[j+1]=key
    print(f"Pass no {pass_no}: {numbers}")
print(f"Sorted Array: {numbers}")