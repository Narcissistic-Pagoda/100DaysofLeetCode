#day2 - remove element which matches with the given val in an array

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Initialize a pointer l to track the position for the next non-val element
        l = 0
        
        # Iterate through each element in the nums list
        for i in range(len(nums)):
            # Check if the current element is not equal to the specified value (val)
            if nums[i] != val:
                # Place the current non-val element at the position pointed by l
                nums[l] = nums[i]
                # Increment l to move to the next position
                l += 1
        
        # Return the length of the modified array with non-val elements
        return l


# Create an instance of the Solution class
sol = Solution()

# Initialize the input list nums and the value to be removed val
nums = [3, 2, 2, 3]
val = 3

# Call the removeElement method to remove all instances of val from nums
new_length = sol.removeElement(nums, val)

# Print the new length of the array after removal of val
print("New length:", new_length)           # Output: New length: 2

# Print the modified array containing only the elements that are not val
print("Modified array:", nums[:new_length])  # Output: Modified array: [2, 2]
