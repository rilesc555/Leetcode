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

# 21 merge two sorted lists. Starting to see how this works
def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    return dummy.next


#143. reorder list. Find middle using slow and fast pointers, reverse second half, then merge
def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

    # find middle.
    s, f = head, head.next
    while f and f.next:
        s = s.next
        f = f.next.next
    
    # reverse second half. Lotta pointers here
    second = s.next
    s.next = prev = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    first, second = head, prev

    # merge
    while first and second:
        temp = first.next
        first.next = second
        second = temp
        first = first.next

#remove nth node from end of list. Separate 2 pointers by n nodes, then move both until end of list, and remove left pointer
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        l = dummy
        r = head
        while n > 0:
            r = r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next

        l.next = l.next.next

        return dummy.next





