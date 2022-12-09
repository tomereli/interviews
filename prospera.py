
import unittest

class Solution(unittest.TestCase):
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def __init__(self, *args, **kwargs):
        super(Solution, self).__init__(*args, **kwargs)
    
    def find_max_islands(self, A) -> list:
        i = 0
        j = 0
        cur_sum = 0
        while i < len(A[0]):
            if A[i][0]:
                cur_sum = cur_sum + 1


    def test_islands(self, A) -> list:
        #self.assertEquals()
        
if __name__ == "__main__":
    unittest.main()
