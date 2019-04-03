// calculator.js

// DOM selectors
const displayDiv = document.querySelector('#display')
const acDiv = document.querySelector('#AC')
const ceDiv = document.querySelector('#CE')
const eqDiv = document.querySelector('#eq')
const decDiv = document.querySelector('#dec')
const digits = document.querySelectorAll('.num')
const ops = document.querySelectorAll('.op')

const add = (a, b) => a + b
const subtract = (a, b) => a - b
const multiply = (a, b) => a * b
const divide = (a, b) => a / b
const updateDisplay = (value) => {
  displayDiv.innerText = value
}

let running_total = 0
let current_value = ''
let decimal = false
let operator = null

updateDisplay(running_total)

acDiv.addEventListener('click', () => {
  running_total = 0
  current_value = 0
  updateDisplay(running_total)
})

ceDiv.addEventListener('click', () => {
  current_value = 0
  updateDisplay(running_total)
})

digits.forEach(elem => {
  let digit = elem.innerText
  elem.addEventListener('click', () => {
    current_value += digit
    updateDisplay(current_value)
  })
})

decDiv.addEventListener('click', () => {
  if (!decimal) {
    current_value += '.'
    updateDisplay(current_value)
    decimal = true
  }
})

ops.forEach(elem => {
  let op = elem.id
  elem.addEventListener('click', () => {
    if (operator === null) {
      running_total = current_value
    }
    operator = op
    current_value = ''
    updateDisplay(current_value)
  })
})

eqDiv.addEventListener('click', () => {
    if (current_value) {
    let a = parseFloat(running_total)
    let b = parseFloat(current_value)
    if (operator === 'add') {
      running_total = add(a, b)
    } else if (operator === 'sub') {
      running_total = subtract(a, b)
    } else if (operator === 'mult') {
      running_total = multiply(a, b)
    } else if (operator === 'divide') {
      running_total = divide(a, b)
    }
    current_value = ''
  }
  updateDisplay(running_total)
})
