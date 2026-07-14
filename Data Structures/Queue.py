class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,element):
        self.queue.append(element)
        print("Successfully equeued")
    def dequeue(self):
        if self.check_empty():
            print("Queue Underflow")
        else:
            popped=self.queue.pop(0)
            print(f"{popped} successfully dequeued")
    def front(self):
        if self.check_empty():
            return "Queue Underflow"
        else:
            return self.queue[0]
    def rear(self):
        if self.check_empty():
            return "Queue Underflow"
        else:
            return self.queue[-1]
    def display(self):
        if self.check_empty():
            print("Queue Already Empty")
        else:
            print(self.queue)
    def check_empty(self):
        return len(self.queue)==0
    def size(self):
        return len(self.queue)
    def clear_queue(self):
        if self.check_empty():
            print("Queue already empty")
        else:
            self.queue.clear()
            print("Queue Cleared Successfully....")
q=Queue()
while True:
    try:
        line='='*40
        print(f"{line}\nQueue Implementation\n{line}\n")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Rear")
        print("5. Display")
        print("6. Check Empty")
        print("7. Size")
        print("8. Clear queue")
        print("9. Exit")
        ch=int(input("Enter choice: "))
        if ch==1:
            element=input("Enter element: ")
            q.enqueue(element)
        elif ch==2:
            q.dequeue()
        elif ch==3:
            print(q.front())
        elif ch==4:
            print(q.rear())
        elif ch==5:
            q.display()
        elif ch==6:
            if q.check_empty():
                print("Queue is empty")
            else:
                print("Queue is not empty")
        elif ch==7:
            print(f"Queue has {q.size()} elements")
        elif ch==8:
            q.clear_queue()
        elif ch==9:
            print("Exiting....")
            break
        else:
            print("Please enter a valid choice")
    except ValueError:
        print("Please enter a valid integer")