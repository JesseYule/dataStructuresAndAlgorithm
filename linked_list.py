class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:

    def __init__(self):
        self.head = None

    def initlist(self, data_list):

        self.head = Node(data_list[0])
        temp = self.head  # 创建头结点

        for i in data_list[1:]:
            cur_node = Node(i)
            temp.next = cur_node
            temp = cur_node

    def is_empty(self):
        if self.head.next == None:
            print('Linked list is empty')
            return True
        else:
            return False

    def get_length(self):
        temp = self.head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        return length

    def insert(self, key, value):  # 链表插入数据，这是重点

        if key < 0 or key >= self.get_length()-1:
            print('insert error')
        temp = self.head
        i = 0

        while i <= key:  # 遍历直到找到key
            pre = temp
            temp = temp.next
            i += 1

        node = Node(value)
        pre.next = node  # 把key对应指向的node改为插入的node
        node.next = temp  # 把插入的node的next指向原来的key对应的下一个node

    def print_list(self):
        temp = self.head
        print_list = []
        while temp is not None:
            print_list.append(temp.data)
            temp = temp.next
        print(print_list)

    def remove(self, key):

        if key < 0 or key >= self.get_length()-1:
            print('remove error')

        i = 0
        temp = self.head

        while temp is not None:
            pre = temp  # 从head开始，此时对应的key为-1
            temp = temp.next
            i += 1
            if i == key:  # 当i==key，此时node（pre）指向key-1，temp指向key
                pre.next = temp.next  # key-1指向key+1的节点，实现remove
                temp = None
                return True

        pre.next = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

