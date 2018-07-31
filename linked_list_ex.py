"""
This module demonstates exmaple for single linked list and its operations
"""

class Node:

    def __init__(self,item,link=None):
        self.item = item
        self.link = link

    def getNext(self):
        return self.link

    def setnext(self,newnode):
        self.link = newnode

    def getData(self):
        return self.item

class SingleLinkedList(Node):

    def __init__(self,head=None):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        new_node.setnext(self.head)
        self.head = new_node

    def search(self,data):
        
        current = self.head
        flag = False
        while current:
            if current.getData() == data:
                print("Data found {}".format(current.getData()))
                break
            else:
                current = current.getNext()
        return False


    def size(self):

        current = self.head
        count = 0

        while current:
            count+=1
            current = current.getNext()

        return count


    def delete(self,data):
        current = self.head
        previous = None
        found = False
        while current and not found:

            if current.getData() == data:
                print("Data found")
                found = True
    
            else:
                previous = current
                current = current.getNext()
        if current is None:
            raise ValueError("Item provided is not present in linkedlist")

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setnext(current.getNext())

    def display_items(self):
        print("Values in linked list")
        current = self.head
        while current:
            print(current.getData())
            current=current.getNext()
        if current is None:
            print("no data to print in linked list")


if __name__ == "__main__":
    import sys
    linked_list = SingleLinkedList()
    items = sys.argv
    print(items)
    for value in range(int(items[1])):
            x= input("""Enter operation to perfrom 
                1. Insert data to linked list
                2, Delete data from linked list
                3. search date from linked list
                4. size of linked list
                5. Display values in linked list
                6. Quit
                """)
            if x==1:
                value = input("Enter data to insert in linked list")
                linked_list.insert(value)
            elif x==2:
                value = input("Enter data to delete from linked list")
                linked_list.delete(value)
            elif x==3:
                value = input("Enter data to search")
                linked_list.search(value)
            elif x==4:
                output = linked_list.size()
                print("Length of linked list %{}".format(output))
            elif x==5:
                linked_list.display_items()
            elif x==6:
                break
            else:
                raise ValueError("Please Enter valid input")


