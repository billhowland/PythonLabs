# Practice 03-Lists14.py
# Write a function which takes a list as a parameter and returns a new list
# with any duplicates removed.


def find_unique(nums):
    return sorted(list(set(nums)))


nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]


print(find_unique(nums))
