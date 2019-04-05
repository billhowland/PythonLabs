// fibonacci.js

function fibonacci(num){
  if (num <= 1) return 1;

  return fibonacci(num - 1) + fibonacci(num - 2);

}

console.log(fibonacci(12))




const fibonacci = (n) => (n <= 1 ? n : fibonacci(n-1) + fibonacci(n-2))
const fibonacciList = (n) => [...Array(n+1).keys()].map(i => fibonacci(i))
console.log(fibonacciList(23))
