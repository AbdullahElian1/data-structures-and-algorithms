from typing import Counter


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


class BinarySearch(BinaryTree):

    def add(self,value):


        if not self.root:
            self.root=Node(value)
            # print(self.root.value)
            return

        current=self.root
        print(current.value)
        while current :
                    if value>current.value:
                        if current.right:
                             current=current.right
                        else:
                            current.right=Node(value)

                            return

                    else:
                        if current.left:
                             current=current.left
                        else:
                            current.left=Node(value)
                            return
    def Contains(self,value):

             if not self.root:
                raise Exception("empty tree")

             elif value==self.root.value:
                 return True


             current = self.root

             while current:
                if value == current.value:

                    return True

                if value > current.value:
                    if current.right:
                        current = current.right
                    else:

                        return False

                else:
                    if current.left:
                        current = current.left
                    else:

                        return False







x=BinarySearch()
# x.push(10)
# root=Node(1)
# root.left=Node(2)
# root.left.left=Node(3)
# root.left.right=Node(4)
# root.right=Node(5)
# root.right.left=Node(6)
# x.root=root
x.add(7)
x.add(8)
x.add(6)
x.add(5)
x.add(150)
x.add(19)
x.add(111)
x.add(115)
x.add(10000)
print(x.Contains(10000))


result=x.in_order(x.root)
print(result)
# result=x.post_order(1)
# x.test()
# result=x.pre_order(root)
# for i in result:
# print(result)
