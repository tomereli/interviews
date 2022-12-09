import random
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, nodes=[]) -> None:
        self.head = None
        self.len = 0
        for i in range(len(nodes) - 1, -1, -1):
            self.addAtHead(nodes[i])

    def addAtHead(self, val) -> None:
        self.head = ListNode(val, self.head)
        self.len += 1
    
    def toList(self) -> list:
        l = []
        cur = self.head
        while cur:
            l.append(cur.val)
            cur = cur.next
        return l

class maxSubArrSum:
    def __init__(self, sum, start, end):
        self.sum = sum
        self.start = start
        self.end = end

    @property
    def len(self):
        return self.end - self.start

    def copy(self, other):
        self.sum = other.sum
        self.start = other.start
        self.end = other.end

    def checkAndUpdate(self, other):
        if other.sum > self.sum:
            self.copy(other)
        elif other.sum == self.sum and self.len < other.len:
            self.copy(other)
        elif other.sum == self.sum and self.len == other.len and other.start < self.start:
            self.copy(other)

def rand_list(n):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(3,9))
    return rand_list


# https://www.interviewbit.com/problems/pick-from-both-sides/
import unittest

class Solution(unittest.TestCase):
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def __init__(self, *args, **kwargs):
        super(Solution, self).__init__(*args, **kwargs)

    def pickFromBothSides(self, A, B):
        left = 0
        right = B
        s = sum(A[-right:])
        max_sum = s
        while (right > 0):
            s = s - A[-right] + A[left]
            if s > max_sum:
                max_sum = s

            left = left + 1
            right = right - 1
        return max_sum
    
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        max = maxSubArrSum(-9999999, -1, -1)
        cur = maxSubArrSum(-9999999, -1, -1)
    
        #print(A)
        for i in range(len(A)):
            # Completed segment
            if A[i] < 0:
                if cur.start > -1:
                    cur.end = i
                    max.checkAndUpdate(cur)
                    cur = maxSubArrSum(-9999999, -1, -1)
                continue
            
            # Positive number - either continue counting cur or start a new count
            if cur.start < 0:
                cur.start = i
                cur.sum = A[i]
            else:
                cur.sum = cur.sum + A[i]
       
        # Finished. Check if the last segment
        if cur.start > -1:
            cur.end = i + 1
            max.checkAndUpdate(cur)
        
        if max.start == -1:
            return []
        if max.start == max.end:
            return [A[max.start]]
        return A[max.start:max.end]

    def removeDuplicates(self, nums: list[int]) -> int:
        prev = nums[0]
        w = 1
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[w] = nums[i]
                prev = nums[w]
                w += 1
        return w
    
    def test_removeDuplicates(self):
        self.assertEqual(self.removeDuplicates([1,1,2]), 2)

    def removeElement(self, nums: list[int], val: int) -> int:
        w = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[w] = nums[i]
                w += 1
        return w

    def reverseStringImpl(self, i, j, s) -> None:
        # This is actually O(n) space...
        if i >= j:
            return

        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp

        self.reverseStringImpl(i + 1, j - 1, s)

    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """ 
        return self.reverseStringImpl(0, len(s) - 1, s)
    
    def test_reverseString(self):
        S = ["a","b","c","d","e", "f"]
        self.reverseString(S)
        self.assertEqual(S, ["f", "e", "d", "c", "b", "a"])

    def test_removeElement(self):
        self.assertEqual(self.removeElement([0,1,2,2,3,0,4,2], 2), 5)
    
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        w = n + m - 1
        r1 = m - 1
        r2 = n - 1

        for w in range(n + m - 1, -1 , -1):
            if r1 < 0:
                nums1[w] = nums2[r2]
                r2 -=1
            elif r2 < 0:
                nums1[w] = nums1[r1]
                r1 -=1
            else:
                if nums1[r1] > nums2[r2]:
                    nums1[w] = nums1[r1]
                    r1 -= 1
                else:
                    nums1[w] = nums2[r2]
                    r2 -= 1
        return nums1

    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        This is using 2 indexes only, Much less readable and harder to understand.
        """
        i = m - 1 # index in nums1 arr
        j = n - 1 # index in nums2 arr
        #out = [-1]*(m+n)
        while i >= 0 and j >= 0:
            end = i + j + 1
            if  nums1[i] > nums2[j]:
                nums1[end] = nums1[i]
                i -= 1
            else:
                nums1[end] = nums2[j]
                j -= 1
        end = i + j + 1
        for l in range(end, -1 , -1):
            if i < 0:
                nums1[l] = nums2[j]
                j -= 1
            else:
                nums1[l] = nums1[i]
                i -= 1
        return nums1

    def test_merge(self):
        self.assertEqual(self.merge([1,2,3,0,0,0], 3, [2,5,6], 3), [1,2,2,3,5,6])
        self.assertEqual(self.merge([0], 0, [1], 1), [1])

    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        dups = 0
        for i in range(length):
            if arr[i] == 0:
                dups = dups + 1
            if dups + i + 1 == length:
                break
            if dups + i + 1 > length:
                dups = dups - 1
                arr[length - 1] = 0
                length = length - 1
                break

        dst = length - 1
        src = length - dups - 1
        while dst >= 0:
            val = arr[src]
            arr[dst] = val
            if val == 0:
                    arr[dst - 1] = 0
                    dst = dst - 1
            dst = dst - 1
            src = src - 1
        return arr

    def test_duplicateZeroes(self):
        self.assertEqual(self.duplicateZeros([1,0,2,3,0,4,5,0]), [1,0,0,2,3,0,0,4])
        self.assertEqual(self.duplicateZeros([8,4,5,0,0,0,0,7]), [8,4,5,0,0,0,0,0])

    def test_maxset_simple(self):
        self.assertEqual(self.maxset([ 1, 2, 5, -7, 2, 5 ]), [1, 2, 5] )
        self.assertEqual(self.maxset([ 756898537, -1973594324, -2038664370, -184803526, 1424268980 ]), [1424268980])
        self.assertEqual(self.maxset([ -1469348094, 1036140795, 2040651434, -317097467, 1376710097, 1330573317, 1687926652 ]), [1376710097, 1330573317, 1687926652])



        self.assertEqual(self.maxset([ -1, -1, -1, -1, -1 ]), [])

    def test_pickFromBothSides_simple(self):
        self.assertEqual(15, self.pickFromBothSides([1,2,3,4,5,6], 3))
        self.assertEqual(3, self.pickFromBothSides([1,2,-3,4,5,-6], 3))
        
    def swapPairsRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tmp = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairsRecursive(tmp)
        return head
    
    def test_swapPairsRecursive(self):
        l = LinkedList([1,2,3,4,5,6])
        l.head = self.swapPairsRecursive(l.head)
        self.assertEqual(l.toList(), [2,1,4,3,6,5])
    
    def swapPairsIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        next = head.next.next
        head, head.next = head.next, head
        head.next.next = next

        while next and next.next:
            tmp = next.next.next
            next, next.next = next.next, next
            next.next.next = tmp
            next = tmp
        
        return head

    def test_swapPairsIterative(self):
        l = LinkedList([1,2,3,4])
        l.head = self.swapPairsIterative(l.head)
        self.assertEqual(l.toList(), [2,1,4,3])
    
if __name__ == "__main__":
    unittest.main()
