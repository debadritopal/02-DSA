numbers=[]
print("Enter Numbers 10: ")
for i in range(10):
    numbers.append(int(input()))
for pass_no in range(len(numbers)-1):
    min=pass_no
    for j in range(i+1,len(numbers)-1):
        if numbers[j]<numbers[min]:
            min=j
    numbers[pass_no],numbers[min]=numbers[min],numbers[pass_no]
    print(f"{pass_no}: {numbers}")
print(f"Sorted Array: {numbers}")