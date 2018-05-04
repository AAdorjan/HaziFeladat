class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LancoltList:
    head = None
    def appendFront(self,data):
        newe=Node(data)
        newe.next=self.head
        self.head=newe

    def appendBack(self,data):
        newe = Node(data)
        if self.head is None:
            self.head=newe
        else:
            current_item=self.head
            while current_item.next is not None:
                current_item=current_item.next
            current_item.next=newe

    def remove(self,element):
        tmp=self.head
        previous=None
        while tmp is not None:
            if tmp.data==element:
                if previous is None:
                    self.head=self.head.next
                else:
                    previous.next=tmp.next
            previous=tmp
            tmp=tmp.next



    def show(self):
        tmp=self.head
        print("A lista elemei: ")
        while tmp is not None:
            print(tmp.data)
            tmp=tmp.next
        print('None')

s=LancoltList()
s.appendFront(23)
s.appendFront(42)
s.appendBack(11)
s.appendBack(77)

s.show()

s.remove(77)

s.show()

import math
import matplotlib.pyplot as plt
import numpy as np

def gyok(x):
    return math.sqrt(x)
gyok2=lambda x: math.sqrt(x)


sum=lambda x,y:x+y

fakt=lambda n: n*(fakt(n-1)) if n>1 else 1


print(gyok(25))
print(gyok2(25))
print(sum(10,20))
print(100 if 4%2==0 else 101)
print(fakt(5))
