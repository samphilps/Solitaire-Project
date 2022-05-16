from email import generator
import pygame
from components import *
from card import *
from layout import *

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Cards")
    
    def _quit_game(self):
        pygame.quit()
        return None
    

    def run(self):
        click_num = 0
        
        m = MouseCard()
        d = Deck()
        t = Table()
        d.fiftytwo_pickup()

        for i in range(len(d.deck)):
            for card in range(i):
                m.add_sub(d.deck[i][card])

        func_dict = {
            pygame.MOUSEBUTTONUP: m.notify_up,
            pygame.MOUSEBUTTONDOWN: m.notify_down,
            pygame.QUIT : self._quit_game
        }
        
        
        # GAME LOOP -------------------------------------------
        
        t.draw_screen(d.deck, t.foundation, t.tableau, t.stock, t.waste)

        while True:
            Screen.screen.fill(Screen.SCREENCOLOR)

            t.draw_foundation()
            t.draw_tableau()
            t.draw_stock(t.stock)
            #t.draw_waste(t.stock, t.waste)
            
            mouse_presses = pygame.mouse.get_pos()
            mouse_x = mouse_presses[0]
            mouse_y = mouse_presses[1]
            
            for event in pygame.event.get():
                if event.type in func_dict:
                    func_dict[event.type]()
            
            if click_num != 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for a in range(len(d.deck)):
                        for b in range(len(d.deck[a])):
                            card = d.deck[a][b]
                            if type(card) == Card:
                                if t.click_box(mouse_x, mouse_y, card.width, card.height, card.x, card.y):
                                    if card in t.stock:
                                        t.draw_waste(t.stock, t.waste)
                                    if len(t.stock) == 0:
                                        t.reset_stock(t.stock, t.waste)
                                    click_num = 1
                                    break

            if event.type == pygame.MOUSEBUTTONUP:
                click_num = 0
                
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         t.draw_screen(d.deck, t.foundation, t.tableau, t.stock, t.waste)
            #         t.reset_stock(t.stock, t.waste)

            # for stack in range(len(d.deck)):
            #     for c in range(len(d.deck[stack])):
            #         pass
            #         #d.deck[stack][c].show()
            
            pygame.display.flip()
            Screen.clock.tick(Screen.FPS)
            m.set_prev(m.curr)