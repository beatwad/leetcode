from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if list is empty - return
        if head is None:
            return head
        n = 1
        ll_head = head
        # get the length of the list
        while head.next:
            head = head.next
            n += 1
        # decrease k according to list length
        k = n - k % n
        # if number of rotations is multiple of list length - return
        if k == 0:
            return ll_head
        # get the list's end
        ll_end = head
        ll_end.next = ll_head
        # go back to the beginning
        head = ll_head
        # move for k iterations, then change the beginning of the list
        while k > 1:
            head = head.next
            k -= 1
        ll_begin = head.next
        head.next = None
        return ll_begin


if __name__ == '__main__':
    def generate_linked_list(nums):
        first_a = ListNode(nums[0])
        _a = first_a
        for i in range(1, len(nums)):
            _a.next = ListNode(nums[i])
            _a = _a.next
        return first_a

    sol = Solution()

    a = generate_linked_list([1, 2])
    c = sol.rotateRight(a, 2)
    res = []
    while c:
        res.append(c.val)
        c = c.next

    assert res == [1, 2]

    a = generate_linked_list([1, 2, 3, 4, 5])
    c = sol.rotateRight(a, 2)
    res = []
    while c:
        res.append(c.val)
        c = c.next

    assert res == [4, 5, 1, 2, 3]

    a = generate_linked_list([1, 2, 3])
    c = sol.rotateRight(a, 2)
    res = []
    while c:
        res.append(c.val)
        c = c.next

    assert res == [2, 3, 1]

    a = generate_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 5, 2, 0, 2])
    c = sol.rotateRight(a, 600000000)
    res = []
    while c:
        res.append(c.val)
        c = c.next

    assert res == [3, 4, 5, 6, 7, 8, 9, 22, 5, 2, 0, 2, 1, 2]

