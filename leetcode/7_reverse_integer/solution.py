# # Given a 32-bit signed integer, reverse digits of an integer.

# # Example 1:
# # Input: 123
# # Output: 321

# # Example 2:
# # Input: -123
# # Output: -321
# 
# # Example 3:
# # Input: 120
# # Output: 21
# # Note:
# # Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
# # For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, data: int) -> int:
        if data < 0:inp = -data
        elif data > 0:inp = data
        else:return 0
        rev = 0
        while(inp!=0):
            rem = int(inp%10)
            rev = rev*10 + rem
            inp = int(inp/10)
        if ((-2**31) <= rev <= (2**31 - 1)) and (data < 0):
            return -rev
        elif ((-2**31) <= rev <= (2**31 - 1)) and (data > 0):
            return rev
        else:
            return 0

if __name__ == "__main__":
    output = Solution()
    data = int(input("Enter you digit: "))
    print(output.reverse(data))

        