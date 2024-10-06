#day1 - remove duplicates from sorted array

class Solution:
    def removeDuplicates(self, nums:list[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l

# Create an instance of the Solution class
sol = Solution()

# Initialize the input list nums
nums = [3, 2, 2, 3]
val = 3

# Call the removeDuplicates method to remove all instances of duplictae int from nums
new_length = sol.removeDuplicates(nums)

# Print the new length of the array after removing duplicates
print("New length:", new_length)          

# Print the modified array containing only the original elements
print("Modified array:", nums[:new_length])  
