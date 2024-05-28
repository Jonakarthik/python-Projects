class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class double:
    def __init__(self):
        self.head=None
        self.tail=None
    def node_beg(self,data):
        temp=self.head
        nb=Node(data)
        nb.next=self.head
        self.head=nb
        temp.prev=nb
    def node_end(self,data):
        ne=Node(data)
        temp=self.head
        while(temp.next):
             temp=temp.next
        temp.next=ne
        ne.prev=temp
        ne.next=None
    def node_pos(self,pos,data):
        temp=self.head
        np=Node(data)
        for p in range(1,pos-1):
            temp=temp.next
        
        np.next=temp.next
        temp.next=np
        np.prev=temp
        temp.next.prev=np

    def reverse(self):
        temp=self.tail
        if(self.tail is None):
            print("DLL is empty:")
        while(temp):
            print(temp.data,end="-->")
            temp=temp.prev
    def display(self):
        temp=self.head
        if(self.head is None):
            print("linked list is empty:")
        else:
            while(temp):
                print(temp.data,end="-->")
                temp=temp.next
   
n1=Node(10)
d1=double()
d1.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
n4=Node(40)
n4.prev=n3
n3.next=n4
d1.tail=n4
#d1.reverse()
d1.node_pos(3,25)
d1.display()


    
