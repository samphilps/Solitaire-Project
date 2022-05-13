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
        self._general_size = 30
        self.width = int(self._general_size * 2.25)
        self.height = int(self._general_size * 3.5)
        self.generic_card = Card(('a', 'spades'))

    def draw_stock(self):
        pass

    def draw_foundation(self):
        self.stack = []
        for a in range(4):
            stack = py.draw.rect(Screen.screen, (48, 122, 72), [self.x, self.y, self.width, self.height])
            self.x += (40 + self.width)
            self.stack.append(stack)
            self.foundation.append(self.stack)
            self.stack = []
        
    def draw_tableau(self):
        range_num = 7
        index_num = 0
        seperator = 20
        disgusting_equation = ((self.generic_card.width + seperator) * 7) - seperator
        x_loc = (Screen().SCREENWIDTH - disgusting_equation)/2
        y_loc = 200
        print(y_loc)
        mult = 1
        
        
        for i in range(7):
            
            for j in range(range_num):
                card_id = Deck().deck[0][j + index_num].value
                card = Card(card_id, x_axis=x_loc, y_axis=y_loc)
                print(card.value)
                if j == 0:
                    card.face_up = True
                    
                card.show()
                distance = card.width + seperator
                x_loc += distance
            
            index_num += range_num
            range_num -= 1
            x_loc = ((Screen().SCREENWIDTH - disgusting_equation)/2) + (distance * mult)
            y_loc += 20
            mult += 1

    def draw_waste(self):
        pass
    
t = Table()

t.draw_tableau()
