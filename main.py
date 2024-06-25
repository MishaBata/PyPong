import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect(300, 550, 200, 50)  # Center the rectangle horizontally
ball = pygame.Rect(650, 200, 50, 50)

ball_x = ball.x
ball_y = ball.y

count = 0
# Начальные скорости шарика
ball_dx = -0.1
ball_dy = 0.1

# Настройка шрифта для отображения текста
font = pygame.font.Font(None, 36)  # Использование встроенного шрифта, размер 36

run = True
while run:
    screen.fill((0, 0, 0))

    # Обновление точных координат шарика
    ball_x += ball_dx
    ball_y += ball_dy
    ball.topleft = (ball_x, ball_y)

    # Проверка столкновений с границами экрана
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_dx = -ball_dx
        count += 1
    if ball.top <= 0:
        ball_dy = -ball_dy
        count += 1

    # Проверка столкновения с платформой
    if ball.colliderect(player) and ball_dy > 0:  # Условие для отскока от платформы (только при движении вниз)
        ball_dy = -ball_dy
        count += 1

    # Проверка, если шарик упал ниже платформы
    if ball.bottom >= SCREEN_HEIGHT:
        run = False  # Остановка игры при падении шарика ниже экрана

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        if player.left > 0:
            player.move_ip(-1, 0)
    if key[pygame.K_d]:
        if player.right < SCREEN_WIDTH:
            player.move_ip(1, 0)

    pygame.draw.rect(screen, (255, 0, 0), player)  # Рисуем красный прямоугольник
    pygame.draw.rect(screen, (0, 0, 255), ball)  # Рисуем синий шарик

    # Создание текста и отображение его на экране
    count_text = font.render(f"Count: {count}", True, (255, 255, 255))  # Белый цвет текста
    screen.blit(count_text, (10, 10))  # Размещение текста в верхнем левом углу

    pygame.display.update()

pygame.quit()
