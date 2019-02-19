# Practice 03-Lists11.py
# Write a function combine_all that takes a list of lists, and returns a list
# containing each element from each of the lists.
# nums = [[5,2,3],[4,5,1],[7,6,3]]
# combine_all(nums) → [5,2,3,4,5,1,7,6,3]


def combine_all(nums):
    return sum(nums, [])


nums = [[5, 2, 3], [4, 5, 1], [7, 6, 3]]


print(combine_all(nums))
