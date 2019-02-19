# Practice 03-Lists10.py

#  Write a function that merges two lists into a single list, where each
#  element of the output list is a list containing two elements, one from each
#  of the input lists.
#  merge([5,2,1], [6,8,2]) → [[5,6],[2,8],[1,2]]


def merge_lists(lista, listb):
    return ([list(i) for i in zip(lista, listb)])


lista = [5, 2, 1]
listb = [6, 8, 2]

print(merge_lists(lista, listb))
