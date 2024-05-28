class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def node_beg(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def node_pos(self,pos,data):
        if pos==1:
            self.node_beg(data)
        else:
         np=Node(data)
         temp=self.head
         for p in range(1,pos-1):
            temp=temp.next
         np.next=temp.next
         temp.next=np
    def node_end(self,data):
        ne=Node(data)
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=ne
        ne.next=None
    def del_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def del_end(self):
        prev=self.head
        temp=self.head.next
        while(temp.next):
            temp=temp.next
            prev=prev.next
        prev.next=None
    def del_pos(self,pos):
        if pos==1:
            self.del_beg()
        else:
         prev=self.head
         temp=self.head.next
         for p in range(1,pos-1):
            temp=temp.next
            prev=prev.next
         prev.next=temp.next
    def display(self):
        temp=self.head
        if(self.head is None):
            print("linked list is empty:")
        else:
            while(temp):
                print(temp.data,end="-->")
                temp=temp.next
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    def rev_list(self):
        l=[]#[10,20,30,40]
        temp=self.head
        while(temp):
            l.append(temp.data)
            temp=temp.next
        for p in range(len(l)-1,-1,-1):
            print(l[p],end="-->")
n1=Node(10)
s1=single()
s1.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
s1.node_pos(1,5)
#s1.node_beg(5)
#s1.node_end(50)
#s1.reverse()
#s1.rev_list()
#s1.display()
#s1.del_pos(1)
s1.display()
    
