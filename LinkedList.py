# 206 reverse linked list
# Ugh, this is weird in python

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

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

# deep copy of list with pointers to next and to random node
def copyRandomList(self, head: Node) -> Node:
        oldToCopy = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next


        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]

# 2. add two numbers. Add each digit, keep track of remainder. Return new list with dummy head. Easy Stuff
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        result = dummy = ListNode()
        multiplier = 1
        remainder = 0
        while cur1 or cur2:
            temp = 0
            if cur1:
                temp += cur1.val
                cur1 = cur1.next
            if cur2:
                temp += cur2.val
                cur2 = cur2.next
            temp += remainder
            result.next = ListNode(temp % 10, None)
            result = result.next
            remainder = temp // 10

        if remainder:
            result.next = ListNode(remainder, None)

        return dummy.next

# 141. Linked List Cycle. 2 pointers, one moves 2 at a time, one moves 1 at a time. If they meet, there is a cycle
def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = f = head
        while f:
            s = s.next
            f = f.next

            if f:
                f = f.next
            else:
                return False
            
            if s == f:
                return True
            

# 287. find duplicate number. 2 pointers, one moves 1 at a time, one moves 2 at a time. When they meet, move one back to start, and move both 1 at a time. When they meet, that is the duplicate. 
# Floyd's cycle detection algorithm. Just have to know it            
def findDuplicate(self, nums: list[int]) -> int:
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    newSlow = 0

    while newSlow != slow:
        slow = nums[slow]
        newSlow = nums[newSlow]

    return slow


            

