import pygame
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shotgun Game")

# Set up the background
background_image = pygame.image.load(r"C:\Us39.png").convert_alpha()
background_image = pygame.transform.scale(background_image, (width, height))

# Set up the player
player_size = 150
player_image = pygame.image.load(r"C:\Users\LENOVO\Downloads\image-dosseh-colors-vrai-removebg-preview.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (player_size, player_size))
player_x = width // 2 - player_size // 2
player_y = height - player_size

# Set up the shotgun
shotgun_image = pygame.image.load(r"C:\Usw.png").convert_alpha()
shotgun_image = pygame.transform.scale(shotgun_image, (100, 100))
shotgun_offset_x = 30
shotgun_offset_y = 70

# Set up the target
target_size = 150
target_image = pygame.image.load(r"C:\Usg-w.png").convert_alpha()
target_image = pygame.transform.scale(target_image, (target_size, target_size))
target_hit_image = pygame.image.load(r"C:\Usew.png").convert_alpha()
target_hit_image = pygame.transform.scale(target_hit_image, (target_size, target_size))
target_x = random.randint(0, width - target_size)
target_y = random.randint(0, height - target_size)
target_speed_x = 0.3
target_speed_y = 0.3
target_hit = False

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

# Load the success sound
success_sound = pygame.mixer.Sound(r"C:ngtone.wav")

# Load the clicking sound
clicking_sound = pygame.mixer.Sound(r"C:\Uwav")

# Set up reset button
reset_button = pygame.Rect(650, 10, 120, 40)
reset_text = font.render("Reset", True, (0, 0, 0))

# Set up exit button
exit_button = pygame.Rect(650, 60, 120, 40)
exit_text = font.render("Exit", True, (0, 0, 0))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicking_sound.play()

            # Check if reset button is clicked
            if reset_button.collidepoint(mouse_x, mouse_y):
                score = 0
                target_x = random.randint(0, width - target_size)
                target_y = random.randint(0, height - target_size)
                target_hit = False
                success_sound.stop()
                clicking_sound.play()
                player_size = 200
                player_image = pygame.transform.scale(player_image, (player_size, player_size))

            # Check if exit button is clicked
            elif exit_button.collidepoint(mouse_x, mouse_y):
                running = False

            elif not target_hit and mouse_x >= target_x and mouse_x <= target_x + target_size and \
                    mouse_y >= target_y and mouse_y <= target_y + target_size:
                score += 1
                target_hit = True
                success_sound.play()

    mouse_x, mouse_y = pygame.mouse.get_pos()

    window.blit(background_image, (0, 0))  # Draw the background

    if not target_hit:
        target_x += target_speed_x
        target_y += target_speed_y

        if target_x <= 0 or target_x >= width - target_size:
            target_speed_x *= -1
        if target_y <= 0 or target_y >= height - target_size:
            target_speed_y *= -1

    if target_hit:
        window.blit(target_hit_image, (target_x, target_y))  # Draw the hit target
    else:
        window.blit(target_image, (target_x, target_y))  # Draw the target

    window.blit(player_image, (player_x, player_y))  # Draw the player
    window.blit(shotgun_image, (mouse_x - shotgun_offset_x, mouse_y - shotgun_offset_y))  # Draw the shotgun

    pygame.draw.rect(window, (255, 255, 255), reset_button)
    window.blit(reset_text, (660, 20))

    pygame.draw.rect(window, (255, 255, 255), exit_button)
    window.blit(exit_text, (670, 70))

    score_text = font.render("By:Zed_King".format(score), True, (0, 0, 0))
    window.blit(score_text, (10, 10))  # Draw the score

    pygame.display.update()  # Update the display

# Quit the game
pygame.quit()
