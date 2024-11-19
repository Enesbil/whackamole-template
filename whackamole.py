import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        grid_scale = 32
        mole = (0, 0)
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x_touch, y_touch = event.pos
                    mole_x, mole_y = mole
                    if mole_x <= x_touch < mole_x + grid_scale and mole_y <= y_touch < mole_y + grid_scale:
                        new_x = random.randint(0, 19) * 32
                        new_y = random.randint(0, 15) * 32
                        mole = (new_x, new_y)

            screen.fill((213, 247, 242))

            for i in range(1, 21):
                pygame.draw.line(screen, (0, 0, 139), (32 * i, 0), (32 * i, 512))
                pygame.draw.line(screen, (0, 0, 139), (0, 32 * i), (640, 32 * i))

            if mole:
                x, y = mole
                screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
