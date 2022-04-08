# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 중간점 찾기
        count = 1
        temp = head
        while temp.next is not None:
            count += 1
            temp = temp.next
        # 중간지점으로 이동해서 return
        for i in range(count//2):
            head = head.next
            print(head)
        return head
