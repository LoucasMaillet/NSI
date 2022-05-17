#!/usr/bin/env python3.10
#coding: utf-8

#    _____            __
#   / ___/____  _____/ /_  ____  __  __
#   \__ \/ __ \/ ___/ __/ / __ \/ / / /
#  ___/ / /_/ / /  / /__ / /_/ / /_/ /
# /____/\____/_/   \__(_) .___/\__, /
#                      /_/    /____/
#
# Just a simple start in depth of sorting algorithms


from typing import Callable, Any
from functools import wraps
from collections import defaultdict


# * Decorator


def copylist(fn: Callable) -> Callable:  # Too lazy to rewrite
    @wraps(fn)
    def wrapper(array: list) -> list:
        array = array.copy()  # Hehe
        fn(array)
        return array
    return wrapper


# * Sorting functions


def sort_insert_bubble(array: list) -> None:  # First version on my own (who wasn't exactly the thing needed)
    for i in range(1, len(array)):
        while array[i-1] > array[i] and i > 0:
            array[i], array[i-1] = array[i-1], array[i]  # Invert value
            i -= 1


def sort_insert(array: list) -> None:  # Second version based on wiki pseudocode
    for i in range(1, len(array)):
        v = array[i]
        i -= 1
        while v < array[i] and i >= 0:
            array[i+1] = array[i]  # Shift value
            i -= 1
        array[i+1] = v


def sort_select(array: list) -> None:
    for i in range(len(array)-1):
        j = i
        for k in range(i, len(array)):  # Find the minimum by index
            if array[j] > array[k]:
                j = k
        array[i], array[j] = array[j], array[i]  # Invert value


def sort_bubble(array: list) -> None:
    for i in range(len(array), 1, -1):
        for j in range(i-1):
            if array[j+1] < array[j]:
                array[j+1], array[j] = array[j], array[j+1]  # Invert value


# * Other functions


def n_before(array: list, n: int) -> list:
    i = 0
    while array[i] < n:
        i += 1
    return array[:i]


def most(array: list) -> Any:
    sort_insert(array)
    i = 1
    j = 0
    mfind = 0
    while i < len(array):
        find = i
        while i < len(array) and array[i-1] == array[i]:
            i += 1
        find = i - find
        if mfind < find:
            mfind = find
            j = i
        i += 1
    return array[j - 1]


def check_sort(array: list) -> bool:
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            return False
    return True


def occurences(array: list) -> tuple[Any, int]:
    hashmap = defaultdict(int)  # Optimized
    for k in array:
        hashmap[k] += 1
    return list(hashmap.items())  # Much less optimized


# * Main


if __name__ == "__main__":

    from random import randint

    array = [randint(0, 100) for _ in range(25)]

    print(most(array))
    print(occurences(array))

    bench = [
        sort_insert,
        sort_select,
        sort_bubble
    ]

    for fn in bench:
        fn = copylist(fn)  # Better use a decorator (more pythonic)
        print(array)
        array = fn(array)
        print(array)
        print(n_before(array, 20))
        assert check_sort(array)
