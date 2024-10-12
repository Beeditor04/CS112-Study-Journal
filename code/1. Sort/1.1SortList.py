class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def getLength(head):
            n = 0
            while head:
                n += 1
                head = head.next
            return n

        def merge(left, right):
            dummy = ListNode(0)
            cur = dummy
            while left and right:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next
            cur.next = left if left else right
            return dummy.next
        def mergeSort(head, length):
            if length == 1:
                return head
            mid = length // 2
            midNode = head
            cut_tail = None
            for i in range(mid):
                cut_tail = midNode
                midNode = midNode.next  
            cut_tail.next = None
            left = mergeSort(head, mid)
            right = mergeSort(midNode, length - mid)
            return merge(left, right)
        if not head or not head.next:
            return head
        length = getLength(head)
        head = mergeSort(head, length)
        return head
        
s = Solution()
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
res = s.sortList(head)
while res:
    print(res.val)
    res = res.next