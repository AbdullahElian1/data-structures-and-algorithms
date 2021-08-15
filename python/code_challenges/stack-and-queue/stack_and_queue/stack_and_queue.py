from typing import Counter


class Node():
    def __init__(self,value=""):
        self.next=None
        self.value=value

class Stack():
    def __init__(self):
        self.top=None

    def push(self,value):
        node=Node(value)
        node.next=self.top
        self.top=node

    def pop(self):

        if self.is_empty():
            raise Exception("empty stack")
        temp=self.top
        self.top=self.top.next
        temp.next=None
        return temp.value

    def peek(self):
        if self.is_empty():
            raise Exception("empty stack")
        return self.top.value

    def is_empty(self):
     return not self.top

    def __len__(self):
        counter=0
        while self.top:
            counter +=1
            self.pop()
        return counter








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

class pseudo_queue:
    def __init__(self):

        self.first_stack=Stack()
        self.second_stack=Stack()

    def enqueue(self,value):
        self.first_stack.push(value)


    def dequeue(self):
         if self.second_stack.is_empty():
            while self.first_stack.top != None:
                self.second_stack.push(self.first_stack.pop())
         return self.second_stack.pop()

    def __str__(self):
        string = ""
        current = self.first_stack.top
        current1=self.second_stack.top
        if current:
          return str( current.value)
        elif current1:
            return str(current1.value)
        else:
            return ("empty stack")


        # while current:

        #     string += f"{self.first_stack.top.value} -> "
        #     current = self.first_stack.pop()
        #     # string += "None"

class Animal:
    def __init__(self,name,type):
        self.name=name
        self.type=type


class Dog(Animal):
    pass

class Cat(Animal):
    pass

class AnimalShelter:
    def __init__(self) :
        self.dog=Queue()
        self.cat=Queue()

    def enqueue(self,animal_type):

        if animal_type.type=="dog":
            # print(animal_type.name)
            self.dog.enqueue(animal_type)
        elif animal_type.type=="cat":
            # print(animal_type.name)
            self.cat.enqueue(animal_type)
        else:
            print("animal should be cat or dog")

    def dequeue(self,pref):
        if pref=="dog":
            name=self.dog.dequeue().name
            return name
        elif pref=="cat":
            name=self.cat.dequeue().name
            return name
        else:
            print("pref should be cat or dog")
    def __str__(self):
        string=""
        cuurrent=self.dog.front
        cuurrent1=self.cat.front

        while cuurrent:
         string+="Dog Queue"
         string+= f"{cuurrent.value.name} -> "
         cuurrent=cuurrent.next
        string+="None -> Cat Queue ->"

        while cuurrent1:
         string+= f"{cuurrent1.value.name} -> "
         cuurrent1=cuurrent1.next
        string+="None"



        return string

# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
def validate_brackets(string):
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    stack = []
    for i in string:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                print(open_list[pos] )
                print(stack[len(stack)-1])
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

# print(validate_brackets("()"))
# test=Dog("haski","dog")
# test2=Dog("s","dog")
# # test3=Dog("s","dog")
# test4=Cat("sherazi","cat")
# test5=Cat("test","cat")

# test1=AnimalShelter()
# test1.enqueue(test)
# test1.enqueue(test2)
# # # test1.enqueue(test)
# test1.enqueue(test4)
# test1.enqueue(test5)
# print(test1)
#
# print(test1.dequeue("dog"))
# print(test1.dequeue("dog"))

# print(test1.dequeue("cat"))
# test=Do

# print(test1.dequeue("dog"))


# test=pseudo_queue()
# test.enqueue(5)
# test.enqueue(10)
# test.enqueue(15)
# test.enqueue(20)
# # test.enqueue(10)

# test.dequeue()
# test.dequeue()
# test.dequeue()
# test.dequeue()

# print(test)
# # test.push(2)
# test.push(1)
# test.e()
# test.dequeue()

# print(test.__len__())
# test=Stack()
# test.push(1)
# test.push(2)


# print(test.peek())

def x(list,k):

    y=Queue()
    for i in list:
        y.enqueue(i)
    # print(y.peek())

    Current=y
    print(Current.front)
    while Current.front:
        for i in range(k):
           c=Current.peek()
           print(c)
        #    if k-1==i:
        #        Current.dequeue()
        #        continue
        #    print(c)
        #    Current.dequeue()
        #    Current.enqueue(c)
        Current=Current.next




r=["a","b","c","d"]
x(r,3)
