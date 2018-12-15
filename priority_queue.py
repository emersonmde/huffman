#!/usr/bin/env python3


class PriorityQueueNode:
    def __init__(self, val, p, n):
        self.val = val
        self.next = n
        self.prev = p


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.len = 0

    def push(self, val):
        self.len += 1
        if self.head is None:
            self.head = PriorityQueueNode(val, None, None)
        else:
            for i in self:
                if val <= i.val:
                    if i.prev is None:
                        n = PriorityQueueNode(val, None, i)
                        i.prev = n
                        self.head = n
                    else:
                        i.prev.next = PriorityQueueNode(val, i.prev, i)
                        i.prev = i.prev.next
                    break
                elif i.next is None:
                    i.next = PriorityQueueNode(val, i, None)

    def pop(self):
        if self.head is None:
            self.len = 0
            return None
        else:
            i = self.head.val
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            self.len -= 1
            return i

    def to_array(self):
        a = []
        for i in self:
            a.append(i.val)
        return a

    def __iter__(self):
        self.i = self.head
        return self

    def __next__(self):
        if self.i is None:
            raise StopIteration
        else:
            i = self.i
            self.i = self.i.next
            return i

    def __repr__(self):
        return repr(self.to_array())



