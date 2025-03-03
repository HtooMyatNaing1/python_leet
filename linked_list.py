class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.length = 1
        self.head = new_node
        self.tail = new_node

    def append_list(self, value):
        appended_node = Node(value)
        if self.head is None:
            self.head = appended_node
            self.tail = appended_node
        else:
            self.tail.next = appended_node
            self.tail = appended_node
        self.length += 1
        return True

    def prepend_item(self, value):
        prepended_node = Node(value)
        if self.head is None:
            self.head = prepended_node
            self.tail = prepended_node
            prepended_node.next = None
        else:
            prepended_node.next = self.head
            self.head = prepended_node
        self.length += 1
        return True

    def pop_first_item(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def pop_item(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp # Use (.value) to better visualize the process

    def get_by_index(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get_by_index(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend_item(value)
        if index == self.length:
            return self.append_list(value)
        new_node = Node(value)
        temp = self.get_by_index(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first_item()
        if index == self.length-1:
            return self.pop_item()
        pre = self.get_by_index(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def print_list(self):
        """
        while self.head is not None:
            print(self.head.value)
            self.head = self.head.next
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

def find_kth_from_end(ll, k):
    slow = fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow