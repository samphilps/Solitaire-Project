from email import generator
import pygame
from components import Screen
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
        while True:
            
            m.set_curr(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type in func_dict:
                    func_dict[event.type]()
            
            for stack in range(len(d.deck)):
                for c in range(len(d.deck[stack])):
                    pass
                    #d.deck[stack][c].show()

            
            pygame.display.flip()
            Screen.clock.tick(Screen.FPS)
            m.set_prev(m.curr)
