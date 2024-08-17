class Solution:
    def scoreOfString(self, s: str) -> int:
        s = s.lower()
        total = 0

        if len(s) < 2 or len(s) > 100:
            print("Length of string is out of bounds")
            return

        for i in range(len(s)-1):
            total += abs(ord(s[i]) - ord(s[i+1]))
        return total

test = Solution()
print(test.scoreOfString("zaz"))
##output = 50
print(test.scoreOfString("HeLLo"))
#output = 3
print(test.scoreOfString("g"))
#Length of string is out of bounds