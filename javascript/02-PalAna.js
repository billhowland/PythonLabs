// 02-palana.js

let check_palindrome = (word) => {
  if (word === word.split("").reverse().join("")) {
    return (`Yes, ${word} is a palindrome.`)
  }else{
    return (`No, ${word} is not a palindrome.`)
  }
}

console.log(check_palindrome("word"))

// This worked!
// ----------------------------------------------------------------------------

let check_anagram = (worda, wordb) => {
   return ((worda.split("").sort().join("")) == (wordb.split("").sort().join("")))
}

console.log(check_anagram("word","drow"))

// This worked!
// ----------------------------------------------------------------------------
