import pygame



pygame.init()


WIDTH = 700 # Ширина
HEIGHT = 400 # Высота
TITLE = "Игра-платформер"
FPS = 30


screen = pygame.display.set_mode((WIDTH, HEIGHT)) # flags=pygame.NOFRAME
icon = pygame.image.load("Images/Icons/icon_snake.png") # Загружаем иконку игры
pygame.display.set_icon(icon) # Меняем иконку игры
pygame.display.set_caption(TITLE) # Меняем название игры
clock = pygame.time.Clock()





fon = pygame.image.load("Images/Backgronds/Background_2.jpg") # Загружаем фон (а точнее фотографию, которую мы сделаем фоном)
pers_stay = pygame.image.load("Images/Characters and Items/pers_stay.png") # Загружаем персонажа (а точнее фотографию персонажа)
pers_run_right = pygame.image.load("Images/Characters and Items/pers_run_right.png")
pers_run_left = pygame.image.load("Images/Characters and Items/pers_run_left.png")
pers_down = pygame.image.load("Images/Characters and Items/pers_down.png")
pers_jumping_up = pygame.image.load("Images/Characters and Items/pers_jumping_up.png")
pers_jumping_down = pygame.image.load("Images/Characters and Items/pers_jumping_down.png")
# pers_hurt = pygame.image.load("Images/Characters and Items/pers_hurt.png")
# pers_lie = pygame.image.load("Images/Characters and Items/pers_lie.png")

orange_ball = pygame.image.load("Images/Characters and Items/orange_ball.png")
blue_ball = pygame.image.load("Images/Characters and Items/blue_ball.png")
purple_ball = pygame.image.load("Images/Characters and Items/purple_ball.png")
# fire_ball = pygame.image.load("Images/Characters and Items/fireball.png")
# electro_ball = pygame.image.load("Images/Characters and Items/electro_ball.png")

go = pygame.image.load("Images/Characters and Items/Game_Over_with_pers.png")


direction = "stay"

game_over = False # Флаг, который отвечает за мод игры
count = 0

pers_x = 90
pers_y = 225
orange_ball_x = 710
orange_ball_y = 250
blue_ball_x = 1100
blue_ball_y = 200
purple_ball_x = 710
purple_ball_y = 250

jumping = False
jump_count = 13

squat = False


running = True
while running:

    for event in pygame.event.get(): # Проходимся циклом по скринам (различным кадрам) приложения-игры
        if event.type == pygame.QUIT: # Выход из приложения-игры (закрытие приложения-игры) (Это делается, чтобы, во-первых, курсор мышки не показывал загрузку, когда мы наводимся на скрин, во-вторых, чтобы при нажатии на крестик (закрыть окно), окно закрывалось без проблем и без вывода ошибки (в окошко Run))
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not jumping:
                jumping = True
                # direction = "up"
            elif event.key == pygame.K_DOWN and not squat:
                squat = True
                pers_y = 250
                direction = "down"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pers_y = 225
                squat = False
                direction = "stay"


    if not game_over:

        # Прыжок
        if jumping:
            if jump_count >= -13:
                neg = 1
                direction = "jumping_up"
                if jump_count < 0:
                    direction = "jumping_down"
                    neg = -1
                pers_y -= (jump_count ** 2) * 0.2 * neg
                jump_count -= 1
            else:
                direction = "stay"
                jumping = False
                jump_count = 13

        # Движение первого (1) шарика
        if orange_ball_x > -75:
            orange_ball_x -= 5
        else:
            orange_ball_x = WIDTH + 20
            count += 1 # очки

        # Движение второго (2) шарика
        if blue_ball_x > -75:
            blue_ball_x -= 5
        else:
            blue_ball_x = WIDTH + 20
            count += 1 # очки

        # Управление героем
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and pers_x > 0:
            pers_x -= 6
            direction = "left"
        elif keys[pygame.K_RIGHT] and pers_x < 635:
            pers_x += 6
            direction = "right"


        # Cтолкновение
        if (pers_x < orange_ball_x + 70 and pers_x + 20 > orange_ball_x and pers_y < orange_ball_y + 30 and pers_y + 30 > orange_ball_y) \
                or (pers_x < blue_ball_x + 70 and pers_x + 30 > blue_ball_x and pers_y < blue_ball_y + 30 and pers_y + 30 > blue_ball_y):
            game_over = True





    screen.blit(fon, (0, 0)) # Устанавливаем фон на скрин

    if direction == "stay":
        screen.blit(pers_stay, (pers_x, pers_y)) # Добавляем (изображение) персонажа
    if direction == "right":
        screen.blit(pers_run_right, (pers_x, pers_y))
    if direction == "left":
        screen.blit(pers_run_left, (pers_x, pers_y))
    if direction == "jumping_up":
        screen.blit(pers_jumping_up, (pers_x, pers_y))
    if direction == "jumping_down":
        screen.blit(pers_jumping_down, (pers_x, pers_y))
    if direction == "down":
        screen.blit(pers_down, (pers_x, pers_y))



    # screen.blit(pers_run_right, (120, 225))
    # screen.blit(pers_run_left, (120, 225))
    # screen.blit(pers_down, (150, 240))
    # screen.blit(pers_jumping_up, (70, 214))
    # screen.blit(pers_jumping_down, (150, 225))
    # screen.blit(pers_hurt, (90, 230))
    # screen.blit(pers_lie, (90, 270))

    # screen.blit(fire_ball, (400, 280))
    # screen.blit(electro_ball, (300, 250))
    screen.blit(orange_ball, (orange_ball_x, orange_ball_y))
    screen.blit(blue_ball, (blue_ball_x, blue_ball_y))
    # screen.blit(purple_ball, (purple_ball_x, purple_ball_y))



    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Счёт: {count}", True, (255, 0, 0))
    screen.blit(score_text, ((10, 10)))

    if game_over:
        screen.blit(go, (0, 0))
        screen.blit(score_text, (320, 230))



    pygame.display.flip() ### Обновляем скрин (дисплей)
    clock.tick(FPS) # Частота кадров в секунду



