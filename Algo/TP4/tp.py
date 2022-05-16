#! /usr/bin env python3.10
#coding: utf-8

from typing import Callable, Any
from functools import wraps

def copylist(fn: Callable) -> Callable: # Too lazy to rewrite
    @wraps(fn)
    def wrapper(array: list) -> list:
        array = array.copy() # 
        fn(array)
        return array
    return wrapper

def __sort_insert_bubble(array: list) -> None:
    for i in range(1, len(array)):
        while array[i-1] > array[i] and i > 0:
            array[i], array[i-1] = array[i-1], array[i] # invert value
            i -= 1

def sort_insert(array: list) -> None: # 2nd version from wiki pseudocode
    for i in range(1, len(array)):
        v = array[i]
        i -= 1
        while v < array[i] and i >= 0:
            array[i+1] = array[i] # shift value
            i -= 1
        array[i+1] = v

def sort_select(array: list) -> None:
    for i in range(len(array)-1):
        j = i
        for k in range(i, len(array)): # find the minimum by index
            if array[j] > array[k]:
                j = k
        array[i], array[j] = array[j], array[i] # invert value
        
def sort_bubble(array: list) -> None:
    for i in range(len(array), 1, -1):
        for j in range(i-1):
            if array[j+1] < array[j]:
                array[j+1], array[j] = array[j], array[j+1] # invert value

def nbefore(array:list, n : int) -> list:
    i = 0
    while array[i] < n:
        i += 1
    return array[:n]

def most(array: list) -> Any:
    sort_insert(array)
    i = 1
    j = 0
    mfind = 0
    while i < len(array):
        find = 0
        while array[i-1] < array[i]:
            find += 1
            i += 1
        if mfind < find:
            mfind = find
            j = i
        i += 1
    return array[j]

def check_sort(array: list) -> bool:
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            return False
    return True

print(most([0, 0, 2, 2 ,2,3, 3, 4]))

if __name__ == "__main_d_":

    from random import randint
    
    bench = [
        sort_insert,
        sort_select,
        sort_bubble
        ]

    for fn in bench:
        fn = copylist(fn)
        array = [randint(0, 100) for _ in range(25)]
        print(array)
        array = fn(array)
        print(array)
        print(nbefore(array, 5))
        assert check_sort(array)