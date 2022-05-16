#!/usr/bin/env python3.8
#coding: utf-8


from time import sleep
from tkinter import Event, Frame, Canvas, Label, Tk, StringVar
from random import sample


class Cell(int):

    def __init__(self, _, rgb) -> None:
        self.hex_color = "#%02x%02x%02x" % rgb
        self.rgb_color = "%02d;%02d;%02d" % rgb

    def __new__(cls, v, *_) -> None:
        return super(Cell, cls).__new__(cls, v)


# Delay between each update (in ms)
T_DELAY = 100
# Percent of initialised uninfected cells
DENSITY = .5
# Different types of cells
CL_BLANK = Cell(0x0, (255, 255, 240))
CL_UNINFECTED = Cell(0x1, (50, 205, 50))
CL_SPREAD = Cell(0x2, (255, 5, 5))
CL_INFECTED = Cell(0x3, (191, 191, 191))


class AutoCell(list):

    def __init__(self, r: int, n: int) -> None:
        list.__init__(self, ([CL_BLANK for j in range(n+2)] for i in range(r+2)))
        self.c_spread = 0
        self.c_uninfected = int(DENSITY*n*r)
        self.c_infected = 0
        self._r = r + 1
        self._n = n + 1
        self._spreader = set()
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
            self._spreader.add((i, j))
            self[i][j] = CL_SPREAD

    def update(self) -> bool:
        spreader = set()
        for i, j in self._spreader:
            self[i][j] = CL_INFECTED
            self.c_spread -= 1
            for i, j in ((i-1, j-1), (i-1, j), (i-1, j+1),  # A B C
                         (i, j-1), (i, j+1),                # D _ E
                         (i+1, j-1), (i+1, j), (i+1, j+1)):  # F G H
                if self[i][j] == CL_UNINFECTED:
                    spreader.add((i, j))
        for i, j in spreader:
            self[i][j] = CL_SPREAD
            self.c_infected += 1
            self.c_uninfected -= 1
            self.c_spread += 1
        self._spreader = spreader

    def draw(self) -> None:
        print("\033c", end='')
        i = 1
        while i < self._r:
            j = 1
            while j < self._n:
                print(f"\033[48;2;{self[i][j].rgb_color}m\a   \033[0m", end='')
                j += 1
            print()
            i += 1


class AutoCellCanvas(AutoCell, Canvas):

    def __init__(self, frame: Frame, width: int, height: int, r: int, n: int, upd_time: int = T_DELAY, **kwargs) -> None:
        AutoCell.__init__(self, r, n)
        Canvas.__init__(self, frame, width=width, height=height, **kwargs)
        self.c_height = height / r
        self.c_width = width / n
        self.upd_time = upd_time
                    
        def __listener_button_1__(event: Event):
            i, j = int(event.y // self.c_height), int(event.x // self.c_width)
            self.spread(i,j)
        
        self.bind("<Button-1>", __listener_button_1__)
        
        def __update_loop__():
            self.update()
            self._id = self.after(self.upd_time, __update_loop__)
            
        self._id = self.after(self.upd_time, __update_loop__)
        
        self.draw()
        self.pack()

    def __draw_cell__(self, i: int, j: int):
        x, y = (j-1) * self.c_width, (i-1) * self.c_height
        self.create_rectangle(x, y, x + self.c_width, y +
                              self.c_height, fill=self[i][j].hex_color, width=0)

    def draw(self):
        i = 1
        while i < self._r:
            j = 1
            while j < self._n:
                self.__draw_cell__(i, j)
                j += 1
            i += 1
        
    def update(self):
        spreader = set()
        for i, j in self._spreader:
            self[i][j] = CL_INFECTED
            self.c_spread -= 1
            self.__draw_cell__(i, j)
            for i, j in ((i-1, j-1), (i-1, j), (i-1, j+1),  # A B C
                         (i, j-1), (i, j+1),                # D _ E
                         (i+1, j-1), (i+1, j), (i+1, j+1)):  # F G H
                if self[i][j] == CL_UNINFECTED:
                    spreader.add((i, j))
        for i, j in spreader:
            self[i][j] = CL_SPREAD
            self.c_infected += 1
            self.c_uninfected -= 1
            self.c_spread += 1
            self.__draw_cell__(i, j)
        self._spreader = spreader


if __name__ == "__main__":
    
    # 252 2582 2453 358 3813 1154 3010 1304 3481 3669 2665

    fm = AutoCell(9*6+1, 16*5-1)

    gui = Tk()
    gui.title(f"Spreading Cellular Automata")
    frame = Frame()
    frame.pack()
    fm = AutoCellCanvas(frame,
                        1920/2,
                        1080/2,
                        9*40,
                        16*40)
    gui.mainloop()
    
    # fm.spread(0, 0)
    # fm.draw()
    # while fm.self.c_spread != 0:
    #     fm.update()
    #     fm.draw()
    #     sleep(.1)
