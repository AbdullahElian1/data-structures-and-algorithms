# import linked_list


from typing import Counter


class Node:

  def __init__(self, value=""):
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value)

class LinkedList():
  def __init__(self):
    self.head = None

  def insert(self, value):
    node = Node(value)

    if self.head:
      node.next = self.head

    self.head = node

  def includes(self,vlaue):
     current=self.head

     while current :
        #  print(current.value)
         if vlaue ==current.value:
            return True
         current=current.next

     return False

  def append(self,value):
      node=Node(value)
      current=self.head
    #   print(current.next)
      if current==None:
          self.insert(value)
          return
      while current.next!=None:
          current=current.next
      current.next=node

  def insert_after(self,old_value,value):
    node=Node(value)
    current=self.head
    temp=self.head

    while current.next!=None:

      if current.value==old_value:
        temp=temp.next
        current.next=node
        current=current.next
        current.next=temp
        return
      current=current.next
      temp=temp.next

    self.append(value)



  def insert_before(self,old_value,value):
    node=Node(value)
    current=self.head
    temp=self.head

    if current.value==old_value:
      self.insert(value)
      return

    while(current.next.value!= old_value):
      current=current.next

    temp = current.next
    current.next=node
    node.next = temp


  def kthFromEnd(self,num):
      if num <0:
          return "please input positive number"

      num1=len(self)-1
      if num1<num:
          return ("out of range")

      num_of_loop=(len(self)-num)-1
      current=self.head

      while num_of_loop >0 :
        #   print(num_of_loop)
          current=current.next
          num_of_loop -=1

      return current.value



  def __str__(self):
    string = ""
    current = self.head

    while current:
      string += f"{current.value} -> "
      current = current.next
    # string += "None"
    return string

  def __repr__(self):
    return "LinkedList()"

  def __len__(self):
    counter = 0
    current = self.head

    while current:
      counter += 1
      current = current.next

    return counter




def zip_linked_list(linked1, linked2):



        cuurent=linked1.head
        cuurent1=linked2.head
        if cuurent==None:
          if cuurent1==None:
            raise Exception("empty list")
        if cuurent==None:
          if cuurent1!=None:
            return linked2
        if cuurent!=None:
          if cuurent1==None:
            return linked1
        # if len(linked1)>len(linked2):
        #     print(linked1)
        #     cuurent=linked1.head
        # else:
        #     print(linked2)
        #     cuurent=linked2.head
        #     cuurent1=linked1.head
        # print(cuurent)

        while cuurent:

          if cuurent1:
                temp=cuurent.next
                cuurent.next=cuurent1
                cuurent=temp



                if temp:
                  temp1=cuurent1.next
                  cuurent1.next=temp
                  cuurent1=temp1

          if cuurent1==None:
              break

        #   cuurent=cuurent.next
        #   if cuurent1:
        #       cuurent.next=cuurent1
        #       break











        return linked1


new_linked=LinkedList()
new_linked1=LinkedList()
new_linked1.append("t")
new_linked1.append("a")
new_linked1.append("d")
new_linked1.append("o")
new_linked1.append("c")
new_linked1.append("a")
new_linked1.append("t")

# new_linked1.append(5)
# new_linked1.append(6


# print(zip_linked_list(new_linked,new_linked1))



def palindrome(linked):
    current=linked.head
    value=[]

    while current:
        value.append(current.value)
        print(current)
        current=current.next

    current=linked.head
    value=value[::-1]
    print(value)
    for i in value:
        if i==current.value:
            current=current.next
            if current==None:
                return True
        else:
            return False


palindrome(new_linked1)










    #   while current.next!=None:
    #       current.next=urrent
    #       urrent.next=current.next
    #       urrent=urrent.next
    #       current=current.next


# #   print(test.kthFromEnd(6))
# #   test.insert_before(7,77890)
#   # test.insert_before(7777,7)
# #   print(test)









