from linkedlist import *
#from singlelinkedlist import *

node1 = ListNode(15)  
node2 = ListNode(8.2)  
item3 = "Berlin"  
node4 = ListNode(15)

track = SingleLinkedList()  
print("track length: %i" % track.list_length())

for current_item in [node1, node2, item3, node4]:  
    track.add_list_item(current_item)
    print("track length: %i" % track.list_length())
    track.output_list()
