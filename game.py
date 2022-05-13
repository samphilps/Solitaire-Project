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
        Screen.screen.fill(Screen.SCREENCOLOR)
        t.draw_foundation()
        t.draw_tableau()
        t.draw_stock()

        d.deck.pop(0)
        d.deck.append(t.foundation)
        d.deck.append(t.tableau)
        d.deck.append(t.stock)
        d.deck.append(t.waste)
        
        #t.draw_waste(t.stock)
        
        # GAME LOOP -------------------------------------------
        while True:
            mouse_presses = pygame.mouse.get_pos()
            mouse_x = mouse_presses[0]
            mouse_y = mouse_presses[1]
            
            m.set_curr(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type in func_dict:
                    func_dict[event.type]()
            
            if click_num == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    t.check_card_click(mouse_x, mouse_y, d.deck)
                    click_num = 1

            if event.type == pygame.MOUSEBUTTONUP:
                click_num = 0

            # for stack in range(len(d.deck)):
            #     for c in range(len(d.deck[stack])):
            #         pass
            #         #d.deck[stack][c].show()
            
            pygame.display.flip()
            Screen.clock.tick(Screen.FPS)
            m.set_prev(m.curr)