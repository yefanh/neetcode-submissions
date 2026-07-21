# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head

        for _ in range(left-1):
            leftPrev, cur = cur, cur.next

        prev = None
        for _ in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev # reverse the linkedlist
            prev = cur
            cur = tmpNext
            
        leftPrev.next.next = cur # cur now is in after the right pointer
        leftPrev.next = prev # prev now is in right pointer

        return dummy.next