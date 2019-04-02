// Lists 7.js

// Problem 7:

const common_elements = (nums1, nums2) => nums1.filter(x => nums2.includes(x))

  nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
  nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

  console.log(common_elements(nums1, nums2))
