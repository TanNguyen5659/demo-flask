# # Add Strings
# # Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# # Note:
# # The length of both num1 and num2 is < 5100.
# # Both num1 and num2 contains only digits 0-9.
# # Both num1 and num2 does not contain any leading zero.
# # Example:
# # Input: num1 = "30", num2 = "10"
# # Output: 40
# # The output should be given as an integer

# # def sum_str(str1,str2):
# #     return int(str1) + int(str2)

# # print(sum_str('30','10'))

# # Lucky Numbers
# # Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
# # Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
# # Example 1:
# # Input: arr = [2,2,3,4]
# # Output: 2
# # Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# # Example 2:
# # Input: arr = [1,2,2,3,3,3]
# # Output: 3
# # Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

# def lucky(arr):
#     freq = {}
#     for i in range(0,len(arr)):
#         if arr[i] not in freq:
#             freq[arr[i]] = 1
#         else:
#             freq[arr[i]] += 1
#     print(freq)
#     lst = []
#     if len(lst) > 0:
#         for k,v in freq.items():
#             if k == v:
#                 lst.append(k)
#         return max(lst)
#     return -1


# print(lucky([1,2,2,3,3,3]))
# print(lucky([2,2,3,4]))
# print(lucky([8,9,7,6]))

# Move Zeros
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example Input: [0,0,11,2,3,4]					
# Example Output: [11,2,3,4,0,0]

# def move_zeros(lst):
#     for i in range(0,len(lst)):
#         if lst[i] == 0:
#             lst += [lst.pop(i)]
#     return lst

# print(move_zeros([0,1,0,3,12]))

# Square(n) sum
# Create a function that given a list of integers squares each number passed into it and then sums the results together.
# Example Input: [1, 2, 2]
# Example Output: 9
#  Explanation: 1^2 + 2^2 + 2^2 = 9
# Example Input: [3, 4, 5]
# Explanation: 3^2 + 4^2 + 5^2 = 50
# Example Output: 50
def sum_s(lst):
    # sum = 0
    # for num in lst:
    #     sum += num**2
    return sum(x**2 for x in lst)
print(sum_s([3, 4, 5]))
