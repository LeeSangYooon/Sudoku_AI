import pygame
from board.vector2 import vector2
from board.board import board
from gui.color import color





class gui:
    def __init__(self):
        pass

    def gui_init(self):
        pygame.init()

        self.board = board(vector2(1,1))
        self.size = [2000, 1500]
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        
        pygame.display.set_caption("Sudoku AI")
        self.done = False
        self.clock = pygame.time.Clock()

        self.pixel_size = 70

        self.space = 50

        self.font = pygame.font.Font('resource/font/arial.ttf', 30)

        self.selected = vector2(-1,-1)


    def renderText(self, text, pos, color):
        text = self.font.render(text, True, color)
        pos[1] -= 10
        self.screen.blit(text, pos)


    def draw(self):
        self.screen.fill(color.background_color)
        pygame.draw.rect(self.screen, color.WHITE, [self.space, self.space, self.pixel_size * self.board.size.x,
                                                   self.pixel_size * self.board.size.y])
        pygame.draw.rect(self.screen, color.GRAY, [self.space, self.space, self.pixel_size * self.board.size.x,
                                                   self.pixel_size * self.board.size.y], 5)

        for n in range(self.board.size.x):
            w = 5 if n%3==0 else 3
            pygame.draw.line(self.screen, color.GRAY, [self.space + n*self.pixel_size, self.space],[self.space + n*self.pixel_size, self.space + self.pixel_size * self.board.size.y], w)
        for n in range(self.board.size.y):
            w = 5 if n % 3 == 0 else 3
            pygame.draw.line(self.screen, color.GRAY, [self.space, self.space + n*self.pixel_size],[self.space + self.pixel_size * self.board.size.x, self.space + n*self.pixel_size], w)

        space = self.space + self.pixel_size * 0.41
        for y in range(self.board.size.y):
            for x in range(self.board.size.x):
                c = color.BLUE if self.selected.x == x and self.selected.y == y else color.GRAY
                self.renderText(str(self.board.board[y][x]), [space + self.pixel_size*x, space + self.pixel_size*y], c)

        pygame.display.flip()

    def main_loop(self):
        self.clock.tick(30)

        mouse_pos = vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        mouse_down = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        keys = pygame.key.get_pressed()
        to = -1
        if keys[pygame.K_1]: to = 1
        elif keys[pygame.K_2]: to = 2
        elif keys[pygame.K_3]: to = 3
        elif keys[pygame.K_4]: to = 4
        elif keys[pygame.K_5]: to = 5
        elif keys[pygame.K_6]: to = 6
        elif keys[pygame.K_7]: to = 7
        elif keys[pygame.K_8]: to = 8
        elif keys[pygame.K_9]: to = 9
        elif keys[pygame.K_0]: to = 0
        if to != -1:
            self.board.board[self.selected.y][self.selected.x] = to




        if mouse_down and 0 < mouse_pos.x - self.space < self.board.size.x * self.pixel_size and \
                0 < mouse_pos.y - self.space < self.board.size.y * self.pixel_size:
            self.selected = vector2((mouse_pos.x - self.space) // self.pixel_size, (mouse_pos.y - self.space) // self.pixel_size)

        self.draw()

        return 0  # event
