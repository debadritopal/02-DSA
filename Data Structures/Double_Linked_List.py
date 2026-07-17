class Node:
    def __init__(self,num):
        self.data=num
        self.next=None
        self.prev=None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def check_empty(self):
        return self.head is None
    def insert_at_beginning(self,num):
        new_node=Node(num)
        if self.check_empty():
            self.head=new_node
            print("Data succesfully added")
            return
        self.head.prev=new_node
        new_node.next=self.head
        self.head=new_node
        print("Data succesfully added")
    def insert_at_end(self,num):
        new_node=Node(num)
        if self.check_empty():
            self.head=new_node
            print("Data succesfully added")
            return
        current=self.head
        while current.next is not None:
            current=current.next
        new_node.prev=current
        current.next=new_node
        print("Data succesfully added")
    def insert_at_position(self,num,pos):
        new_node=Node(num)
        count=1
        current=self.head
        if self.check_empty():
            if pos==1:
                self.insert_at_beginning(num)
            else:
                print("Invalid position")
            return
        if pos==1:
            self.insert_at_beginning(num)
            return
        while current.next is not None and count<pos-1:
            current=current.next
            count+=1
        if current.next is None:
            if count==pos-1:
                self.insert_at_end(num)
            else:
                print("Invalid position")
            return
        new_node.next=current.next
        new_node.prev=current
        current.next.prev=new_node
        current.next=new_node
        print(f"{num} successfully insereted at position {pos}")
    def delete_from_beginning(self):
        if self.check_empty():
            print("Linked List Underflow")
            return
        deleted=self.head.data
        self.head=self.head.next
        if not self.check_empty():
            self.head.prev=None
        print(f"{deleted} successfully deleted")
    def delete_from_end(self):
        if self.check_empty():
            print("Linked List Underflow")
            return
        current=self.head
        deleted=0
        if current.next is None:
            deleted=current.data
            self.head=None
            print(f"{deleted} successfully deleted")
            return
        while current.next.next is not None:
            current=current.next
        deleted=current.next.data
        current.next=None
        print(f"{deleted} successfully deleted")
    def delete_by_value(self,num):
        if self.check_empty():
            print("LInked List Underflow")
            return
        if self.head.data==num:
            self.delete_from_beginning()
            return
        current=self.head
        while current.next is not None:
            if current.data==num:
                current.next.prev=current.prev
                current.prev.next=current.next
                current.prev=None
                current.next=None
                print(f"{num} has been successfully deleted")
                return
            current=current.next
        if current.data==num:
            self.delete_from_end()
            return
        if current.next is None:
            print("Value doesn't exist")
    def display_forward(self):
        if self.check_empty():
            print("Linked List Underflow")
            return
        current=self.head
        print("Head-->",end='')
        while current is not None:
            print(current.data,"-->",sep='',end='')
            current=current.next
        print("None")
    def display_reverse(self):
        if self.check_empty():
            print("Linked List Underflow")
            return
        current=self.head
        while current.next is not None:
            current=current.next
        print("Tail-->",end='')
        while current is not None:
            print(current.data,"-->",sep='',end='')
            current=current.prev
        print("None")
    def search(self,num):
        if self.check_empty():
            print("Linked List Underflow")
            return
        current=self.head
        pos=1
        while current is not None:
            if current.data==num:
                print(f"{num} found at position {pos}")
                return
            pos+=1
            current=current.next
        if current is None:
            print("Number not found")
    def reverse(self):
        if self.check_empty():
            print("Linked List Underflow")
            return
        current=self.head
        new_head=0
        while current is not None:
            new_head=current
            pointer=current.prev
            current.prev=current.next
            current.next=pointer
            current=current.prev
        self.head=new_head
        print("Linked List Succesfully reversed")
dl=DoubleLinkedList()
while True:
    try:
        line="="*40
        print(f"{line}\nWelcome to Double Linked List!\n{line}\n")
        print("1. Add Elements to the Beginning\n2. Add Elements to the End\n3. Insert at a position\n4. Delete Element from beginning\n5. Delete Element from end\n6. Delete by Value\n7. Display Forward\n8. Display Backward\n9. Search Element\n10. Reverse Linked List\n11. Exit")
        ch=int(input("Enter choice: "))
        if ch==1:
            num=int(input("Enter number: "))
            dl.insert_at_beginning(num)
        elif ch==2:
             num=int(input("Enter number: "))
             dl.insert_at_end(num)
        elif ch==3:
            num=int(input("Enter element to be inserted: "))
            pos=int(input("Enter position: "))
            dl.insert_at_position(num,pos)
        elif ch==4:
            dl.delete_from_beginning()
        elif ch==5:
            dl.delete_from_end()
        elif ch==6:
            num=int(input("Enter value to be deleted: "))
            dl.delete_by_value(num)
        elif ch==7:
            dl.display_forward()
        elif ch==8:
            dl.display_reverse()
        elif ch==9:
            num=int(input("Enter element to be searched: "))
            dl.search(num)
        elif ch==10:
            dl.reverse()
        elif ch==11:
            print("Exiting....")
            break
        else:
            print("Enter a valid choice")
    except ValueError:
        print("Enter a valid integer")