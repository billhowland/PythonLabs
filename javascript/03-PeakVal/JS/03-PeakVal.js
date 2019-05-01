// 03peakvalley.js

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
//  peaks at 6 and 14
//  valleys at 9, 17

// returns indices of peaks:

let peaks = (data) => {
  let pks = []
  for (let i=1; i<data.length-1; i++){
    if ((data[i] > data [i-1]) && (data[i] > data[i+1])){
      pks.push(i)
    }
  }
  return pks
}
console.log(peaks(data))
// returns indices of valleys:

let valleys = (data) => {
  let vals = []
  for (let i=1; i<data.length-1; i++){
    if ((data[i] < data [i-1]) && (data[i] < data[i+1])){
      vals.push(i)
    }
  }
  return vals
}
console.log(valleys(data))
// compile list of peaks and valleys in order NOT WORKING

let pksnvals = (data) => {
  return peaks(data).concat(valleys(data))


}
alert(pksnvals(data))
//
// def valleys(data):  # returns indices of valleys
//     return [i for i in range(1, (len(data)-1)) if data[i] < data[i-1]
//             and data[i] < data[i+1]]
//
//
// def peaksnvalleys(data):  # compile list of peaks and valleys in order
//     return sorted(valleys(data) + peaks(data))
//
//
// def printxs(data):
//     x = max(data)
//     while x > 0:
//         print(' ', end='')
//         for y in data:
//             if y >= x:
//                 print('X  ', end='')
//             if y < x:
//                 print('-  ', end='')
//         x -= 1
//         print('')
//
//
// def main():  # do the stuff
//
//     printxs(data)
//     print(data)
//     print(f"Peaks = {peaks(data)}")
//     print(f"Valleys = {valleys(data)}")
//     print(f"Peaks and Valleys = {peaksnvalleys(data)}")
//
//     # ----------------------------------------------------------------
//
//
// if __name__ == '__main__':
//
//     run = 1
//     while run:
//
//         # --------------------------------------------------------
//
//         main()
//
// # ----------------------------------------------------------------
//
//         ask = input('Quit? Y/N > ').strip().lower()
//         if ask == 'y':
//             run = 0
