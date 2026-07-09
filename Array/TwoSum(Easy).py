class Solution:
    def twoSum(self, nums , target):
        num_map={}
        for i, num in enumerate(nums):
            c=target - num
            if c in num_map:
                return [num_map[c],i]
            num_map[num]=i
nums=[2,7,11,15]
target=9
solution=Solution()
result=solution.twoSum(nums,target)
print(result)            