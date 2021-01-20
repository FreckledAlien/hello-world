# Simple pygame program

# Import and initialize the pygame library
import pygame
import keyboard
import random
import time
import tkinter
import logging
import threading
import array




# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pink = (0, 112, 90)
blue = (11, 112, 92)
purple = (61, 122, 110)
white = (255,255,255)
red = (255,0,0)
clear = (255, 255, 255, 0)

        


def text_objects(text, font):
    textSurface = font.render(text, True, pink)
    return textSurface, textSurface.get_rect()

def text_objects_blue(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()


def text_objects_purple(text, font):
    textSurface = font.render(text, True, purple)
    return textSurface, textSurface.get_rect()

def text_objects_red(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def death():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects_red("YOU DIED", largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(TextSurf, TextRect)

    
    pygame.display.update()
    time.sleep(2)




def life():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects_red("2 LIVES LEFT", largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(TextSurf, TextRect)

    
    pygame.display.update()
  
    time.sleep(3)
    # counter = 0



def life_2():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects_red("1 LIFE LEFT", largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(TextSurf, TextRect)

    
    pygame.display.update()
  
    time.sleep(3)
 




  

def Level_Two_Stage():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Level Two", largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(TextSurf, TextRect)

    
    pygame.display.update()
    time.sleep(3)
    game_level_two()
  

def Level_Three_Stage():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects_blue("Level Three", largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(TextSurf, TextRect)

    
    pygame.display.update()
    time.sleep(3)
    game_level_three()
  
def Level_Four_Stage():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects_purple("Level Four", largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(TextSurf, TextRect)

    
    pygame.display.update()
    time.sleep(3)
    game_level_four()
  
def Boss_Stage():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects_purple("BOSS LEVEL", largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(TextSurf, TextRect)

    
    pygame.display.update()
    time.sleep(3)
    boss_level()
  
     
     
# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("turtle.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-10, 0)
            move_left_sound.play()
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)
            move_right_sound.play()
        if pressed_keys[K_SPACE]:
            pause = True
    

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("starfish.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 7)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
       
        if pygame.sprite.spritecollideany(player, enemies):
            
            counter.append('a')
            print(counter)
            counter_length = len(counter)
            if counter_length == 1:
                life()
                self.kill()
            if counter_length == 2:
                
                life_2()
                self.kill()
            if counter_length > 2:
                death()
                player.kill()
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                pygame.quit()
                    # Stop any moving sounds and play the collision sound
                move_up_sound.stop()
                move_down_sound.stop()
                # collision_sound.play()

                # Stop the loop
                # running = False

                    
    
  

# Define the crab object by extending pygame.sprite.Sprite
class Crab(pygame.sprite.Sprite):
    def __init__(self):
        super(Crab, self).__init__()
        self.surf = pygame.image.load("crab.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the crab based on a constant speed
    # Remove the crab when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-3, 0)
        if self.rect.right < 0:
            self.kill()
        if pygame.sprite.spritecollideany(player, crabs):
            
            counter.append('a')
            print(counter)
            counter_length = len(counter)
            if counter_length == 1:
                life()
                self.kill()
            if counter_length == 2:
                
                life_2()
                self.kill()
            if counter_length > 2:
                death()
                player.kill()
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                pygame.quit()
                    # Stop any moving sounds and play the collision sound
                move_up_sound.stop()
                move_down_sound.stop()
                # collision_sound.play()

                # Stop the loop
                # running = False


# Define the whale object by extending pygame.sprite.Sprite
class Whale(pygame.sprite.Sprite):
    def __init__(self):
        super(Whale, self).__init__()
        self.surf = pygame.image.load("whale.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 7)
    # Move the whale based on a constant speed
    # Remove the whale when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-7, 0)
        if self.rect.right < 0:
            self.kill()
        
        if pygame.sprite.spritecollideany(player, whales):
            
            counter.append('a')
            print(counter)
            counter_length = len(counter)
            if counter_length == 1:
                life()
                self.kill()
            if counter_length == 2:
                
                life_2()
                self.kill()
            if counter_length > 2:
                death()
                player.kill()
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                pygame.quit()
                    # Stop any moving sounds and play the collision sound
                move_up_sound.stop()
                move_down_sound.stop()
                # collision_sound.play()

                # Stop the loop
                # running = False

#Create pink star enemies
class PinkStar(pygame.sprite.Sprite):
    def __init__(self):
        super(PinkStar, self).__init__()
        self.surf = pygame.image.load("pink_star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(6, 8)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        if pygame.sprite.spritecollideany(player, stars):
            
            counter.append('a')
            print(counter)
            counter_length = len(counter)
            if counter_length == 1:
                life()
                self.kill()
            if counter_length == 2:
                
                life_2()
                self.kill()
            if counter_length > 2:
                death()
                player.kill()
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                pygame.quit()
                    # Stop any moving sounds and play the collision sound
                move_up_sound.stop()
                move_down_sound.stop()
                # collision_sound.play()

                # Stop the loop
                # running = False

#Create squid enemies
class Squid(pygame.sprite.Sprite):
    def __init__(self):
        super(Squid, self).__init__()
        self.surf = pygame.image.load("squid.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(7, 9)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        if pygame.sprite.spritecollideany(player, squids):
            
            counter.append('a')
            print(counter)
            counter_length = len(counter)
            if counter_length == 1:
                life()
                self.kill()
            if counter_length == 2:
                
                life_2()
                self.kill()
            if counter_length > 2:
                death()
                player.kill()
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                pygame.quit()
                    # Stop any moving sounds and play the collision sound
                move_up_sound.stop()
                move_down_sound.stop()
                # collision_sound.play()

                # Stop the loop
                # running = False


#Create squid enemies
class Seahorse(pygame.sprite.Sprite):
    def __init__(self):
        super(Seahorse, self).__init__()
        self.surf = pygame.image.load("sea_horse.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(7, 9)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        if pygame.sprite.spritecollideany(player, seahorses):
            
            counter.append('a')
            print(counter)
            counter_length = len(counter)
            if counter_length == 1:
                life()
                self.kill()
            if counter_length == 2:
                
                life_2()
                self.kill()
            if counter_length > 2:
                death()
                player.kill()
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                pygame.quit()
                    # Stop any moving sounds and play the collision sound
                move_up_sound.stop()
                move_down_sound.stop()
                # collision_sound.play()

                # Stop the loop
                # running = False



def Add_Enemy():
 # Create the new enemy and add it to sprite groups
    new_enemy = Enemy()
    enemies.add(new_enemy)
    all_sprites.add(new_enemy)

def Add_Crab():
    new_crab = Crab()
    crabs.add(new_crab)
    all_sprites.add(new_crab)

def Add_Whale():
    new_whale = Whale()
    whales.add(new_whale)
    all_sprites.add(new_whale)

def Add_Star():
    new_star = PinkStar()
    stars.add(new_star)
    all_sprites.add(new_star)

def Add_Squid():
    new_squid = Squid()
    squids.add(new_squid)
    all_sprites.add(new_squid)

def Add_Seahorse():
    new_seahorse = Seahorse()
    seahorses.add(new_seahorse)
    all_sprites.add(new_seahorse)



# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Setup for sounds. Defaults are good.
pygame.mixer.init()

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Instantiate player
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
crabs = pygame.sprite.Group()
whales = pygame.sprite.Group()
stars = pygame.sprite.Group()
squids = pygame.sprite.Group()
seahorses = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


# Load and play background music
pygame.mixer.music.load("bubbles.mp3")
pygame.mixer.music.play(-1)

# Load all sound files
move_up_sound = pygame.mixer.Sound("Blop.wav")
move_down_sound = pygame.mixer.Sound("Blop.wav")
move_left_sound = pygame.mixer.Sound("Blop.wav")
move_right_sound = pygame.mixer.Sound("Blop.wav")
# collision_sound = pygame.mixer.Sound("Collision.ogg")

counter = []

def boss_level():
    # Create a custom event for adding a new enemy
 
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 700)

    ADDSEAHORSE = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDSEAHORSE, 900)

    # Create custom events for adding a new crab
    ADDSTARS = pygame.USEREVENT + 3
    pygame.time.set_timer(ADDSTARS, 2000)

#     # Create custom events for adding a new whale
    ADDWHALE = pygame.USEREVENT + 4
    pygame.time.set_timer(ADDWHALE, 3000)

    ADDSQUID = pygame.USEREVENT + 5
    pygame.time.set_timer(ADDSQUID, 5000)


  

# # Run until the user asks to quit
    boss = True
  
    
    # Main loop
    while boss:

    
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    boss = False


            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                boss = False


                 # Add a new enemy?
            elif event.type == ADDENEMY:

                Add_Enemy()

            elif event.type == ADDSEAHORSE:
                Add_Seahorse()

                # Add a new crab?
            elif event.type == ADDSTARS:
                # Create the new crab and add it to sprite groups
                Add_Star()

            #     # Add a new whale?
            elif event.type == ADDWHALE:
                # Create the new crab and add it to sprite groups
                Add_Whale()

            elif event.type == ADDSQUID:
                # Create the new crab and add it to sprite groups
                Add_Squid()
                
   

            
    
        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()

        # Update the player sprite based on user keypresses
        player.update(pressed_keys)

        # Update enemy position
        enemies.update()
        crabs.update()
        whales.update()
        stars.update()
        squids.update()
        seahorses.update()

        # Fill the screen with colour
        screen.fill((255, 255, 255))



        ## Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollideany(player, enemies):
            # If so, then remove the player and stop the loop
            boss = False
        
        if pygame.sprite.spritecollideany(player, crabs):
        # If so, then remove the player and stop the loop
            boss = False
        
        if pygame.sprite.spritecollideany(player, whales):
        # If so, then remove the player and stop the loop
            boss = False

        if pygame.sprite.spritecollideany(player, stars):
        # If so, then remove the player and stop the loop
            boss = False

        if pygame.sprite.spritecollideany(player, squids):
        # If so, then remove the player and stop the loop
            boss = False

        if pygame.sprite.spritecollideany(player, seahorses):
        # If so, then remove the player and stop the loop
            boss = False
                  
                  
        
            # counter.append('a')
            

            # collision_lives()
           
           
            # death()
            # player.kill()
            # pygame.mixer.music.stop()
            # pygame.mixer.quit()
            # pygame.quit()
            #     # Stop any moving sounds and play the collision sound
            # move_up_sound.stop()
            # move_down_sound.stop()
            # # collision_sound.play()

            # # Stop the loop
            # running = False


        # Update the display
        pygame.display.flip()

        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)


def game_level_four():
    # Create a custom event for adding a new enemy
 
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 700)

    # Create custom events for adding a new crab
    ADDSTARS = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDSTARS, 2000)

#     # Create custom events for adding a new whale
    ADDWHALE = pygame.USEREVENT + 3
    pygame.time.set_timer(ADDWHALE, 3000)

    ADDSQUID = pygame.USEREVENT + 4
    pygame.time.set_timer(ADDSQUID, 5000)

    NEXTLEVEL5 = pygame.USEREVENT + 5
    pygame.time.set_timer(NEXTLEVEL5, 10000)

# # Run until the user asks to quit
    running4 = True
  
    
    # Main loop
    while running4:

    
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running4 = False


            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running4 = False


                 # Add a new enemy?
            elif event.type == ADDENEMY:

                Add_Enemy()
            

                # Add a new crab?
            elif event.type == ADDSTARS:
                # Create the new crab and add it to sprite groups
                Add_Star()

            #     # Add a new whale?
            elif event.type == ADDWHALE:
                # Create the new crab and add it to sprite groups
                Add_Whale()

            elif event.type == ADDSQUID:
                # Create the new crab and add it to sprite groups
                Add_Squid()
                
        
        

            elif event.type == NEXTLEVEL5:
                # Create the new crab and add it to sprite groups
           
                Boss_Stage()
                # LevelUp()
                boss_level()
                running4 = False


            
    
        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()

        # Update the player sprite based on user keypresses
        player.update(pressed_keys)

        # Update enemy position
        enemies.update()
        crabs.update()
        whales.update()
        stars.update()
        squids.update()

        # Fill the screen with colour
        screen.fill((255, 255, 255))



        ## Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollideany(player, enemies):
            # If so, then remove the player and stop the loop
            running4 = False
        
        if pygame.sprite.spritecollideany(player, crabs):
        # If so, then remove the player and stop the loop
            running4 = False
        
        if pygame.sprite.spritecollideany(player, whales):
        # If so, then remove the player and stop the loop
            running4 = False

        if pygame.sprite.spritecollideany(player, stars):
        # If so, then remove the player and stop the loop
            running4 = False

        if pygame.sprite.spritecollideany(player, squids):
        # If so, then remove the player and stop the loop
            running4 = False
        
        
            # counter.append('a')
            

            # collision_lives()
           
           
            # death()
            # player.kill()
            # pygame.mixer.music.stop()
            # pygame.mixer.quit()
            # pygame.quit()
            #     # Stop any moving sounds and play the collision sound
            # move_up_sound.stop()
            # move_down_sound.stop()
            # # collision_sound.play()

            # # Stop the loop
            # running = False


        # Update the display
        pygame.display.flip()

        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)


game_level_four()
# All done! Stop and quit the mixer.
pygame.mixer.music.stop()
pygame.mixer.quit()
    
# Done! Time to quit.
pygame.quit()

