#!/bin/python3

'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.
Every function in this file takes a comparator `cmp` as input

If cmp(a, b) returns -1, then a < b;
if cmp(a, b) returns  1, then a > b;
if cmp(a, b) returns  0, then a == b.

'''


def cmp_standard(a, b):

    '''
    used for sorting from lowest to highest
    >>> cmp_standard(125, 322)
    -1
    >>> cmp_standard(523, 322)
    1
    '''

    if a < b:
        return -1
    if b < a:
        return 1
    return 0


def cmp_reverse(a, b):

    '''
    used for sorting from highest to lowest
    >>> cmp_reverse(125, 322)
    1
    >>> cmp_reverse(523, 322)
    -1
    '''

    if a < b:
        return 1
    if b < a:
        return -1
    return 0


def cmp_last_digit(a, b):

    '''
    used for sorting based on the last digit only
    >>> cmp_last_digit(125, 322)
    1
    >>> cmp_last_digit(523, 322)
    1
    '''
    return cmp_standard(a % 10, b % 10)


def _merged(xs, ys, cmp=cmp_standard):

    '''
    >>> _merged([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    '''

    x = 0
    y = 0
    ret = []
    while x < len(xs) and y < len(ys):
        if cmp(xs[x], ys[y]) == -1:
            ret.append(xs[x])
            x += 1
        else:
            ret.append(ys[y])
            y += 1
    while x < len(xs):
        ret.append(xs[x])
        x += 1
    while y < len(ys):
        ret.append(ys[y])
        y += 1
    return ret


def merge_sorted(xs, cmp=cmp_standard):

    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves
    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''
    div = len(xs)//2
    left = []
    right = []

    if len(xs) <= 1:
        return xs
    else:
        left = xs[div:]
        right = xs[:div]
        lsort = merge_sorted(left, cmp=cmp)
        rsort = merge_sorted(right, cmp=cmp)
        return _merged(rsort, lsort, cmp=cmp)


def quick_sorted(xs, cmp=cmp_standard):

    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected,
    and the list is split into a "less than
    " sublist and a "greater than" sublist.
    The pseudocode is:
        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            put all the values equal to p in a list
            sort the greater/less than lists recursively
            return the concatenation of (less than, equal, greater than)

    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''

    if len(xs) <= 1:
        return xs
    else:
        split = len(xs)//2
        p = xs[(split)]
        lessp = [i for i in xs if cmp(i, p) == -1]
        greatp = [i for i in xs if cmp(i, p) == 1]
        equalp = [i for i in xs if cmp(i, p) == 0]
        lpsort = quick_sorted(lessp, cmp=cmp)
        gpsort = quick_sorted(greatp, cmp=cmp)
        return lpsort + equalp + gpsort


def quick_sort(xs, cmp=cmp_standard):

    '''
    EXTRA CREDIT:
    '''
