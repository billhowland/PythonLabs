// fundamentals04-reduce.js

let max_element = (a, b, c) => [a, b, c].reduce((acc, cur) => (acc > cur ? acc : cur)) 

max_element = (a, b, c) => Math.max(a, b, c)

max_element = (a, b, c) => {
  let running_max = -Infinity
  for (let num of [a, b, c]){
    if (num > running_max){
      running_max = num
    }
  }
  return running_max
}

  nums = [1, 3, 5]

  console.log(max_element(nums))
