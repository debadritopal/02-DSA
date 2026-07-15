class Node:
    def __init__(self,num):
        self.data=num
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,num):
        new_node=Node(num)
        new_node.next=self.head
        self.head=new_node
        print("Element Successfully Added")
    def insert_at_end(self,num):
        new_node=Node(num)
        current=self.head
        if current is None:
            self.head=new_node
            print("Element Successfully Added")
            return
        while current.next is not None:
            current=current.next
        current.next=new_node
        print("Element Successfully Added")
    def delete_from_beginning(self):
        if self.head is None:
            print("Linked List Underflow")
            return
        print(f"{self.head.data} successfully deleted")
        self.head=self.head.next
    def delete_from_end(self):
        if self.head is None:
            print("Linked List Underflow")
            return
        if self.head.next is None:
            deleted=self.head.data
            self.head=None
            print(f"{deleted} successfully deleted")
            return
        current=self.head
        while current.next.next is not None:
            current=current.next
        deleted=current.next.data
        current.next=None
        print(f"{deleted} successfully deleted")
    def search(self,num):
        current=self.head
        pos=1
        found=False
        while current is not None:
            if current.data==num:
                print(f"{num} found at position {pos}")
                found=True
                break
            else:
                pos+=1
                current=current.next
        if not found:
            print(f"{num} not found...")
    def display(self):
        current=self.head
        print("Head-->",end='')
        while current is not None:
            print(current.data,"-->",sep='',end='')
            current=current.next
        print("None")
l=LinkedList()
while True:
    try:
        line="="*40
        print(f"{line}\nWelcome to Linked List!\n{line}\n")
        print("1. Add Elements to the Beginning\n2. Add Elements to the End\n3. Delete element from beginning\n4. Delete element from end\n5. Search Element\n6. View Linked List\n7. Exit")
        ch=int(input("Enter choice: "))
        if ch==1:
            num=int(input("Enter number: "))
            l.insert_at_beginning(num)
        elif ch==2:
             num=int(input("Enter number: "))
             l.insert_at_end(num)
        elif ch==3:
            l.delete_from_beginning()
        elif ch==4:
            l.delete_from_end()
        elif ch==5:
            num=int(input("Enter element to be searched: "))
            l.search(num)
        elif ch==6:
            l.display()
        elif ch==7:
            print("Exiting....")
            break
        else:
            print("Enter a valid choice")
    except ValueError:
        print("Enter a valid integer")