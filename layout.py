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
        self.generic_card = Card('spades', 'a')
        self.stack_dict = {"foundation": 0, "tableau": 1, "stock": 2, "waste":  3}

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
        mult = 1
        
        for i in range(7):
            
            for j in range(range_num):
                card_id = Deck().deck[0][j + index_num]
                card = Card(card_id.suit, card_id.number, x_axis=x_loc, y_axis=y_loc)
                if j == 0:
                    card.face_up = True
                card.show()
                distance = card.width + seperator
                x_loc += distance
                self.tableau.append(card)
            
            index_num += range_num
            range_num -= 1
            x_loc = ((Screen().SCREENWIDTH - disgusting_equation)/2) + (distance * mult)
            y_loc += 20
            mult += 1

    def draw_stock(self):
        cards_left = 23
        for a in range(24):
            index = (cards_left + 28)
            self.stock.insert(0, (Deck().deck[0][index]))
            suit = Deck().deck[0][index].suit
            num = Deck().deck[0][index].number
            y_loc = self.y
            x_loc = Screen().SCREENWIDTH - (y_loc + self.generic_card.width)
            card = Card(suit, num, x_axis=x_loc, y_axis=y_loc)
            card.show()
            cards_left -= 1

    def draw_waste(self, stock_list):
        subtract_number = 200
        for a in range(3):
            x_loc = Screen().SCREENWIDTH - 50
            card = stock_list[a]
            card.face_up = True
            card.y = 50
            card.x = x_loc - subtract_number
            card.show()
            subtract_number -= 25
    
    def click_box(self, mouse_x, mouse_y, card_width, card_height, card_x, card_y):
        if (mouse_x <= card_width) and (mouse_x >= card_x):
            if (mouse_y <= card_width) and (mouse_y >= card_height):
                return True

    def check_card_click(self, x, y, stack_list):
        for a in range(len(stack_list)):
            for b in range(len(stack_list[a])):
                card = stack_list[a][b]
                print(card.x)
                # if self.click_box(x, y, card.width, card.height, card.x_axis, card.y_axis):
                #     print(card.suit)

t = Table()


