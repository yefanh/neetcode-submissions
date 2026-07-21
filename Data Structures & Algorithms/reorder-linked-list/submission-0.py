# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1 -> 2 -> 3 -> 4 -> 5 -> N
        #           s              f
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # split
        # 1 -> 2 -> 3 -> N
        #                prev
        # 4 -> 5 -> N
        # sec 
        second = slow.next # the 1st node of sencond half              
        prev = slow.next = None

        # reverse the second half linkedList
        # N <- 4 -> 5 -> N
        #          tmp
        #      pre  sec
        while second:
            tmp = second.next # tmp = 5
            second.next = prev # 4 -> N
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
