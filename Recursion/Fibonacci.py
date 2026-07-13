memo={}
def Fibonacci(num):
    if num<=1:
        return num
    if num in memo:
        return memo[num]
    else:
        fibo=Fibonacci(num-1)+Fibonacci(num-2)
        memo[num]=fibo
    return fibo
def printFib(num):
    l=[]
    for fib in range(num+1):
        l.append(Fibonacci(fib))
    return l
while True:
    try:
        num=int(input("Enter a positive integer (Enter -1 to exit): "))
        if num>=0:
            fib_seq=printFib(num)
            print(f"Fibonacci series till {num}: ",*fib_seq)
        elif(num==-1):
            print("Exiting....")
            break
        else:
            print("Please enter a positive integer")
    except ValueError:
        print("Please enter a valid positive integer")