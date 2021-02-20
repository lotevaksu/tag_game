import sys
import copy
from random import randint
import pygame


def main():
    pygame.init()

    size = 500, 500
    screen = pygame.display.set_mode(size)
    font = pygame.font.SysFont('Consolas', 50)

    green = 157, 201, 158
    white = 248, 248, 255
    blue = 34, 164, 245

    fps = pygame.time.Clock()

    main_board = [
        [1, 5, 9, 13],
        [2, 6, 10, 14],
        [3, 7, 11, 15],
        [4, 8, 12, 0]
    ]

    board = copy.deepcopy(main_board)

    for i in range(50):
        x1, y1 = randint(0, 3), randint(0, 3)
        x2, y2 = randint(0, 3), randint(0, 3)
        board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]

    running = True

    while running:
        fps.tick(60)

        pos = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

        screen.fill(green)

        for x in range(4):
            for y in range(4):
                rect = pygame.Rect(x * 125 + 10, y * 125 + 10, 105, 105)
                if pos:
                    if rect.collidepoint(pos):
                        current_piece = board[x][y]
                        moved = False
                        if current_piece > 0:
                            if x > 0 and board[x - 1][y] == 0:
                                board[x - 1][y] = current_piece
                                board[x][y] = 0
                                moved = True

                            if x < 3 and board[x + 1][y] == 0:
                                board[x + 1][y] = current_piece
                                board[x][y] = 0
                                moved = True

                            if y > 0 and board[x][y - 1] == 0:
                                board[x][y - 1] = current_piece
                                board[x][y] = 0
                                moved = True

                            if y < 3 and board[x][y + 1] == 0:
                                board[x][y + 1] = current_piece
                                board[x][y] = 0
                                moved = True

                        if moved:
                            pygame.mixer.music.load('move-click.mp3')
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load('wrong-click.mp3')
                            pygame.mixer.music.play()

                if board == main_board:
                    print('You are win')
                    running = False

                pygame.draw.rect(screen, white, rect)

                piece = board[x][y]
                if piece:
                    typeface = font.render(str(piece), True, blue)
                    screen.blit(typeface,
                                (rect.left + (rect.width - typeface.get_width()) / 2,
                                 rect.top + (rect.height - typeface.get_width()) / 2))

        pygame.display.flip()


if __name__ == '__main__':
    main()
