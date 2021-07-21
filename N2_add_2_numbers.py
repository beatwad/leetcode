class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = ListNode()
        l3 = first

        while l1 or l2:
            if not l1:
                l3.val += l2.val
                l2 = l2.next
            elif not l2:
                l3.val += l1.val
                l1 = l1.next
            else:
                l3.val += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next

            surplus, l3.val = divmod(l3.val, 10)

            if l1 or l2 or surplus > 0:
                l3.next = ListNode(surplus)
                l3 = l3.next

        return first


if __name__ == '__main__':

    def generate_linked_list(nums):
        first_a = ListNode(nums[0])
        _a = first_a
        for i in range(1, len(nums)):
            _a.next = ListNode(nums[i])
            _a = _a.next
        return first_a

    a = generate_linked_list([2, 4, 3])
    b = generate_linked_list([5, 6, 4])

    sol = Solution()

    c = sol.addTwoNumbers(a, b)
    res = []

    while c:
        res.append(c.val)
        c = c.next

    assert res == [7, 0, 8]

    a = generate_linked_list([9, 9, 9, 9, 9, 9, 9])
    b = generate_linked_list([9, 9, 9, 9])

    sol = Solution()

    c = sol.addTwoNumbers(a, b)
    res = []

    while c:
        res.append(c.val)
        c = c.next

    assert res == [8, 9, 9, 9, 0, 0, 0, 1]

