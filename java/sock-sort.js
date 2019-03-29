// sock-sort.js

const sockTypes = ['ankle', 'crew', 'calf', 'thigh']
const sockList = []
const sockCounter = {}

for (let i=0; i<100; i++) {
  //randomly select sock from socktypes
  let sock = sockTypes[Math.floor(Math.random() * sockTypes.length)]
  sockList.push(sock)

  sockCounter[sock] = (sockCounter[sock] || 0) + 1

  // if (sockCounter.hasOwnProperty(sock)) {
  //   sockCounter[sock] += 1
  // }else{
  //   sockCounter[sock] = 1
  // }
}

for (let sock in sockCounter) {
  console.log(`${sock} has ${sockCounter[sock] % 2} loner(s).`)
}

console.log(sockList)
console.log(sockCounter)

// ----------------------------------------------------------------------------

const sockTypes = ['ankle', 'crew', 'calf', 'thigh']
const sockColors = ['black', 'white', 'blue']
const sockList = []
const sockCounter = {}

for (let i=0; i<100; i++) {
  //randomly select sock from socktypes
  let type = sockTypes[Math.floor(Math.random() * sockTypes.length)]
  let color = sockColors[Math.floor(Math.random() * sockColors.length)]
  let sock = [type, color]
  sockList.push(sock)

  sockCounter[sock] = (sockCounter[sock] || 0) + 1

  // if (sockCounter.hasOwnProperty(sock)) {
  //   sockCounter[sock] += 1
  // }else{
  //   sockCounter[sock] = 1
  // }
}

for (let sock in sockCounter) {
  console.log(`${sock} has ${sockCounter[sock] % 2} loner(s).`)
}

console.log(sockList)
console.log(sockCounter)
