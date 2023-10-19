import pygame
import random

# Inicialização do pygame
pygame.init()

# Definições de cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Tamanho da janela e grade
WINDOW_SIZE = 600
GRID_SIZE = 20

# Criação da janela
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Jogo da Cobrinha')


# Função para desenhar a cobra
def draw_snake(snake):
    for segment in snake: 
        pygame.draw.rect(window, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# Função para desenhar a comida
def draw_food(food):
    pygame.draw.rect(window, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# Função para mostrar a tela de game over
def show_game_over_screen(window, clock, score):
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("Aff, noob...", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    continue_text = font.render("Pressione C para continuar", True, WHITE)
    quit_text = font.render("Pressione Q para sair", True, WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return  # Retorna para continuar o jogo
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        window.fill(BLACK)
        window.blit(game_over_text, (WINDOW_SIZE // 2 - 100, WINDOW_SIZE // 2 - 50))
        window.blit(score_text, (WINDOW_SIZE // 2 - 50, WINDOW_SIZE // 2))
        window.blit(continue_text, (WINDOW_SIZE // 2 - 100, WINDOW_SIZE // 2 + 50))
        window.blit(quit_text, (WINDOW_SIZE // 2 - 80, WINDOW_SIZE // 2 + 100))
        pygame.display.flip()
        clock.tick(5)


# Função principal do jogo
def main():
    clock = pygame.time.Clock()

    running = True
    while running:
        snake = [(3, 3)]
        food = (random.randint(0, WINDOW_SIZE // GRID_SIZE - 1), random.randint(0, WINDOW_SIZE // GRID_SIZE - 1))
        direction = (1, 0)
        score = 0  # Inicializa a pontuação

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != (0, 1):
                        direction = (0, -1)
                    elif event.key == pygame.K_DOWN and direction != (0, -1):
                        direction = (0, 1)
                    elif event.key == pygame.K_LEFT and direction != (1, 0):
                        direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                        direction = (1, 0)

            new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

            if new_head in snake:
                show_game_over_screen(window, clock, score)  # Chama a tela de game over com o score
                break  # Sai do loop interno para reiniciar o jogo

            if new_head[0] < 0 or new_head[0] >= WINDOW_SIZE // GRID_SIZE or new_head[1] < 0 or new_head[
                1] >= WINDOW_SIZE // GRID_SIZE:
                show_game_over_screen(window, clock, score)  # Chama a tela de game over com o score
                break  # Sai do loop interno para reiniciar o jogo

            snake.insert(0, new_head)

            if new_head == food:
                food = (random.randint(0, WINDOW_SIZE // GRID_SIZE - 1), random.randint(0, WINDOW_SIZE // GRID_SIZE - 1))
                score += 1
            else:
                snake.pop()  # Remove a última posição da cobra para apagar o rastro

            window.fill(BLACK)  # Preenche a tela com a cor de fundo
            draw_snake(snake)
            draw_food(food)

            font = pygame.font.Font(None, 36)
            text = font.render(f"Score: {score}", True, WHITE)
            window.blit(text, (WINDOW_SIZE - 120, 10))

            pygame.display.update()

            clock.tick(10)

    pygame.quit()


if __name__ == '__main__':
    main()
