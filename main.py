import pygame

pygame.init()
pygame.display.set_caption('tic_tac_toe_4_zoomers')
size = [600, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color('white'), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top,
                    self.cell_size, self.cell_size), 1)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size


class TicTacToe(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.selected_cell = None
        self.current_turn = 1

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def on_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        x = cell[0]
        y = cell[1]
        print(x, y)
        if self.board[y][x] == 0:
            if self.current_turn == 1:
                self.current_turn = 2
            else:
                self.current_turn = 1
            self.board[y][x] = self.current_turn
        else:
            print('Эта клетка уже занята')

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 1:
                    pygame.draw.line(screen, pygame.Color('red'),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top),
                                     (x * self.cell_size + self.left + self.cell_size,
                                      y * self.cell_size + self.top + self.cell_size))
                    pygame.draw.line(screen, pygame.Color('red'),
                                     (x * self.cell_size + self.left,
                                      y * self.cell_size + self.top + self.cell_size),
                                     (x * self.cell_size + self.left + self.cell_size, y * self.cell_size + self.top))
                if self.board[y][x] == 2:
                    pygame.draw.ellipse(screen, pygame.Color('blue'),
                                        (x * self.cell_size + self.left + 5, y * self.cell_size + self.top + 5,
                                         self.cell_size - 10, self.cell_size - 10), 1)
                pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                                  self.cell_size), 1)


board = TicTacToe(3, 3)
board.set_view(15, 15, 190)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.on_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
pygame.quit()