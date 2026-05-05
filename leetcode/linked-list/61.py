# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def size(self, head):
        num = 0
        while head:
            head = head.next
            num += 1
        return num

    def rotateRight(self, head, k):
        temp = head
        prev = None
        res = None

        length = self.size(head)

        if length == 0:
            return head

        rotate = k % length

        if rotate == 0:
            return head

        for i in range(length):
            if i == length - rotate:
                res = temp
                prev.next = None
                break

            prev = temp
            temp = temp.next

        temp = res
        while temp and temp.next:
            temp = temp.next

        temp.next = head

        return res
