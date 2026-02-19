# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head

    # Step 1: Find length
    length = 1
    tail = head

    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Reduce k
    k = k % length
    if k == 0:
        return head

    # Step 3: Make circular
    tail.next = head

    # Step 4: Find new tail
    steps_to_new_tail = length - k - 1
    new_tail = head
    for _ in range(steps_to_new_tail):
        new_tail = new_tail.next

    # Step 5: Set new head
    new_head = new_tail.next
    new_tail.next = None

    return new_head


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
    nums = list(map(int, input("Enter list elements (space separated): ").split()))
    k = int(input("Enter k: "))

    head = create_linked_list(nums)
    rotated_head = rotateRight(head, k)

    print("Rotated List:")
    print_linked_list(rotated_head)
