from ssl import PEM_cert_to_DER_cert
import pygame as py
from components import Screen
import random
from card import Card, Deck

class Table():
    def __init__(self):
        self.waste = []
        self.tableau = [[],[],[],[],[],[],[]]
        self.foundation = [[],[],[],[]]
        self.stock = []
        self.x = 50
        self.y = 50
        self.stock_coord = (883, 50)
        self._general_size = 30
        self.width = int(self._general_size * 2.25)
        self.height = int(self._general_size * 3.5)
        self.generic_card = Card('spades', 'a')
        self.stack_dict = {"foundation": 0, "tableau": 1, "stock": 2, "waste":  3}
        self.reset_text = self.generic_card._suit_font.render("⟳",True,(0,0,0))
        self.reset_textrect = self.reset_text.get_rect()
        self.reset_textrect.center = ((883 + self.generic_card.width/2), 50 + self.generic_card.height/2)
        
    def draw_screen(self, deck, foundation, tableau, stock, waste):
        random.shuffle(deck[0])
        self.create_tableau(deck)
        self.create_stock(deck)

        deck.pop(0)
        deck.append(foundation)
        deck.append(tableau)
        deck.append(stock)
        deck.append(waste)

    # def create_foundation(self):
    #     self.stack = []
    #     for a in range(4):
    #         stack = py.draw.rect(Screen.screen, (48, 122, 72), [self.x, self.y, self.width, self.height])
    #         self.stack.append(stack)
    #         self.foundation.append(self.stack)
    #         self.stack = []
        
    def draw_foundation(self):
        self.x = 50
        for a in range(len(self.foundation)):
            if len(self.foundation[a]) == 0:
                py.draw.rect(Screen.screen, (48, 122, 72), [self.x, self.y, self.width, self.height])
                self.x += (40 + self.width)

    def create_tableau(self, deck):
        range_num = 7
        index_num = 0
        seperator = 20
        disgusting_equation = ((self.generic_card.width + seperator) * 7) - seperator
        x_loc = (Screen().SCREENWIDTH - disgusting_equation)/2
        y_loc = 200
        mult = 1
        
        for i in range(7):
            
            for j in range(range_num):
                card_id = deck[0][j + index_num]
                card = Card(card_id.suit, card_id.number, x_axis=x_loc, y_axis=y_loc)
                if j == 0:
                    card.face_up = True
                distance = card.width + seperator
                x_loc += distance
                self.tableau[j].append(card)
                card.set_z(self.tableau[j].index(card))
            
            index_num += range_num
            range_num -= 1
            x_loc = ((Screen().SCREENWIDTH - disgusting_equation)/2) + (distance * mult)
            y_loc += 20
            mult += 1

    def draw_tableau(self):
        range_num = len(self.tableau)
        for a in range(range_num):
            for b in range(len(self.tableau[a])):
                self.tableau[a][0].show()

    def create_stock(self, deck):
        cards_left = 23
        

        for a in range(24):
            index = (cards_left + 28)
            suit = deck[0][index].suit
            num = deck[0][index].number
            y_loc = self.y
            x_loc = Screen().SCREENWIDTH - (y_loc + self.generic_card.width)
            card = Card(suit, num, x_axis=x_loc, y_axis=y_loc)
            self.stock.insert(0, card)
            card.set_z(cards_left)
            cards_left -= 1



    def draw_stock(self, stock_list):
        range_num = len(stock_list)
        if range_num == 0:
            Screen.screen.blit(self.reset_text, self.reset_textrect)
            return 0
        for a in range(range_num):
            stock_list[a].show()
        
    def update_waste(self, stock_list, waste_list):
        if len(stock_list) == 0:
            self.reset_stock(stock_list, waste_list)
            return None

        if len(stock_list) >= 3:
            range_num = 3
        else:
            range_num = len(stock_list)

        for a in range(range_num):
            print(f"\n{range_num}\n")
            card = stock_list[0]
            waste_list.append(card)
            stock_list.remove(card)
            
    def display_waste(self, waste_list):
        if len(waste_list) == 0:
            return None

        if len(waste_list) >= 3:
            range_num = 3
        else:
            range_num = len(waste_list)

        subtract_number = 260

        for a in range(range_num):
            card = waste_list[0 - range_num]
            x_loc = Screen().SCREENWIDTH - subtract_number
            card.face_up = True
            card.y = 50
            card.x = x_loc
            card.show()

            subtract_number -= 30
            range_num -= 1
        
            
        
    def click_box(self, mouse_x, mouse_y, card_width, card_height, card_x, card_y):
        if (mouse_x >= card_x) and (mouse_x <= card_x + card_width):
            if (mouse_y >= card_y) and (mouse_y <= card_y + card_height):
                return True

    def reset_stock(self, stock_list, waste_list):
        range_num = len(waste_list)
        for a in range(range_num):
            current_card = waste_list[0]
            current_card.x = self.stock_coord[0]
            current_card.face_up = False
            stock_list.append(current_card)
            waste_list.remove(current_card)
            
        
    def stock_check(self, mouse_x, mouse_y):
        if (mouse_x >= self.stock_coord[0]) and (mouse_x <= self.stock_coord[0] + self.generic_card.width):
            if (mouse_y >= self.stock_coord[1]) and (mouse_y <= self.stock_coord[1] + self.generic_card.height):
                return True

t = Table()
