#快慢指针

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        slow,fast=head,head
        for i in range(k):
            if not fast:
                return None
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        return slow