import pygame
class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
    def set_view(self, screen, x, y, width, height):
        t, u = x, y
        len_cletki = width // self.width
        for i in range(self.height):
            u += len_cletki
            t = x
            for j in range(self.width):
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, "white", (t, u, len_cletki, len_cletki), 1)
                else:
                    pygame.draw.rect(screen, "white", (t, u, len_cletki, len_cletki), 0)
                t += len_cletki
    def get_cell(self, pos):
        x, y = pos
        for i in
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
        print(22)
screen = pygame.display.set_mode((300, 300))
board = Board(4, 3)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.set_view(screen, 50, 50, 100, 50)
    pygame.display.flip()