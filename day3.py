#concatenation of array
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []
        for i in range(len(2*nums)): #iterating over the size of ans
            ans.append(nums[i%n]) #append the value at i % n at ans[i]
        return ans
    
sol = Solution()
nums = [1, 2, 3, 2, 1]
final = sol.getConcatenation(nums)
print(final)
