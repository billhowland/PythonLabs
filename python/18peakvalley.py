# 18peakvalley.py
# Version 1:

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
#  peaks at 6 and 14

# define functions here-------------------------------------------


def peaks(data):  # returns indices of peaks
    # return [data.index(i) for i in data if data.index(i) > 1 and data.index(i)
            # < len(data) and i > (data[data.index(i) - 1])
            # and i > (data[data.index(i) + 1])]
    result = []
    for i in range(1, (len(data)-1)):
        num = data[i]
        # print(i)
        # y
        print(num)
        if num > data[i-1] and num > data[i+1]:
            result.append(i)
    return result


def valleys():  # returns indices of valleys
    pass


def peaksnvalleys():  # compile list of peaks and valleys in order
    peaks


def main():  # do the stuff
    print(peaks(data))

    # ----------------------------------------------------------------


if __name__ == '__main__':

    run = 1
    while run:

        # --------------------------------------------------------

        main()

# ----------------------------------------------------------------

        ask = input('Quit? Y/N > ').strip().lower()
        if ask == 'y':
            run = 0
