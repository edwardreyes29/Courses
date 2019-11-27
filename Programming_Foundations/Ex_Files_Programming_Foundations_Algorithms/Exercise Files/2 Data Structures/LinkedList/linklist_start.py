# Linked list example


# the Node class
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val # return the val field

    def set_data(self, val):
        self.val = val # sets new value

    def get_next(self):
        return self.next # returns next node object

    def set_next(self, next):
        self.next = next


# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        # TODO: insert a new node
        # inserts new node at begining of list
        new_node = Node(data)
        new_node.set_next(self.head) # sets the curent head of this list as the new node's next
        self.head = new_node # sets head pointer to the new node
        self.count += 1 # increments count

    def find(self, val):
        # TODO: find the first item with a given value
        item = self.head # sets item to the current head which is a node
        while(item != None):
            if item.get_data() == val:
                return item
            else: 
                item = item.get_next()
        return None

    def deleteAt(self, idx):
        # TODO: delete an item at given index
        if idx > self.count-1:
            return
        if idx == 0:
            self.head = self.head.get_next() # set head to next to delete the current head
        else: # would need to search entire list
            tempIdx = 0
            node = self.head
            while tempIdx < idx - 1: # We would want the node right before the one were deleting b/c that's the node whose next pointer we have to fix!!!
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next()) # getting the node after the one selected to be deleted
            self.count -= 1 # decrement the node to reflect the fact that we got rid of a node


    # prints out the list
    def dump_list(self): 
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)
itemlist.dump_list()

# exercise the list
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(13)) # find item that exist
print("Finding item: ", itemlist.find(78)) # find item that doesn't exist in list

# delete an item
itemlist.deleteAt(3)
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(38))
itemlist.dump_list()
