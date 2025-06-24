class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry

        carry = total // 10
        current.next = ListNode(total % 10)

        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next

# Time Complexity: O(max(m, n)), where m and n are the lengths of the linked lists l1 and l2. We traverse both lists once.
# Space Complexity: O(max(m, n)), for the resulting linked list which can be at most the length of the longer input list plus one for the carry.
# Note: This solution efficiently handles the addition of two numbers represented by linked lists, returning a new linked list representing their sum.