#!/bin/env python3.8
# coding: utf-8

from array import array
from random import random, choice

STATES = (0, 1, 2)


class CellMatrix(list):
    
    def __init__(self, n: int, r: int) -> array:
        self.range_n: list = range(n)
        self.range_r: list = range(r)
        super().__init__([STATES[0] for _ in self.range_n] for _ in self.range_r)
    
    def print(self) -> None:
        for i in self.range_r:
            for j in self.range_n:
                print(f" {self[i][j]}", end='')
            print()
            
    def set(self, cells: list):
        for i, j, state in cells:
            self[i][j] = state
            
    def randomise(self, min: int, max: int, states: list = STATES):
        for _ in range(int(random() * max + min)):
            choice(self)[choice(self.range_r)] = choice(states)
            
    def getNextTo(self, i: int, j: int):
        neighbors = [
                (i-1, j-1), (i-1, j), (i-1, j+1),
                (i, j-1), (i, j+1),
                (i+1, j-1), (i+1, j), (i+1, j+1),
            ]
        for i_, (i, j) in enumerate(neighbors):
            if i < 1 or i > self.range_n[-1]
        ...
    
        
c = CellMatrix(4, 4)
c.randomise(2, 5)
c.print()