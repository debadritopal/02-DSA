numbers=[]
print("Enter 10 numbers:")
for i in range(10):
    numbers.append(int(input()))
for pass_no in range(len(numbers)-1):
    for i in range(len(numbers)-1-pass_no):
        if numbers[i+1]<numbers[i]:
            numbers[i+1],numbers[i]=numbers[i],numbers[i+1]
    print(f"Pass Number {pass_no+1}: {numbers}")
print(f"Sorted array: {numbers}")