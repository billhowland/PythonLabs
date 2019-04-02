
// Practice 02: Problem 1:
let doubleLetters = (strang) => {
  return (((strang.split("")) + (strang.split(""))).join(""))
}
console.log(doubleLetters("word"))

// ----------------------------------------------------------------------------

function double_letter_using_loops(text){
  let double_string = ''
  for (let i=0; i<text.length; i++) {
    double_string += text[i] text [i]
  }
  return double_string
}
// Worked
// ----------------------------------------------------------------------------

const double_letters_using_map = (text) => text.split('')
                                               .map(letter => letter + letter)
                                               .join('') 
// Worked
