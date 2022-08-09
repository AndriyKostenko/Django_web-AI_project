import pygame
import os

pygame.init()

#global const
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join('static/persik/images', 'DinoRun1.png')),
           pygame.image.load(os.path.join('static/persik/images', 'DinoRun2.png'))]
JUMPING = pygame.image.load(os.path.join('static/persik/images', 'DinoJump.png'))
DUCKING = [pygame.image.load(os.path.join('static/persik/images', 'DinoDuck1.png')),
           pygame.image.load(os.path.join('static/persik/images', 'DinoDuck2.png'))]
SMALL_CACTUS = [pygame.image.load(os.path.join('static/persik/images', 'SmallCactus1.png'))]
LARGE_CACTUS = [pygame.image.load(os.path.join('static/persik/images', 'LargeCactus1.png'))]
BIRD = [pygame.image.load(os.path.join('static/persik/images', 'Bird1.png')),
        pygame.image.load(os.path.join('static/persik/images', 'Bird2.png'))]

TRACK = pygame.image.load(os.path.join('static/persik/images', 'Track.png'))


class DinoCat:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, user_input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]  # for animation of dino running to change between pict.
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5] # for animation of dino running to change between pict.
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL


    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))




def main():
    run = True
    clock = pygame.time.Clock()
    player = DinoCat()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        SCREEN.fill((255, 255, 255))
        user_input = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(user_input)

        clock.tick(30)
        pygame.display.update()





main()