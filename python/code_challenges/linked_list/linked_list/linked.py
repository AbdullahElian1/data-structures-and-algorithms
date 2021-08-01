# import linked_list


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













  def __str__(self):
    string = ""
    current = self.head

    while current:
      string += f"{str(current.value)} -> "
      current = current.next
    string += "None"
    return string

  def __repr__(self):
    return "LinkedList()"

if __name__ == "__main__":
  test = LinkedList()
#   test.insert(16)
#   test.insert(29)
#   test.insert(4)
#   test.insert(7)
  test.append(177)
  test.append(1)

  test.append(17)

  # print("c")
#   test.insert_before(7,77890)
  # test.insert_before(7777,7)
  print(test)







