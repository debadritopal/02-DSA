def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)
while True:
    try:
        num=int(input("Enter a positive integer (Enter -1 to exit): "))
        if num>=0:
            print(f"Factorial of {num} is {factorial(num)}")
        elif(num==-1):
            print("Exiting....")
            break
        else:
            print("Please enter a positive integer")
    except ValueError:
        print("Please enter a valid positive integer")