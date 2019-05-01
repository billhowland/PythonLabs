# Practice 03-Lists6&7.py
import time

# Problem 6:
# Write a function to move all the elements of a list with value less
# than 10 to a new list and return it.


def extract_less_than_ten(nums):
    lows = [num for num in nums if num < 10]
    return lows


nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(extract_less_than_ten(nums))
# It worked!

# Problem 7:
# Write a function to find all common elements between two lists.


def common_elements(nums1, nums2):
    # return [i for i, j in zip(nums1, nums2) if i == j] # positional
    # return [i for i in (nums1) if i in (nums2)]# not positional
    return (set(nums1) & set(nums2))  # sets, not positional
    # set & set = and (in both)
    # set | set = or (union)
    # set - set = difference
    # set ^ set = XOR


nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
start = time.time_ns()

print(common_elements(nums1, nums2), time.time_ns() - start)
