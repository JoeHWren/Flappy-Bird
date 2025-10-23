import random
import pygame
import heapq

(width, height) = (600, 600)

screen = pygame.display.set_mode((width, height))

background_colour = (0, 0, 255)
screen.fill(background_colour)

(bird_x, bird_y) = (100, 100)
bird_r = 10
bird_colour = (0, 255, 0)
jump_strength = 10
bird_v = 0
gravity = 0.3
max_bird_v = 10
score = 0

drawn = False

pipe_coords = []
pipe_heights = []


pygame.font.init()

font = pygame.font.SysFont('Comic Sans MS', 30)

def draw_score():
    global score
    global screen

    text_surface = font.render(str(round(score, 1)), False, (0, 0, 0))
    screen.blit(text_surface, (20, 20))

def draw_pipes():
    global pipe_x
    global on_screen
    global pipe_height
    global drawn
    global gap
    global pipe_width

    pipe_counter = 3
    displacement = width / pipe_counter
    pipe_velocity = 1

    pipe_width = 25
    gap = 200

    if drawn == False: 
        for counter in range(0, pipe_counter):
            
            pipe_coords.append(width + displacement*counter)
            pipe_heights.append(random.randrange(0, height - gap))

            drawn = True
    
    for counter in range(0, pipe_counter):
        pygame.draw.rect(screen, (0,255,0), (pipe_coords[counter], height - pipe_heights[counter], pipe_width, pipe_heights[counter]))
        pygame.draw.rect(screen, (0,255,0), (pipe_coords[counter], 0, pipe_width, height - pipe_heights[counter] - gap))

    for index in range(0, len(pipe_coords)):
        
        if pipe_coords[index] <= 0:
            pipe_coords[index] = width
            pipe_heights[index] = random.randrange(0, height - gap)
        else:
            pipe_coords[index] -= pipe_velocity


def check_pipe_collision(): 
    global pipe_coords
    global pipe_heights
    global bird_x
    global bird_y
    global gap
    global pipe_width
    global alive

    vertical = False
    horizontal = False

    if min(pipe_coords) < bird_x - pipe_width - bird_r:
        nearest_index = pipe_coords.index(heapq.nsmallest(2,pipe_coords)[1])
    else:
        nearest_index = pipe_coords.index(min(pipe_coords))

    if bird_y > height - (pipe_heights[nearest_index]) or bird_y < height - pipe_heights[nearest_index] - gap:
        vertical = True
    if bird_x + bird_r > pipe_coords[nearest_index] and bird_x - bird_r < pipe_coords[nearest_index] + pipe_width:
        horizontal = True
    if vertical and horizontal:        
        alive = False

def out_of_bounds():
    global bird_y
    global bird_v
    global alive 

    if(bird_y < bird_r):
        bird_v = 0
        bird_y = bird_r
        pygame.draw.circle(screen, bird_colour, (bird_x, bird_y), bird_r, width == 0)
    if(bird_y > height - bird_r):
        alive = False

def apply_gravity():
    global bird_y
    global bird_v

    bird_y += bird_v
    bird_v += gravity

def render_screen():
    screen.fill(background_colour)
    out_of_bounds()
    apply_gravity()
    draw_score()
    draw_pipes()
    check_pipe_collision()
    pygame.draw.circle(screen, bird_colour, (bird_x, bird_y), bird_r, width == 0)
    pygame.display.update()

def render_death():
    screen.fill((0, 0, 0))
    text_surface = font.render(f"You Died, Score: {str(round(score, 1))}", False, (255, 255, 255))
    rect = text_surface.get_rect(center = (width / 2, height / 2))
    screen.blit(text_surface, rect)
    pygame.display.update()

running = True
alive = True

while running:
    if alive == True:
        render_screen()
        score += 0.01
    if alive == False:
        render_death()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_v -= jump_strength
                if bird_v <= -max_bird_v:
                    bird_v = -max_bird_v
                
        if event.type == pygame.QUIT:
            running = False

    pygame.time.wait(10)


    