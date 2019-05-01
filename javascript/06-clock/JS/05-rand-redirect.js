// clock.js



function getRandomInt() {
  return Math.floor(Math.random() * Math.floor(Object.keys(sites).length));
}

console.log(sites[getRandomInt()])
