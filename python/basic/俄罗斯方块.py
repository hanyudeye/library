import pygame
import random

# 初始化
pygame.init()

# 游戏窗口参数
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# 颜色定义
COLORS = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 150, 0),
    (0, 0, 255),
    (255, 120, 0),
    (255, 255, 0),
    (180, 0, 255),
    (0, 220, 220)
]

# 方块形状
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

class Tetromino:
    def __init__(self, x, y):
        self.shape = random.choice(SHAPES)
        self.color = random.randint(1, len(COLORS)-1)
        self.x = x
        self.y = y

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("俄罗斯方块")
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = Tetromino(GRID_WIDTH//2-1, 0)
        self.score = 0
        self.game_over = False

    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                rect = pygame.Rect(x*GRID_SIZE, y*GRID_SIZE, GRID_SIZE-1, GRID_SIZE-1)
                pygame.draw.rect(self.screen, COLORS[self.grid[y][x]], rect)

    def draw_piece(self, piece):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect((piece.x + x)*GRID_SIZE, 
                                     (piece.y + y)*GRID_SIZE,
                                     GRID_SIZE-1, GRID_SIZE-1)
                    pygame.draw.rect(self.screen, COLORS[piece.color], rect)

    def check_collision(self, piece, dx=0, dy=0):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = piece.x + x + dx
                    new_y = piece.y + y + dy
                    if (new_x < 0 or new_x >= GRID_WIDTH or
                        new_y >= GRID_HEIGHT or
                        (new_y >= 0 and self.grid[new_y][new_x])):
                        return True
        return False

    def merge_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece.y + y][self.current_piece.x + x] = self.current_piece.color
        self.clear_lines()
        self.current_piece = Tetromino(GRID_WIDTH//2-1, 0)
        if self.check_collision(self.current_piece):
            self.game_over = True

    def clear_lines(self):
        lines_cleared = 0
        for y in range(GRID_HEIGHT-1, -1, -1):
            if 0 not in self.grid[y]:
                del self.grid[y]
                self.grid.insert(0, [0]*GRID_WIDTH)
                lines_cleared += 1
        self.score += lines_cleared ** 2 * 100

    def run(self):
        fall_time = 0
        fall_speed = 500  # 下落间隔（毫秒）

        while not self.game_over:
            self.screen.fill(COLORS[0])
            delta_time = self.clock.get_time()
            fall_time += delta_time

            # 处理输入
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if not self.check_collision(self.current_piece, dx=-1):
                            self.current_piece.x -= 1
                    if event.key == pygame.K_RIGHT:
                        if not self.check_collision(self.current_piece, dx=1):
                            self.current_piece.x += 1
                    if event.key == pygame.K_DOWN:
                        fall_speed = 50
                    if event.key == pygame.K_UP:
                        self.current_piece.rotate()
                        if self.check_collision(self.current_piece):
                            self.current_piece.rotate()

            # 自动下落
            if fall_time >= fall_speed:
                if not self.check_collision(self.current_piece, dy=1):
                    self.current_piece.y += 1
                    fall_time = 0
                else:
                    self.merge_piece()
                    fall_time = 0
                    fall_speed = 500

            # 绘制
            self.draw_grid()
            self.draw_piece(self.current_piece)
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()