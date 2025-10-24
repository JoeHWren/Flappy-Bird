import random
import pygame

class Display:
    (width, height) = (600, 600)
    screen = pygame.display.set_mode((width, height))
    background_colour = (0, 0, 255)

class Bird:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.r = 10
        self.v = 0
        self.jump_strength = 7
        self.gravity = 0.3
        self.max_v = 10
        self.colour = (0, 255, 0)

    def apply_gravity(self):
        self.v += self.gravity
    
    def apply_jump(self):
        self.v = -self.jump_strength
    
    def update(self):
        self.y += self.v
        self.apply_gravity()
        self.draw_bird()
    
    def check_alive(self):
        return not (self.out_of_bounds() or self.check_pipe_collision()) 
        

    def draw_bird(self):
        pygame.draw.circle(Display.screen, self.colour, (self.x, self.y), self.r)
 
    def get_hitbox(self):
        return(pygame.Rect(self.x - self.r, self.y - self.r, self.r*2, self.r*2))
 
    def out_of_bounds(self):
        if self.y + self.r > Display.height:
            return True
        elif self.y - self.r < 0:  
            return True
  
    def check_pipe_collision(self):
        for i in range(0, pipe.count*2):
            if (pygame.Rect.colliderect(self.get_hitbox(), pipe.get_hitbox()[i])) == True:
                return True

class Game:

    score = 0
    alive = True

    def update(self):
        Display.screen.fill(Display.background_colour)
        pipe.update()
        bird.update()
        self.add_score()
        score.draw_score() 
        
        pygame.display.update()

    def death(self):
        Display.screen.fill((0, 0, 0))
        score.draw_score()
        pygame.display.update()

    def add_score(self):
        if bird.x - bird.r == min(pipe.x_values):
            Game.score += 1
 
class Pipe:
    def __init__(self):
        self.count = 3
        self.displacement = Display.width / self.count
        self.gap = 200
        self.width = 25
        self.colour = (0, 255, 0)
        self.speed = 2
        self.x = Display.width

        self.heights = []
        self.x_values = []
        self.hitboxes = []

        for i in range(0, self.count*2):
            self.hitboxes.append(0)
    
        for pipe_counter in range(0, self.count):
            self.heights.append(random.randrange(self.gap + 10, Display.height))
            self.x_values.append(self.x + self.displacement*pipe_counter)

    def draw_pipe(self, counter):
        pygame.draw.rect(Display.screen, self.colour, (self.x_values[counter], self.heights[counter], self.width, Display.height - self.heights[counter]))
        pygame.draw.rect(Display.screen, self.colour, (self.x_values[counter], 0, self.width, self.heights[counter] - self.gap))

    def draw_pipes(self):
        for pipe_number in range(0, self.count):
            self.draw_pipe(pipe_number)

    def update(self):
        self.draw_pipes()
        for i in range(0, self.count):
            self.x_values[i] -= self.speed
            self.hitboxes[i] = pygame.Rect(self.x_values[i], self.heights[i], self.width, Display.height - self.heights[i])
            self.hitboxes[self.count + i] = pygame.Rect(self.x_values[i], 0, self.width, self.heights[i] - self.gap)
            if self.x_values[i] + self.width < 0:
                self.x_values[i] = Display.width
                self.heights[i] = random.randrange(self.gap + 10, Display.height)

    def get_hitbox(self):
        return self.hitboxes

class Score:
    pygame.font.init() 

    font = pygame.font.SysFont('Comic Sans MS', 30)

    def draw_score(self):
        if bird.check_alive():
            text_surface = self.font.render(str(Game.score), False, (0, 0, 0))
            Display.screen.blit(text_surface, (50, 50))
        else:
            text_surface = self.font.render('You Died, Score: ' + str(Game.score), False, (255, 255, 255))
            text_rect = text_surface.get_rect(center = (Display.width / 2, Display.height / 2))
            Display.screen.blit(text_surface, text_rect)

    
 

running = True
alive = True

bird = Bird()
game = Game()
pipe = Pipe()
display = Display()
score = Score()

game.update()

while running:
    
    if bird.check_alive() == True:
        game.update()

    if bird.check_alive() == False:
        game.death()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                bird.apply_jump()
        if event.type == pygame.QUIT:
            running = False
        
    pygame.time.wait(10)


    