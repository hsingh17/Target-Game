import pygame
import random
import time
import math

class Target:
    current_targets = []
    MAX_RADIUS = 50
    NUM_CIRCLE = 2

    def __init__(self, center):
        #Constructor for a target. An instance of a target is add iff there is space for it in the array, it is within the screen, and it is not 
        #touching another circle
        self.radius = 0
        self.center = center
        self.reach_max = False
        if len(Target.current_targets) < Target.NUM_CIRCLE and Target.circle_inside(center) and not self.check_collision():
            Target.current_targets.append(self)
    
    #Check if circle touch each other. NOT WORKING
    def check_collision(self):
        c1_x, c1_y = self.center
        for target in Target.current_targets:
            c2_x, c2_y = target.center
            distance = math.sqrt((c1_x - c2_x)**2 + (c1_y - c2_y)**2)
            if distance <= self.radius + target.radius:
                return True
        return False

    #Increase or decrease the radius of a circle depnding on if it has reached its max radius or not
    #If it's radius is 0 and it has reached its max radius then it is removed from the list of current targets
    #and returns true to tell user that it has missed a target
    @classmethod
    def vary(cls):
        for target in Target.current_targets:
            if target.radius != cls.MAX_RADIUS and not target.reach_max:
                target.radius += 1 
                if(target.radius == 50):
                    target.reach_max = True
            elif target.reach_max and target.radius != 0:
                target.radius -= 1
            else:
                cls.current_targets.remove(target)
                return True
    
    #Draws target of multiple circles to make it look more like a target
    @classmethod
    def draw(cls):
        for target in Target.current_targets:
            pygame.draw.circle(window, DARK_ORANGE, target.center, target.radius)
            pygame.draw.circle(window, ORANGE, target.center, math.floor(target.radius * 0.75))
            pygame.draw.circle(window, LIGHT_ORANGE, target.center, math.floor(target.radius * 0.50))
            pygame.draw.circle(window, WHITE_ORANGE, target.center, math.floor(target.radius * 0.25))

    #Check if pointer has touched a target
    @classmethod
    def hit_check(cls, m_x, m_y):
        for target in Target.current_targets:
            c_x, c_y = target.center
            distance = math.sqrt((m_x - c_x)**2 + (m_y - c_y)**2)
            if distance <= target.radius:
                cls.current_targets.remove(target)
                return True
        return False

    #Check if circle is within the screen
    @classmethod 
    def circle_inside(cls, center):
        x,y = center
        if x + cls.MAX_RADIUS <= SCREEN_HEIGHT and x - cls.MAX_RADIUS >= 0:
            if y + cls.MAX_RADIUS <= SCREEN_WIDTH and y - cls.MAX_RADIUS >=0:
                return True
        return False

    #Increases diffciulty of game by 1 circle
    @classmethod
    def increase_difficulty(cls):
        cls.NUM_CIRCLE += 1

    #Resets target class variables to original if user wants to play again
    @classmethod
    def reset(cls):
        cls.NUM_CIRCLE = 2
        del cls.current_targets[:]

#Plays a sound, adds sound to library if not in there already
def play_sound(path):
    sound = SOUND_LIBRARY.get(path)
    if sound == None:
        sound = pygame.mixer.Sound(path)
        SOUND_LIBRARY[path] = sound
    sound.play()

#Displays score to screen
def display_score(score):
    score = SCORE_FONT.render(f"{score}", True, BLACK)
    window.blit(score, (40,70))

#Displays game over message
def game_over():
    message = LARGE_FONT.render('Game Over!', True, BLACK)
    window.blit(message, (SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 200))
    play_again = MEDIUM_FONT.render('Press Q to Exit or R to Restart!', True, BLACK)
    window.blit(play_again, (200, 400))

#Main game loop
def game_loop():
    run = True
    score = 0
    miss = 0
    total_targets = 0
    clock = pygame.time.Clock() 
    while run:
        while miss == 3:
            game_over()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        miss = 0 
                        run = False
                    elif event.key == pygame.K_r:
                        Target.reset()
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if Target.hit_check(x,y):
                    score += 1
                    if score != 0 and score % 10 == 0:
                        Target.increase_difficulty()
                        total_targets += Target.NUM_CIRCLE
                    play_sound('pop.wav')
                else:
                    play_sound('bullet.wav')
        
        new_target = Target((random.randint(1, SCREEN_HEIGHT), random.randint(1, SCREEN_WIDTH)))
        if Target.vary():
            play_sound('miss.wav')
            miss += 1
    
        window.fill(WHITE)
        Target.draw()
        display_score(score)
        clock.tick(30)
        pygame.display.update()

    pygame.quit


pygame.font.init()
pygame.init()

#Option variables
WHITE_ORANGE = (255,225,164)
DARK_ORANGE = (255,189,55)
LIGHT_ORANGE = (255,217,139)
ORANGE = (255,203,97)
WHITE = (255,255,255)
BLACK = (0,0,0)
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 700
LARGE_FONT = pygame.font.SysFont("Arial", 100)
MEDIUM_FONT = pygame.font.SysFont("Arial", 50)
SCORE_FONT = pygame.font.SysFont("Bit5x3 Regular", 50)
SOUND_LIBRARY = {}

window = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
pygame.display.set_caption("Target Game")

game_loop()
