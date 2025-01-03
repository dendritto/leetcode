class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # Create a dictionary to store the difference and its index
        num_dict = {}
        
        # Iterate over the list of numbers
        for i, num in enumerate(nums):
            # Calculate the difference needed to reach the target
            diff = target - num
            
            # Check if the difference is already in the dictionary
            if diff in num_dict:
                # If found, return the indices of the two numbers
                return [num_dict[diff], i]
            
            # Otherwise, add the number and its index to the dictionary
            num_dict[num] = i
        
        # If no solution is found, return an empty list
        return []
    