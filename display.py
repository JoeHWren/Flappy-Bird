import random
import pygame 

(width, height) = (600, 600)

screen = pygame.display.set_mode((width, height))

background_colour = (0, 0, 255)
screen.fill(background_colour)

(bird_x, bird_y) = (100, 100)
bird_r = 10
bird_colour = (0, 255, 0)
jump_strength = 10
bird_v = 0
gravity = 0.2
max_bird_v = 10


running = True
while running:
    screen.fill(background_colour)

    if(bird_y < bird_r):
        bird_v = 0
        bird_y = bird_r
        pygame.draw.circle(screen, bird_colour, (bird_x, bird_y), bird_r, width == 0)
    pygame.draw.circle(screen, bird_colour, (bird_x, bird_y), bird_r, width == 0)
    pygame.display.update()

    bird_y += bird_v
    bird_v += gravity


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print(bird_v)
                print(bird_y)
                bird_v -= jump_strength
                if bird_v <= -max_bird_v:
                    bird_v = -max_bird_v
                
        if event.type == pygame.QUIT:
            running = False

    pygame.time.wait(10)