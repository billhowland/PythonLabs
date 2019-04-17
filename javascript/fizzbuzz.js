// fizzbuzz.js

function fizzbuzz(n) {
  for (let num = 0; num <= 100; num++) {
    let outstr = ''
    if (num % 3 === 0) outstr += 'fizz'
    if (num % 5 === 0) outstr += 'buzz'
    if (num % 7 === 0) outstr += 'fuzz'
    if (num % 9 === 0) outstr += 'baz'
    console.log(outstr ? outstr : num)
  }
}

function fizzbuzzfuzzbaz(n) {
  const translate = {3: 'fizz', 5: 'buzz', 7: 'fuzz', 9: 'baz'}
  for (let i=1; i<=n; i++) {
    let num = ''
    for (let k in translate) {
      if (i % k === 0) num += translate(k)
    }
    console.log(num ? num : i)
  }
}
