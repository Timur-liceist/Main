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

    def render(self, screen):
        for w in range(self.width):
            for h in range(self.height):
                x = self.left + w * self.cell_size
                y = self.top + h * self.cell_size
                if self.board[h][w] == 0:
                    pygame.draw.rect(screen, "black", (x, y, self.cell_size, self.cell_size), 0)
                if self.board[h][w] == 1:
                    pygame.draw.rect(screen, "red", (x, y, self.cell_size, self.cell_size), 0)
                if self.board[h][w] == 2:
                    pygame.draw.rect(screen, "blue", (x, y, self.cell_size, self.cell_size), 0)
                pygame.draw.rect(screen, "white", (x, y, self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        if ((self.left < mouse_pos[0] < self.left + self.cell_size * self.width) and (
                self.top < mouse_pos[1] < self.top + self.cell_size * self.height)):
            column = (mouse_pos[0] - self.left) // self.cell_size
            row = (mouse_pos[1] - self.top) // self.cell_size
            return (column, row)
        return None

    def on_click(self, cell):
        # for x in range(self.width):
        #     self.board[cell[0]][x] = (self.board[cell[0]][x] + 1) % 2
        # for y in range(self.height):
        #     self.board[y][cell[1]] = (self.board[y][cell[1]] + 1) % 2
        # self.board[cell[0]][cell[1]] = (self.board[cell[0]][cell[1]] + 1) % 2
        if self.board[cell[1]][cell[0]] == 0:
            self.board[cell[1]][cell[0]] = 1
        elif self.board[cell[1]][cell[0]] == 1:
            self.board[cell[1]][cell[0]] = 2
        elif self.board[cell[1]][cell[0]] == 2:
            self.board[cell[1]][cell[0]] = 0
        # else:
        #     self.board[cell[1]][cell[0]] = 2

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


screen = pygame.display.set_mode((300, 300))
board = Board(5, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if board.get_cell(event.pos):
                board.on_click(board.get_cell(event.pos))
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
