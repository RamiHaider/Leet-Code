class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        empty_Dictionary = {}

        #length constraints
        if len(nums) < 2 or len(nums) > 10**4:  
            print("Length of the list is out of bounds")
            return [] 
        
        #target constraints
        if target < -10**9 or target > 10**9:
            print("Target is out of bounds")
            return []
        
        for index,value in enumerate(nums):

            #max value in list contraints
            if nums[index] < -10**9 or nums[index] > 10**9:
                print(f"The value of {nums[index]} is out of bounds")
                return []
                
            if not (target - value) in empty_Dictionary.keys():
                empty_Dictionary[value] = index
                continue

            if (target - value) in empty_Dictionary.keys():
                return [empty_Dictionary[(target-value)],index]
                
        print(f'No target value found within the list')
        return []
    
#Leet Code: 48ms, beats 96.63% of users

test = Solution()
print(test.twoSum([2,7,11,15],9))
#outputs [0,1]
print(test.twoSum([2],5))
#outputs "Length of the list is out of bounds"
print(test.twoSum([2,5],6))
#outputs "No Target value found"
print(test.twoSum([100000000000000,4,5,5],3))
#outputs "The value of 100.... is out of bounds"