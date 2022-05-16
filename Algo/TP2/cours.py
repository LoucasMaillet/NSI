#!/bin/env python3.8
# coding: utf-8


def give(value: int, sys : tuple) -> tuple:
    """Give a sum of money using a monetary system.

    Return efficiently the total sum in piece of a monetary system.

    Args:
        value (int): The total sum
        sys (tuple): The monetary system (sorted in descending order)

    Returns:
        tuple: The sum converted
    """
    given = []
    m = 0
    for v in sys:
        if value <= 0: break
        elif v > value: continue
        given.append((value // v,  v))
        value -= v * given[-1][0]
        m += given[-1][0]
    return given, m
    

def often_used(value : int, sys : tuple) -> tuple:
    """Get the maximum piece used before a maximal total sum.

    Args:
        value (int): The maximal total sum
        sys (tuple): The monetary system (sorted in descending order)

    Returns:
        tuple: Total sum(s) with the maximal number of piece used
    """
    top_sum = [None]
    multiple_sum = False
    top_m = 0
    for i in range(value):
        m = give(i , sys)[1]
        if m > top_m:
            top_sum = [i]
            top_m = m
            multiple_sum = False
        elif m == top_m:
            top_sum.append(i)
            multiple_sum = True
    return top_sum if multiple_sum else top_sum[0], top_m
    

def most_activity(activity: list) -> list:
    """Sort a list of activitie's schedule to approximately satisfied most activities.

    Args:
        activity (list[tuple]): List of activie's schedule in the form of [(starting_hour, stoping_hour), ...]

    Returns:
        list: The brand new planning
    """
    activity.sort(key=lambda item: item[1])
    lenght = len(activity) - 1
    i = 0
    while i < lenght :
        if activity[i][1] > activity[i + 1][0]: # if intersect
            activity.pop(i+1)
            lenght-=1
        else: 
            i += 1
    return activity

if __name__ == "__main__":

	value = 33
	sys = (500, 200, 100, 50, 20, 10, 5, 2, 1)

	print(give(value, sys))

	print(often_used(200, sys))

	# arr = [(8, 13), (12, 17), (9, 11), (14, 16), (11, 12)]
	arr = [(1,4), (0,6), (3,5), (12,13), (8,11), (8,12), (2,13), (6,10), (5,9), (3,8), (5,7), (13,16), (15,17), (16,19)]
	print(most_activity(arr))