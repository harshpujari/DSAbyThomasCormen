class Solution:
    def maxSubArray(self, nums):
        # Initialize variables to store the total sum and maximum sum
        total_sum = max_sum = nums[0] 
        
        # Iterate through the array starting from the second element
        for i in nums[1:]:
            # Update the total_sum to be the maximum of the current element and the running total_sum + current element
            total_sum = max(i, total_sum + i)
            
            # Update the max_sum to be the maximum of the current max_sum and the updated total_sum
            max_sum = max(max_sum, total_sum)
        
        # Return the maximum subarray sum
        return max_sum
