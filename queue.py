# 通过链表实现队列
# 队列先进先出


class Node(object):
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next


class Queue(object):
    def __init__(self):
        self.head = None  # 头部
        self.rear = None  # 尾部

    def is_empty(self):
        return self.head is None

    def enqueue(self, elem):
        p = Node(elem)
        if self.is_empty():
            self.head = p
            self.rear = p
        else:
            self.rear.next = p
            self.rear = p

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            dequeue_element = self.head.elem
            self.head = self.head.next
            return dequeue_element

    def peek(self):
        if self.is_empty():
            print('queue is empty')
        else:
            return self.head.elem

    def print_queue(self):
        if self.is_empty():
            print('queue is empty')
        else:
            print_list = []
            while self.head is not None:
                print_list.append(self.head.elem)
                self.head = self.head.next
            print(print_list)

