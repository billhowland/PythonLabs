// Dicts3.js
// Average numbers whose keys start with the same letter. Output a dictionary
// containing those letters as keys and the averages.
//

function avgs_to_dict(d) {
  let combined = {}
  for (let key in d) {
    let first_letter = key[0]
    let val = d[key]
    if (combined.hasOwnPropery(first_letter)) {
      [current_sum, count] = combined[first_letter]
      combined[first_letter] = [current_sum + val, count +1]
    } else {
      combined[first_letter] = [val, 1]
    }
  }
  return Object.assign({}, ...Object.entries(combined).map(([key, [rsum, count]]) => ({[key]: rsum/count})))
}



d = {'a1': 4, 'a2': 2, 'a3': 3, 'b1': 10, 'b2': 1, 'b3': 1, 'c1': 4,
     'c2': 5, 'c3': 6}


// OR:

function unify(d) {
    let firsts = new Set(Object.keys(d).map(key => key[0])) // set of first letters
    let avg = {}
    for (let letter of firsts) {
        let group = Object.entries(d).filter(([key, val]) => key[0] == letter)
        let sum = group.reduce((total, current) => total + current[1], 0)
        avg[letter] = sum / group.length
    }
    return avg
}
