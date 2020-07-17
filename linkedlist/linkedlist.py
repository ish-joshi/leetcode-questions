
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# TODO: implement the list interface

class LinkedList:

    def __init__(self):
        root = Node()
        count = 0
    
    def append_item(self, item):
        if len(self) == 0:
            self.root.item = item
            self.count += 1
        else:
            ## Traverse till end
            ## Add the item
            pass

    def __len__(self):
        self.count


