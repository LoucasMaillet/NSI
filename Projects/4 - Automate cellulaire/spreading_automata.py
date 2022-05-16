#!/usr/bin/env python3.8
#coding: utf-8


from tkinter import Event, Frame, Canvas, Tk
from random import sample
from typing import Generator


class Cell(int):

    def __init__(self, _, rgb) -> None:
        self.hex_color = "#%02x%02x%02x" % rgb
        self.rgb_color = "%02d;%02d;%02d" % rgb

    def __new__(cls, v, *_) -> None:
        return super(Cell, cls).__new__(cls, v)


# Next element base of each cell
NEXTS = (
    (1, -1), (1, 0), (1, 1),
    (0, -1), (0, 1),
    (-1, -1), (-1, 0), (-1, 1)
)
# Delay between each update (in ms)
UPD_TIME = 1
# Percent of initialised uninfected cells
DENSITY = .5
# Different types of cells
CL_BLANK = Cell(0x0, (255, 255, 240))
CL_UNINFECTED = Cell(0x1, (50, 205, 50))
CL_SPREAD = Cell(0x2, (255, 5, 5))
CL_INFECTED = Cell(0x3, (191, 191, 191))


class AutoCell(list):

    def __init__(self, r: int, n: int) -> None:
        list.__init__(self, ([CL_BLANK for j in range(n+2)]
                      for i in range(r+2)))
        self.c_spread = 0
        self.c_uninfected = int(DENSITY*n*r)
        self.c_infected = 0
        self._r = r + 1
        self._n = n + 1
        self._queue = []
        for i, j in sample([(i, j) for j in range(1, self._n) for i in range(1, self._r)], self.c_uninfected):
            self[i][j] = CL_UNINFECTED

    def __str__(self) -> str:
        repr_ = ""
        i = 1
        while i < self._r:
            repr_ += '['
            j = 1
            while j < self._n:
                repr_ += f"{self[i][j]}, "
                j += 1
            repr_ += f"{self[i][j]}],\n"
            i += 1
        repr_ += '['
        j = 1
        while j < self._n:
            repr_ += f"{self[i][j]}, "
            j += 1
        repr_ += f"{self[i][j]}]"
        return repr_

    def spread(self, i: int, j: int) -> bool:
        i += self._r if i < 0 else 1
        j += self._n if j < 0 else 1
        if self[i][j] == CL_UNINFECTED:
            self.c_uninfected -= 1
            self.c_spread += 1
            self._queue.append((i, j))
            self[i][j] = CL_SPREAD

    def update(self) -> bool:
        queue = []
        for i, j in self._queue:
            self[i][j] = CL_INFECTED
            self.c_infected += 1
            self.c_spread -= 1
            for i_n, j_n in NEXTS:
                n = (i + i_n, j + j_n)
                if self[n[0]][n[1]] == CL_UNINFECTED:
                    queue.append(n)

        self._queue = []
        for n in queue:
            if self[n[0]][n[1]] == CL_UNINFECTED:
                self[n[0]][n[1]] = CL_SPREAD
                self.c_uninfected -= 1
                self.c_spread += 1
                self._queue.append(n)


class AutoCellCanvas(AutoCell, Canvas):

    def __init__(self, frame: Frame, width: int, height: int, r: int, n: int, upd_time: int = UPD_TIME, **kwargs) -> None:
        AutoCell.__init__(self, r, n)
        Canvas.__init__(self, frame, width=width, height=height, **kwargs)
        self.c_height = height / r
        self.c_width = width / n
        self.upd_time = upd_time

        def __listener_button_1__(ev: Event):
            i, j = int(ev.y // self.c_height), int(ev.x // self.c_width)
            self.spread(i, j)

        self.bind("<Button-1>", __listener_button_1__)

        def __update_loop__():
            self.update()
            self._id = self.after(self.upd_time, __update_loop__)

        self._id = self.after(self.upd_time, __update_loop__)

        self.draw()
        self.pack()

    def draw(self):
        i = 1
        while i < self._r:
            j = 1
            while j < self._n:
                x, y = (j-1) * self.c_width, (i-1) * self.c_height
                self.create_rectangle(x, y, x + self.c_width, y +
                                      self.c_height, fill=self[i][j].hex_color, width=0)
                j += 1
            i += 1

    def __nexts__(self) -> Generator:
        for i, j in self._queue:
            self[i][j] = CL_INFECTED
            self.c_infected += 1
            self.c_spread -= 1
            x, y = (j-1) * self.c_width, (i-1) * self.c_height
            self.create_rectangle(x, y, x + self.c_width, y +
                                self.c_height, fill=self[i][j].hex_color, width=0)
            for i_n, j_n in NEXTS:
                n = (i + i_n, j + j_n)
                if self[n[0]][n[1]] == CL_UNINFECTED:
                    yield n

    def __spread__(self, nexts: list) -> Generator:
        for n in nexts:
            if self[n[0]][n[1]] == CL_UNINFECTED:
                self[n[0]][n[1]] = CL_SPREAD
                self.c_uninfected -= 1
                self.c_spread += 1
                x, y = (n[1]-1) * self.c_width, (n[0]-1) * self.c_height
                self.create_rectangle(x, y, x + self.c_width, y +
                                      self.c_height, fill=self[n[0]][n[1]].hex_color, width=0)
                yield n
                
    def update(self):
        self._queue = [*self.__spread__([*self.__nexts__()])]
        


class AutoCellShell(AutoCell):

    def __init__(self, r: int, n: int) -> None:
        AutoCell.__init__(self, r, n)

    def draw(self) -> None:
        print("\033c", end='')
        i = 1
        while i < self._r:
            j = 1
            while j < self._n:
                print(f"\033[48;2;{self[i][j].rgb_color}m   \033[0m", end='')
                j += 1
            print()
            i += 1

    def update(self):
        queue = []
        for i, j in self._queue:
            self[i][j] = CL_INFECTED
            self.c_infected += 1
            self.c_spread -= 1
            print(
                f"\033[?25l\033[{i};{j*2-1}f\033[48;2;{self[i][j].rgb_color}m   \033[0m")
            for i_n, j_n in NEXTS:
                n = (i + i_n, j + j_n)
                if self[n[0]][n[1]] == CL_UNINFECTED:
                    queue.append(n)

        self._queue = []
        for n in queue:
            if self[n[0]][n[1]] == CL_UNINFECTED:
                self[n[0]][n[1]] = CL_SPREAD
                self.c_uninfected -= 1
                self.c_spread += 1
                self._queue.append(n)
                print(
                    f"\033[?25l\033[{n[0]};{n[1]*2-1}f\033[48;2;{self[n[0]][n[1]].rgb_color}m   \033[0m")
        print("\033[u", end='')


if __name__ == "__main__":

    # 252 2582 2453 358 3813 1154 3010 1304 3481 3669 2665
    # from keyboard import on_press_key, wait
    # from time import sleep
    # from os import get_terminal_size
    # from time import sleep
    # n, r = get_terminal_size()
    # fm = AutoCellShell(r-1, n//3)
    # fm.draw()
    # fm.spread(0, 0)
    # cursor = [0, 0]

    # def __key_event__(key):
    #     print(key)
    #     # if key == Key.up:
    #     #     if cursor[0] < fm._r:
    #     #         cursor[0] += 1
    #     #         print("\033[s", end='')
    #     # elif key == Key.down:
    #     #     if 0 < cursor[0]:
    #     #         cursor[0] -= 1
    #     #         print("\033[s", end='')
    #     # elif key == Key.left:
    #     #     ...
    #     # elif key == Key.right:
    #     #     ...
    # on_press_key("up arrow", __key_event__)
    # UPD_TIME *= 1e-3
    # while True:
    #     fm.update()
    #     # fm.draw()
    #     sleep(UPD_TIME)
    
    fm = AutoCellShell(5, 10)
    fm.draw()    
    
    exit()

    gui = Tk()
    gui.title(f"Spreading Cellular Automata")
    frame = Frame()
    frame.pack()
    f = 10
    fm = AutoCellCanvas(frame,
                        1920/2,
                        1080/2,
                        9*f,
                        16*f)
    fm.mainloop()
