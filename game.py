import pygame
from gameState import GameState


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(pygame.font.get_default_font(), 48)
    game = GameState(font)

    # Main loop
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.events(event)

        screen.fill((0, 0, 0))
        game.render(screen)

        game.tick()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
