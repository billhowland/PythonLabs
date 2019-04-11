// dict 1

function lists_to_dict(keys, values) {
   /*
   returns dictionary of keys mapped to values
   :keys: arr
   :values: arr
   */

   // lists_to_dict(['a', 'b', 'c'], ['aardvark', 'bear', 'coyote']) // {'a': 'aardvark', 'b': 'bear', 'c': 'coyote'}
  let combined = {}
  keys.map((elem, idx) => {
    console.log(Object.assign(combined, {[elem]: values[idx]}))
  return combined
}
