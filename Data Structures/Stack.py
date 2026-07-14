class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
        print("Element Succesfully Pushed!")
    def pop(self):
        if self.check_empty():
            print("List is Already Empty!")
        else:
            popped=self.stack.pop()
            print(f"{popped} Succesfully Popped!")
    def peek(self):
        if self.check_empty():
            return "List is Empty!"
        else:
            return self.stack[-1]
    def display(self):
        print(self.stack)
    def check_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    def clear_stack(self):
        self.stack.clear()
        print("Stack Cleared...")
s=Stack()
while True:
    try:
        line='='*40
        print(f"{line}\nStack Implementation\n{line}\n")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Check Empty")
        print("6. Size")
        print("7. Clear Stack")
        print("8. Exit")
        ch=int(input("Enter choice: "))
        if ch==1:
            element=input("Enter element: ")
            Stack.push(s,element)
        elif ch==2:
            Stack.pop(s)
        elif ch==3:
            print(Stack.peek(s))
        elif ch==4:
            Stack.display(s)
        elif ch==5:
            if Stack.check_empty(s):
                print("Stack is empty")
            else:
                print("Stack is not empty")
        elif ch==6:
            print(f"Stack has {Stack.size(s)} elements")
        elif ch==7:
            Stack.clear_stack(s)
        elif ch==8:
            print("Exiting....")
            break
        else:
            print("Please enter a valid choice")
    except ValueError:
        print("Please enter a valid integer")