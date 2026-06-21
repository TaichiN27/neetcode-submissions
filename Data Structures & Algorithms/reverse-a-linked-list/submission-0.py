# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        prev = None

        while head:
            print(head.val)
            # nxt保存
            nxt = head.next

            # 矢印を逆に
            head.next = prev
            
            # currentを進める

            prev = head
            head = nxt

        return prev


                