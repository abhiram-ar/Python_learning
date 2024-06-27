import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Alien Shooter")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player
player_width = 50
player_height = 50
player_x = width // 2 - player_width // 2
player_y = height - player_height - 10
player_speed = 5

# Bullet
bullet_width = 5
bullet_height = 15
bullet_speed = 7
bullets = []

# Alien
alien_width = 50
alien_height = 50
alien_speed = 2
aliens = []

# Game variables
score = 0
font = pygame.font.Font(None, 36)

# Create player
player = pygame.Rect(player_x, player_y, player_width, player_height)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player.centerx - bullet_width // 2, player.top, bullet_width, bullet_height)
                bullets.append(bullet)

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < width:
        player.x += player_speed

    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Create aliens
    if len(aliens) < 5:
        alien_x = random.randint(0, width - alien_width)
        alien = pygame.Rect(alien_x, 0, alien_width, alien_height)
        aliens.append(alien)

    # Move aliens
    for alien in aliens[:]:
        alien.y += alien_speed
        if alien.top > height:
            aliens.remove(alien)

    # Check for collisions
    for bullet in bullets[:]:
        for alien in aliens[:]:
            if bullet.colliderect(alien):
                bullets.remove(bullet)
                aliens.remove(alien)
                score += 1

    # Draw everything
    window.fill(BLACK)
    pygame.draw.rect(window, GREEN, player)
    for bullet in bullets:
        pygame.draw.rect(window, WHITE, bullet)
    for alien in aliens:
        pygame.draw.rect(window, RED, alien)

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    window.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()