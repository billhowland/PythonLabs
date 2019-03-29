// Problem 6:
// # Write a function to move all the elements of a list with value less
// # than 10 to a new list and return it.
//
// def extract_less_than_ten(nums):
//    lows = [num for num in nums if num < 10]
//    return lows
//
// nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
//
// print (extract_less_than_ten(nums))
// #It worked!

// Practice 03-Lists 6

// -----------------------------------------------------------------------------

nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
function extract_less_than_ten(nums) {
  let less_than_ten = []
  for (let i=0; i<nums.length; i++) {
    if (nums[i] < 10) {
      less_than_ten.push(nums[i])
    }
  }
  return less_than_ten
}
console.log(extract_less_than_ten(nums))

// -----------------------------------------------------------------------------

nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
const extract_less_than_ten_using_filter = (nums) => nums.filter(x => x<10)

// -----------------------------------------------------------------------------
