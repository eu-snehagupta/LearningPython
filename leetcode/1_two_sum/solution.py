# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        lenght = len(nums)
        for i in range(0, lenght):
            for j in range(i+1, lenght):
                if nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    j = j+1
            i = i + 1

if __name__ == "__main__":
    nums= list()
    lenght = int(input("Enter the length of the list: "))
    for i in range (0,lenght):
        numberlist = int(input("Enter the number list: "))
        nums.append(numberlist)
    target = int(input("Enter the traget number: "))
    output = Solution ()
    print(output.twoSum(nums,target))
