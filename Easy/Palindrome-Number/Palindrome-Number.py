import math

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        #This part converts the number x into a list
        #i.e., 512 becomes [5,1,2]
        x_list = []
        while x > 0:
            x_list.append(x % 10)
            x = x // 10
        
        #This part takes the converted list and 
        #finds whether it is Palindrome or not
        for i in range(0,(math.floor((len(x_list)/2)))): 
            if x_list[i] != x_list[(i*(-1)) - 1]:
                return False
        return True

test = Solution()
