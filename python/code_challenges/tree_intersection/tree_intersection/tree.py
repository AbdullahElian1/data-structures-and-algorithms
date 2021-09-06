class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,value):
        node=Node(value)
        if self.is_empty():
            self.front=node
            self.rear=node
        self.rear.next=node
        self.rear=node
    def dequeue(self):
        if self.is_empty():
            raise Exception("empty equeue")
        if self.front==self.rear:
            temp=self.front
            self.front=None
            self.rear=None
            return temp.value
        else:
            temp=self.front
            self.front=self.front.next
            temp.next=None
            return temp.value

    def peek(self):
       if self.is_empty():
           raise Exception("empty equeue")
       return self.front.value


    def is_empty(self):
     return not self.front

    def __len__(self):
        counter=0
        while self.front:
            counter +=1
            self.dequeue()
        return counter



class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self) :
        self.root=None
        self.arr=[]



    def pre_order(self,root):
        # print(root.value)
        try:
            self.arr.append(root.value)
            if root.left !=None:
                self.pre_order(root.left)

            if root.right !=None:
                self.pre_order(root.right)
            return self.arr
        except:
            raise Exception("pre order accept valid ")

    def post_order(self,root):
        try:
            if root.left:
                self.post_order(root.left)


            if root.right:
                self.post_order(root.right)

            self.arr.append(root.value)
            return self.arr
        except:
            raise Exception("something went wrong")
    def in_order(self,root):
        try:
            if root.left:
                self.in_order(root.left)

            self.arr.append(root.value)

            if root.right:
                self.in_order(root.right)

            return self.arr
        except:
            raise Exception("something went wrong")

    def test (self):
        self.arr=[]
    def tree_max(self):

        arr_of_number=self.in_order(self.root)
        # return(x)
        self.max=self.root.value

        for i in arr_of_number :
            if i>self.max:
                self.max=i
        return self.max

        # print(self.temp.value)
        # if self.temp.left:
        #     self.temp=self.temp.left
        #     self.tree_max()

        #     # return self.max
        # print(self.temp.value)
        # if self.max<self.temp.value:
        #     self.max=self.temp.value

        # if self.temp.right:
        #      self.temp=self.temp.right
        #      self.tree_max()

        # return self.max
    def BreadthFirst(self,root):

            if not root:
                raise Exception("Empty Tree")

            Queue_breadth = Queue()
            Queue_breadth.enqueue(root)
            try:
                while Queue_breadth.peek():
                        node_front = Queue_breadth.dequeue()
                        self.arr.append(node_front.value)

                        if node_front.left:
                            Queue_breadth.enqueue(node_front.left)

                        if node_front.right:
                            Queue_breadth.enqueue(node_front.right)
            except :
                    return self.arr
