# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        n1 = n2 = 0

        # Traverse through the NodeList l1
        TotalDigits = 1
        NextNodeList = l1
        while True:
            n1 += TotalDigits * NextNodeList.val
            TotalDigits *= 10
            if NextNodeList.next == None: break
            else: NextNodeList = NextNodeList.next

        # Traverse through the NodeList l2
        TotalDigits = 1
        NextNodeList = l2
        while True:
            n2 += TotalDigits * NextNodeList.val
            TotalDigits *= 10
            if NextNodeList.next == None: break
            else: NextNodeList = NextNodeList.next

        # Prep sum as str
        sum = str(n1 + n2)
        print("Sum", sum)
        
        # Prep ReturnList using a foreach loop
        ReturnList = None
        for num in sum:
            ReturnList = ListNode(num, ReturnList)
        return ReturnList
