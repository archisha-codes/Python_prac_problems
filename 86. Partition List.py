class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x):
        if head is None:
            return None
        
        h1 = t1 = None
        h2 = t2 = None
        
        while head:
            temp = head
            head = head.next
            temp.next = None
            
            if temp.val < x:
                if h1 is None:
                    h1 = t1 = temp
                else:
                    t1.next = temp
                    t1 = temp
            else:
                if h2 is None:
                    h2 = t2 = temp
                else:
                    t2.next = temp
                    t2 = temp
        
        if t1:
            t1.next = h2
            return h1
        else:
            return h2


# 🔹 Helper function to print linked list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# 🔹 Create sample linked list
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

x = 3

sol = Solution()
new_head = sol.partition(head, x)

print_list(new_head)
