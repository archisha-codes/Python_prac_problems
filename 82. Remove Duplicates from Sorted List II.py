# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    if not head:
        return None

    dummy = ListNode(0)
    dummy.next = head

    prev = dummy

    while head:
        # If duplicate sequence found
        if head.next and head.val == head.next.val:
            
            # Skip all duplicates
            while head.next and head.val == head.next.val:
                head = head.next
            
            # Remove duplicate block
            prev.next = head.next
        else:
            prev = prev.next
        
        head = head.next

    return dummy.next


# -------- Helper Functions --------
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# -------- Main Driver --------
if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted list elements (space separated): ").split()))
    
    head = create_linked_list(nums)
    new_head = deleteDuplicates(head)

    print("List after removing duplicates:")
    print_linked_list(new_head)
