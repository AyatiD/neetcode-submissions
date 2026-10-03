class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            # Get values, or 0 if one list has ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add the two digits and carry
            total = val1 + val2 + carry

            # Digit to put in the new node
            digit = total % 10

            # Carry for the next position
            carry = total // 10

            # Create and attach new node
            current.next = ListNode(digit)
            current = current.next

            # Move through the input lists
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next