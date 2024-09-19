import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置窗口大小
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Action Game")

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 定义玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.speed_x = -5
        if keys[pygame.K_RIGHT]:
            self.speed_x = 5
        if keys[pygame.K_UP]:
            self.speed_y = -5
        if keys[pygame.K_DOWN]:
            self.speed_y = 5

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 边界检测
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# 定义敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed_y = random.randint(1, 5)

# 创建玩家和敌人组
player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(player)

for _ in range(10):  # 添加 10 个敌人
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)

# 游戏循环
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # 限制帧率为每秒 60 帧

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新游戏状态
    all_sprites.update()

    # 检测碰撞
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        print("Player hit!")
        running = False

    # 绘制场景
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # 刷新屏幕
    pygame.display.flip()

pygame.quit()
