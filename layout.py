import pygame as py
from components import Screen
from card import Card, Deck

class Table():
    def __init__(self):
        self.waste = []
        self.tableau = []
        self.foundation = []
        self.stock = []
        self.x = 50
        self.y = 50
        self._general_size = 16
        self.width = int(self._general_size * 2.25)
        self.height = int(self._general_size * 3.5)

    def draw_stock(self):
        pass

    def draw_foundation(self):
        self.stack = []
        for a in range(4):
            stack = py.draw.rect(Screen.screen, (48, 122, 72), [self.x, self.y, self.width, self.height])
            self.x += (20 + self.width)
            self.stack.append(stack)
            self.foundation.append(self.stack)
            self.stack = []
        print(self.foundation)
        
    def draw_tableau(self):
        pass

    def draw_waste(self):
        pass