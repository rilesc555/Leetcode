# 206 reverse linked list
# Ugh, this is weird in python

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: ListNode) -> ListNode:
    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    return prev

