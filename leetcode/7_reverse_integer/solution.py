# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
# Input: 123
# Output: 321

# Example 2:
# Input: -123
# Output: -321
# 
# # Example 3:
# Input: 120
# Output: 21

class Solution:
    def reverse(self, data: int) -> int:
        inp = data
        rev = 0
        while(inp!=0):
            rem = int(inp%10)
            rev = rev*10 + rem
            inp = int(inp/10)
        return rev

if __name__ == "__main__":
    output = Solution()
    data = int(input("Enter you digit: "))
    if data  < 0:
        print(-1*(output.reverse(-1*data)))
    else:
        print(output.reverse(data))


# class Solution:
#     def returninput(self, data: int) -> int:
#         if(data<0):
#             return -1 * reverse(-1*data)
#         else:
#             return reverse(data)
#     def reverse(self, data: int) -> int:
#         inp = data
#         rev = 0
#         while(inp!=0):
#             rem = int(inp%10)
#             rev = rev*10 + rem
#             inp = int(inp/10)
#         return rev