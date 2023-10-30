class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        result = [1] * length

        pre = [1] * length
        post = [1] * length
        
        for i in range(0, length-1):
            pre[i+1] = pre[i] * nums[i]

        for i in range(length-1, 0, -1):
            post[i-1] = post[i] * nums[i]
    
        for i in range(0, length):
            result[i] = pre[i] * post[i]
    
        return result