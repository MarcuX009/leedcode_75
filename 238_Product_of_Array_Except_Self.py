# Solution for `238. Product of Array Except Self`
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # init
        left = [1] * n 
        right = [1] * n
        answer = [0] * n
        
        #left    
        for i in range(1, n): # range(start, stop, step)
            left[i] = left[i-1] * nums[i-1]

        #right   
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        for i in range(n):
            answer[i] = left[i] * right[i]
        return answer
