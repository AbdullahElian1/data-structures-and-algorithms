
from hash_left_join.hash_table import HashTable
import re
def hashmap_left_join(hash1,hash2):

    buckets=hash1.get_buckets()
    arr=[]
    for i in buckets:
        if i:
            current=i.head
            while current:
                x=hash2.find(current.value[0])
                if not x:
                    x='Null'
                current.value.append(x)
                arr.append(current.value)
                current=current.next
    return arr



def number_of_word(book:str)-> str:
    string_no_punctuation = re.sub("[^\w\s]", "", book)
    arr=string_no_punctuation.split()
    temp_word=''
    temp_counter=1
    hash=HashTable(40)
    for i in arr:
        i=i.lower()
        # print(i)
        if hash.contains(i):
            x=hash.find(i)
            x =x  + 1
            hash.add(i,x)

            if hash.find(i)>temp_counter:
                # print(i)
                temp_word=i
                temp_counter+=1
        else:
                print(i)
                hash.add(i,1)
                print(hash.contains(i))

            # print(hash.find(i))
    # print(hash._buckets)
    return temp_word


print(number_of_word("yes? no yes yes  no% no!  "))
# hash1 = HashTable()
# hash1.add('fond', 'enamored')
# hash1.add('wrath', 'anger')
# hash1.add('diligent', 'employed')
# hash1.add('outfit', 'garb')
# hash1.add('guide', 'usher')

# hash2 = HashTable()
# hash2.add('fond', 'averse')
# hash2.add('wrath', 'delight')
# hash2.add('diligent', 'idle')
# hash2.add('guide', 'follow')
# hash2.add('flow', 'jam')


# hashmap_left_join(hash1, hash2)



