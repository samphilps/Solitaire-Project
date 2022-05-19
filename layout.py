import pygame as py
from components import Screen
import random
from card import Card

class Table():
    def __init__(self):
        self.waste = []
        self.tableau = [[],[],[],[],[],[],[]]
        self.foundation = [[],[],[],[]]
        self.stock = []
        self.cards_selected = []
        self.num_dict = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K': 13}
        self.x_dict = {0:205.5, 1:292.5, 2:379.5, 3:466.5, 4:553.5, 5:640.5, 6:727.5}
        self.tableau_dict = {205.5:0, 292.5:1, 379.5:2, 466.5:3, 553.5:4, 640.5:5, 727.5:6}
        self.found_x = 50
        self.y = 50
        self.stock_coords = (883, 50)
        self._general_size = 30
        self.width = int(self._general_size * 2.25)
        self.height = int(self._general_size * 3.5)
        self.card_list = {"stock" : self.stock, "tableau" : self.tableau, "waste" : self.waste}
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
        
    def draw_foundation(self):
        self.found_x = 50
        for a in range(len(self.foundation)):
            if len(self.foundation[a]) == 0:
                py.draw.rect(Screen.screen, (48, 122, 72), [self.found_x, self.y, self.width, self.height])
                self.found_x += (40 + self.width)

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
                print(x_loc)
                if j == 0:
                    card.face_up = True
                distance = card.width + seperator
                x_loc += distance
                self.tableau[j - range_num].append(card)
                card.set_z(self.tableau[j - range_num].index(card))
                
                card.list_pos = "tableau"
                
            
            index_num += range_num
            range_num -= 1
            x_loc = ((Screen().SCREENWIDTH - disgusting_equation)/2) + (distance * mult)
            y_loc += 20
            mult += 1

    def draw_tableau(self):
        for a in range(len(self.tableau)):
            if len(self.tableau[a]) == 0:
                y_val = 200
                py.draw.rect(Screen.screen, (48, 122, 72), [self.x_dict[a], y_val, self.width, self.height])
            else:
                for b in range(len(self.tableau[a])):
                    card = self.tableau[a][b]
                    card.show()

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
            card.list_pos = "stock"
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
            card = stock_list[0]
            waste_list.append(card)
            stock_list.remove(card)
            card.list_pos = "waste"
            
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
        
            
        
    def click_box(self, mouse_x, mouse_y, width, height, object_x, object_y):
        if (mouse_x >= object_x) and (mouse_x <= object_x + width):
            if (mouse_y >= object_y) and (mouse_y <= object_y + height):
                return True

    def reset_stock(self, stock_list, waste_list):
        range_num = len(waste_list)
        for a in range(range_num):
            current_card = waste_list[0]
            current_card.x = self.stock_coords[0]
            current_card.face_up = False
            stock_list.append(current_card)
            waste_list.remove(current_card)
            current_card.list_pos = "stock"
            
        
    def stock_check(self, mouse_x, mouse_y):
        return self.click_box(mouse_x, mouse_y, self.generic_card.width, self.generic_card.height, self.stock_coords[0], self.stock_coords[1])
    
    def move_card(self):
        card1 = self.cards_selected[0]
        card2 = self.cards_selected[1]
        print(f"\nCard 1 : '{card1.value}' Card 2 : '{card2.value}'\n")
        
        #-------------------------------

        # Tablaeu check
        if card2.list_pos == "tableau":
            card2_list = self.card_list[card2.list_pos][self.tableau_dict[card2.x]]
            if card1._base_color != card2._base_color:
  
                if self.num_dict[card1.number] == self.num_dict[card2.number] - 1:
                    if card1.list_pos == "tableau":
                        card1_list = self.card_list[card1.list_pos][self.tableau_dict[card1.x]]
                    else:
                         card1_list = self.card_list[card1.list_pos]
                    
                    
                    card1_list.remove(card1)
                    if len(card1_list) > 0:
                        card1_list[-1].face_up = True
                    card2_list.append(card1)
                    card1.list_pos = str(card2.list_pos)
                    card1.x = float(card2.x)
                    card1.y = card2.y + 20
                    card1.z = card2_list.index(card1)

        #-------------------------------
        card1.selected = False
        card1._accent_color = card1._base_color
        card2.selected = False
        card2._accent_color = card2._base_color

        self.cards_selected.clear()

    def card_check(self, mouse_x, mouse_y, card_stack):
        range_num = len(card_stack)
        for a in range(len(card_stack)):
            if type(card_stack[a]) == list:
                range_num = len(card_stack[a])
                if range_num > 0:
                    for b in range(range_num):
                        card = card_stack[a][range_num - 1]
                        if self.click_box(mouse_x, mouse_y, card.width, card.height, card.x, card.y):
                            
                            #-----------------------------
                            
                            if card.selected != True:
                                card.selected = True
                                card._accent_color = card._highlight_color
                                self.cards_selected.append(card)

                            if len(self.cards_selected) == 2:
                                self.move_card()
                                

                            return True
                            #-----------------------------

                        range_num -= 1

            elif type(card_stack[a]) == Card:
                if card_stack == self.waste:
                    card = card_stack[-1]
                    if self.click_box(mouse_x, mouse_y, card.width, card.height, card.x, card.y):
                        #--------------------------
                        card.selected = True
                        self.cards_selected.append(card)
                        card._accent_color = card._highlight_color

                        if len(self.cards_selected) == 2:
                            self.move_card()
                        return True
                        #--------------------------
                    range_num -= 1
                else:
                    return False

        

t = Table()
