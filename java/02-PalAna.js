// # 17palana.py
// # Version 1:
//
// # define functions here-------------------------------------------
//
//
// def check_palindrome(word):
//     if word == word[::-1]:
//         return (f'Yes, {word} is a palindrome.')
//     else:
//         return (f'No, {word} is not a palindrome.')
//
//
// def check_anagram(worda, wordb):
//     # Remove all spaces from each word (replace) str.replace(old, new[, max])
//     # worda = worda.replace(' ', '')
//     # wordb = wordb.replace(' ', '')
//     # Sort the letters of each word (sorted) b = sorted(a) returns a list
//     # sworda = sorted(worda)
//     # swordb = sorted(wordb)
//     # Check if the two are equal
//     # return sworda == swordb
//     return (sorted(worda.replace(' ', '')) == sorted(wordb.replace(' ', '')))
//
//
// def main():
//     word = input('Enter a word: ').strip().lower()
//     print(check_palindrome(word))
//
//     worda = input('Enter the first word: ').strip().lower()
//     wordb = input('Enter the second word: ').strip().lower()
//     print(check_anagram(worda, wordb))
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
