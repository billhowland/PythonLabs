# Practice 03-Lists6&7.py

# Problem 9: Given a list of numbers, and a target number, find a pair of
# numbers from the list that sum to a target number


def find_pair(nums, target):
    # while True:
    #     try:
    #         result = []
    #         for i in range(len(nums)-1):
    #             x = nums[i]
    #             next = nums[i+1]
    #             print(x, next, target)
    #             if x + next == target:
    #                 result.append([x, next])
    #             print('sum', x+next)
    #         return result
    #     except ValueError:
    #         break

    # result = []
    # for i in range(len(nums)):
    #     for j in range(len(nums)-1, -1, -1):
    #         if i >= j:
    #             break
    #         x = nums[i]
    #         next = nums[j]
    #         if x + next == target:
    #             result.append([x, next])
    # return result

    result = []
    for x in nums:
        difference = target - x
        if difference in nums:
            nums.remove(x)
            result.append([x, difference])
    return result

target = 7
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
        14, 15, 16, 17, 18, 19, 20]


print(find_pair(nums, target))
