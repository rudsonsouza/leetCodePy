# Definition for singly-linked list.
from lib2to3.pytree import Node


class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sumListNode = ListNode(0)
        currentList = sumListNode
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Value = l1.val if l1 else 0
            l2Value = l2.val if l2 else 0
            columnSum = l1Value + l2Value + carry
            carry = columnSum // 10
            newList = ListNode(columnSum % 10)
            currentList.next = newList
            currentList = newList
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return sumListNode.next
        
# Call function
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

answer = Solution().addTwoNumbers(l1, l2)
while answer:
    print(answer.val, end=' ')
    answer = answer.next