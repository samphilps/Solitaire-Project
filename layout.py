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
        self.stock_coord = (883, 50)
        self._general_size = 30
        self.width = int(self._general_size * 2.25)
        self.height = int(self._general_size * 3.5)
        self.generic_card = Card('spades', 'a')
        self.stack_dict = {"foundation": 0, "tableau": 1, "stock": 2, "waste":  3}
        
    def draw_screen(self, deck, foundation, tableau, stock, waste):
        self.draw_foundation()
        self.draw_tableau()
        self.draw_stock()

        deck.pop(0)
        deck.append(foundation)
        deck.append(tableau)
        deck.append(stock)
        deck.append(waste)

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
                card.set_z(self.tableau.index(card))
            
            index_num += range_num
            range_num -= 1
            x_loc = ((Screen().SCREENWIDTH - disgusting_equation)/2) + (distance * mult)
            y_loc += 20
            mult += 1

    def draw_stock(self):
        cards_left = 23
        for a in range(24):
            index = (cards_left + 28)
            suit = Deck().deck[0][index].suit
            num = Deck().deck[0][index].number
            y_loc = self.y
            x_loc = Screen().SCREENWIDTH - (y_loc + self.generic_card.width)
            card = Card(suit, num, x_axis=x_loc, y_axis=y_loc)
            self.stock.insert(0, card)
            card.set_z(cards_left)
            cards_left -= 1

        card.show()
    
    
    def draw_waste(self, stock_list, waste_list):
        subtract_number = 200
        if len(stock_list) >= 3:
            range_num = 3
        else:
            range_num = len(stock_list)
        for a in range(range_num):
            x_loc = Screen().SCREENWIDTH - 60
            card = stock_list[0]
            card.face_up = True
            card.y = 50
            card.x = x_loc - subtract_number
            card.show()
            stock_list.remove(card)
            waste_list.insert(0, card)
            subtract_number -= 30
        
    def click_box(self, mouse_x, mouse_y, card_width, card_height, card_x, card_y):
        if (mouse_x >= card_x) and (mouse_x <= card_x + card_width):
            if (mouse_y >= card_y) and (mouse_y <= card_y + card_height):
                return True

    def reset_stock(self, stock_list, waste_list):
        range_num = len(waste_list)
        for a in range(range_num):
            current_card = waste_list[0]
            current_card.x = self.stock_coord[0]
            current_card.y = self.stock_coord[1]
            current_card.face_up = False
            stock_list.insert(0, current_card)
            waste_list.remove(current_card)
            
        self.draw_stock
        
    # def hit_box(self, mouse_x, mouse_y):
    #     if (mouse_x >= self.stock_coord[0]) and (mouse_x <= self.stock_coord[0] + self.generic_card.width):
    #         if (mouse_y >= self.stock_coord[1]) and (mouse_y <= self.stock_coord[1] + self.generic_card.width):
    #             return True

t = Table()
