import pygame
import os
import random




all_sprites = pygame.sprite.Group()
all_sprites10 = pygame.sprite.Group()
screen_rect = (0, 0, 600, 600)
gravity = 0.25
zvuk = True
l1 = False
l2 = False
l3 = False

def load_image(name, x = 100, y = 100):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, (x, y))
    return image


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites10)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость - это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой
        self.gravity = gravity

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))



class Pobeda:
    def __init__(self):
        size = 600, 600
        screen7 = pygame.display.set_mode(size)
        screen7.fill(pygame.Color(117, 187, 253))
        all_sprites7 = pygame.sprite.Group()


        fps = 50

        clock = pygame.time.Clock()

        # для отслеживания улетевших частиц
        # удобно использовать пересечение прямоугольников




        global zvuk
        if zvuk:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('data\muzpob.mp3')
            pygame.mixer.music.play(-1)
        rada = load_image("pob.jpg", 600, 600)
        rad = pygame.sprite.Sprite(all_sprites7)  # без звука
        rad.image = rada
        rad.rect = rad.image.get_rect()
        rad.rect.x = 0
        rad.rect.y = 0

        obla1 = load_image("home.png", 50, 50)
        obl1 = pygame.sprite.Sprite(all_sprites7)  # звук
        obl1.image = obla1
        obl1.rect = obl1.image.get_rect()
        obl1.rect.x = 10
        obl1.rect.y = 10

        pygame.display.flip()
        running7 = True


        pygame.mouse.set_visible(0)

        while running7:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    screen7.fill(pygame.Color(117, 187, 253))
                    running7 = False
                    main()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # создаем частицы по щелчку мыши
                    create_particles(pygame.mouse.get_pos())
                    pos = pygame.mouse.get_pos()
                    if 10 <= pos[0] <= 110 and 10 <= pos[1] <= 110:
                        screen7.fill(pygame.Color(117, 187, 253))
                        running7 = False
                        main()
            screen7.fill((117, 187, 253))
            all_sprites7.draw(screen7)
            all_sprites10.draw(screen7)
            all_sprites10.update()
            pygame.display.flip()
            clock.tick(100)
        pygame.quit()

class Lavel3:
    def __init__(self):
        size = 1000, 600
        screen3 = pygame.display.set_mode(size)
        screen3.fill(pygame.Color(117, 187, 253))
        running3 = True
        all_sprites2 = pygame.sprite.Group()

        obla1 = load_image("home.png", 100, 100)
        obl1 = pygame.sprite.Sprite(all_sprites2)  # звук
        obl1.image = obla1
        obl1.rect = obl1.image.get_rect()
        obl1.rect.x = 10
        obl1.rect.y = 10


        ra3 = load_image("otlich2.jpg", 500, 500)
        r3 = pygame.sprite.Sprite(all_sprites2)  # роса
        r3.image = ra3
        r3.rect = r3.image.get_rect()
        r3.rect.x = 250
        r3.rect.y = 10
        i = 0
        f1 = False
        f2 = False
        f3 = False
        pygame.display.flip()

        while running3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen3.fill(pygame.Color(117, 187, 253))
                    running3 = False
                    main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if (680 <= pos[0] <= 730 and 20 <= pos[1] <= 60) or (430 <= pos[0] <= 480 and 20 <= pos[1] <= 60) and f1 is False: #крыша
                        i += 1
                        f1 = True
                        pygame.draw.rect(screen3, pygame.Color(117, 187, 253), (100, 200, 50, 50))
                        font1 = pygame.font.Font(None, 100)  # слова вверху
                        text1 = font1.render(str(i), True, (0, 0, 0))
                        screen3.blit(text1, (100, 200))
                    if (610 <= pos[0] <= 650 and 360 <= pos[1] <= 410) or (360 <= pos[0] <= 400 and 360 <= pos[1] <= 410) and f2 is False: # солнце
                        i += 1
                        f2 = True
                        pygame.draw.rect(screen3, pygame.Color(117, 187, 253), (100, 200, 50, 50))
                        font1 = pygame.font.Font(None, 100)  # слова вверху
                        text1 = font1.render(str(i), True, (0, 0, 0))
                        screen3.blit(text1, (100, 200))
                    if ((640 <= pos[0] <= 690 and 220 <= pos[1] <= 270) or (570 <= pos[0] <= 620 and 220 <= pos[1] <= 270)) or ((390 <= pos[0] <= 440 and 220 <= pos[1] <= 270) or (320 <= pos[0] <= 370 and 220 <= pos[1] <= 270)) and f3 is False: # табличка
                        i += 1
                        f3 = True
                        pygame.draw.rect(screen3, pygame.Color(117, 187, 253), (100, 200, 50, 50))
                        font1 = pygame.font.Font(None, 100)  # слова вверху
                        text1 = font1.render(str(i), True, (0, 0, 0))
                        screen3.blit(text1, (100, 200))
                    if 10 <= pos[0] <= 110 and 10 <= pos[1] <= 110:
                        screen3.fill(pygame.Color(117, 187, 253))
                        running3 = False
                        main()
                    if i == 3:
                        global l1, l2, l3
                        l3 = True
                        running3 = False
                        screen3.fill(pygame.Color(117, 187, 253))
                        if l1 and l2 and l3:
                            n = Pobeda()
                        else:
                            main()

            all_sprites2.draw(screen3)
            pygame.display.flip()
        pygame.quit()



class Lavel2:
    def __init__(self):
        size = 1000, 650
        screen2 = pygame.display.set_mode(size)
        screen2.fill(pygame.Color(117, 187, 253))
        running2 = True
        all_sprites1 = pygame.sprite.Group()

        ra = load_image("rain.jpg", 300, 300)
        r = pygame.sprite.Sprite(all_sprites1)  # дождь
        r.image = ra
        r.rect = r.image.get_rect()
        r.rect.x = 150
        r.rect.y = 10

        obla1 = load_image("home.png", 100, 100)
        obl1 = pygame.sprite.Sprite(all_sprites1)  # звук
        obl1.image = obla1
        obl1.rect = obl1.image.get_rect()
        obl1.rect.x = 10
        obl1.rect.y = 10

        ra1 = load_image("rosa.jpg", 300, 300)
        r1 = pygame.sprite.Sprite(all_sprites1)  # роса
        r1.image = ra1
        r1.rect = r1.image.get_rect()
        r1.rect.x = 550
        r1.rect.y = 10

        self.width = 5
        self.height = 1
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = 280
        self.top = 350
        self.cell_size = 100
        self.render(screen2)

        pygame.draw.rect(screen2, pygame.Color(0, 0, 0), (800, 375, 50, 50), 5) # cleen
        font1 = pygame.font.Font(None, 100)  # слова вверху
        text1 = font1.render("X", True, (0, 0, 0))
        screen2.blit(text1, (803, 373))


        self.width = 7
        self.height = 1
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = 178
        self.top = 450
        self.cell_size = 100
        self.render(screen2)
        font0 = pygame.font.Font(None, 120)  # слова вверху
        text0 = font0.render("А  С  Я  К  Л  О  П", True, (255, 255, 255))
        screen2.blit(text0, (178, 455))
        a = []
        i1 = -1
        while running2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen2.fill(pygame.Color(117, 187, 253))
                    running2 = False
                    main()
                if event.type == pygame.KEYDOWN:

                    screen2.fill(pygame.Color(117, 187, 253))
                    global l1, l2, l3
                    l2 = True
                    if l1 and l2 and l3:
                        n = Pobeda()
                    else:
                        lev3 = Lavel3()
                    running2 = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 10 <= pos[0] <= 110 and 10 <= pos[1] <= 110:
                        screen2.fill(pygame.Color(117, 187, 253))
                        running2 = False
                        main()
                    if 180 <= pos[0] <= 260 and 450 <= pos[1] <= 550:
                       a.append("А")
                       i1 += 1
                    if 280 <= pos[0] <= 360 and 450 <= pos[1] <= 550:
                       a.append("С")
                       i1 += 1
                    if 380 <= pos[0] <= 460 and 450 <= pos[1] <= 550:
                       a.append("Я")
                       i1 += 1
                    if 480 <= pos[0] <= 560 and 450 <= pos[1] <= 550:
                       a.append("К")
                       i1 += 1
                    if 580 <= pos[0] <= 660 and 450 <= pos[1] <= 550:
                       a.append("Л")
                       i1 += 1
                    if 680 <= pos[0] <= 760  and 450 <= pos[1] <= 550:
                       a.append("О")
                       i1 += 1
                    if 780 <= pos[0] <= 860 and 450 <= pos[1] <= 550:
                       a.append("П")
                       i1 += 1
                    if 805 <= pos[0] <= 845 and 380 <= pos[1] <= 420:
                        a = []
                        i1 = -1
                        self.left = 280
                        self.top = 350
                        self.cell_size = 100
                        for i in range(0, 5):
                            for j in range(0, 1):
                                pygame.draw.rect(screen2, pygame.Color(117, 187, 253), (
                                        self.left + (i * self.cell_size), self.top + (j * self.cell_size),
                                        self.cell_size,
                                        self.cell_size))
                                pygame.draw.rect(screen2, pygame.Color(255, 255, 255), (
                                    self.left + (i * self.cell_size), self.top + (j * self.cell_size),
                                    self.cell_size,
                                    self.cell_size), 5)
                        continue
                    if len(a) != 0:
                        font1 = pygame.font.Font(None, 100)  # заполняем таблицу
                        text1 = font1.render(a[i1], True, (0, 0, 0))
                        screen2.blit(text1, (i1 * 100 + 290, 355))
                    if len(a) == 5:
                        font1 = pygame.font.Font(None, 100)  # заполняем таблицу
                        text1 = font1.render(a[i1], True, (0, 0, 0))
                        screen2.blit(text1, (i1 * 100 + 290, 355))
                        if a[0] == "К" and a[1] == "А" and a[2] == "П" and a[3] == "Л" and a[4] == "Я":
                            font = pygame.font.Font(None, 20)
                            text2 = font.render("Для перехода на следующий уровень нажмите любую кнопку...", True,
                                                (0, 0, 0))
                            screen2.blit(text2, (5, 600))
                        else:
                            i1 = -1
                            a = []
                            self.left = 280
                            self.top = 350
                            self.cell_size = 100
                            for i in range(0, 5):
                                for j in range(0, 1):
                                    pygame.draw.rect(screen2, pygame.Color(117, 187, 253), (
                                        self.left + (i * self.cell_size), self.top + (j * self.cell_size),
                                        self.cell_size,
                                        self.cell_size))
                                    pygame.draw.rect(screen2, pygame.Color(255, 255, 255), (
                                        self.left + (i * self.cell_size), self.top + (j * self.cell_size),
                                        self.cell_size,
                                        self.cell_size), 5)

            all_sprites1.draw(screen2)
            pygame.display.flip()
        pygame.quit()

    def render(self, screen1):
        for i in range(0, self.width):
            for j in range(0, self.height):
                    pygame.draw.rect(screen1, pygame.Color(255, 255, 255), (
                        self.left + (i * self.cell_size), self.top + (j * self.cell_size), self.cell_size,
                        self.cell_size), 5)

class Lavel1:
    def __init__(self):
        size = 1000, 650
        screen1 = pygame.display.set_mode(size)
        all_sprites6 = pygame.sprite.Group()
        screen1.fill(pygame.Color(117, 187, 253))
        self.width = 5
        self.height = 5
        self.board = [[0] * self.width for _ in range(self.height)]
        self.t1 = False
        self.t2 = False
        self.t3 = False
        self.left = 250
        self.top = 80
        self.cell_size = 100
        self.render(screen1)

        obla1 = load_image("home.png", 100, 100)
        obl1 = pygame.sprite.Sprite(all_sprites6)  # звук
        obl1.image = obla1
        obl1.rect = obl1.image.get_rect()
        obl1.rect.x = 10
        obl1.rect.y = 10

        running1 = True
        while running1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen1.fill(pygame.Color(117, 187, 253))
                    running1 = False
                    main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.get_click(event.pos, screen1)
                    self.render(screen1)
                    pos = pygame.mouse.get_pos()
                    if 10 <= pos[0] <= 110 and 10 <= pos[1] <= 110:
                        screen1.fill(pygame.Color(117, 187, 253))
                        running1 = False
                        main()

                if event.type == pygame.KEYDOWN:
                    screen1.fill(pygame.Color(117, 187, 253))

                    global l1, l2, l3
                    l1 = True
                    if l1 and l2 and l3:
                        n = Pobeda()
                    else:
                        lev2 = Lavel2()
                    running1 = False
            pygame.display.flip()
            all_sprites6.draw(screen1)
        pygame.quit()


    def get_click(self, mouse_pos, screen1):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell, screen1)



    def on_click(self, cell, screen1):
        x = cell[0]
        y = cell[1]
        if self.board[x][y] == 0:
            self.board[x][y] = 1
        elif self.board[x][y] == 1:
            self.board[x][y] = 0
        font0 = pygame.font.Font(None, 50)
        if self.prov(2, 0, 3, 0, 4, 0):
            pygame.draw.rect(screen1, pygame.Color(117, 187, 253),
                             (480, 10, 100, 100))
            text1 = font0.render("------", True, (255, 255, 255))
            screen1.blit(text1, (480, 10))
            self.t1 = True
        elif self.prov(0, 0, 0, 1, 0, 2):
            text0 = font0.render("------", True, (255, 255, 255))
            screen1.blit(text0, (255, 10))
            self.t2 = True
        elif self.prov(2, 3, 3, 3, 4, 3):
            text2 = font0.render("------", True, (255, 255, 255))
            screen1.blit(text2, (700, 10))
            self.t3 = True
        if self.t1 and self.t2 and self.t3:
            font = pygame.font.Font(None, 20)
            text2 = font.render("Для перехода на следующий уровень нажмите любую кнопку...", True, (0, 0, 0))
            screen1.blit(text2, (5, 600))


    def prov(self, x, y, x1, y1, x2, y2):
        if self.board[x][y] == 1 and self.board[x1][y1] == 1 and self.board[x2][y2] == 1:
            self.board[x][y] = 0
            self.board[x1][y1] = 0
            self.board[x2][y2] = 0
            f = True
            for i in range(5):
                for j in range(5):
                    if self.board[i][j] == 1:
                        f = False
            if f:
                return True
            else:
                self.board[x][y] = 1
                self.board[x1][y1] = 1
                self.board[x2][y2] = 1
                return False

    def get_cell(self, mouse_pos):
        return [round((mouse_pos[0] - 200)/ self.cell_size) - 1, round((mouse_pos[1] - 90) / self.cell_size) - 1]

    def render(self, screen1):
        for i in range(0, self.width):
            for j in range(0, self.height):

                if self.board[i][j] == 0:
                    pygame.draw.rect(screen1, pygame.Color(255, 255, 255), (
                        self.left + (i * self.cell_size), self.top + (j * self.cell_size), self.cell_size,
                        self.cell_size))

                elif self.board[i][j] == 1:
                    pygame.draw.rect(screen1, pygame.Color(255, 192, 203), (
                        self.left + (i * self.cell_size), self.top + (j * self.cell_size), self.cell_size,
                        self.cell_size))

                pygame.draw.rect(screen1, pygame.Color(0, 0, 0), (
                    self.left + (i * self.cell_size), self.top + (j * self.cell_size), self.cell_size,
                    self.cell_size), 1, 0)

        font0 = pygame.font.Font(None, 50)  # слова вверху
        text0 = font0.render("сон", True, (255, 255, 255))
        screen1.blit(text0, (255, 10))
        text1 = font0.render("ток", True, (255, 255, 255))
        screen1.blit(text1, (480, 10))
        text2 = font0.render("эра", True, (255, 255, 255))
        screen1.blit(text2, (700, 10))

        font = pygame.font.Font(None, 100)  # таблица для игры
        text = font.render(" C   Л   Т  О   К", True, (100, 255, 100))
        screen1.blit(text, (255, 87))
        text = font.render(" О  Ф  О   Т   Л", True, (100, 255, 100))
        screen1.blit(text, (255, 187))
        text = font.render(" Н  П   О   Т   А", True, (100, 255, 100))
        screen1.blit(text, (255, 287))
        text = font.render(" М  С   Э   Р   А", True, (100, 255, 100))
        screen1.blit(text, (255, 387))
        text = font.render(" Д  М  Б  Ю   Л", True, (100, 255, 100))
        screen1.blit(text, (255, 487))

class Pravila():
    def __init__(self):
        size = 600, 500
        screen8 = pygame.display.set_mode(size)
        screen8.fill(pygame.Color(117, 187, 253))
        all_sprites8 = pygame.sprite.Group()

        obla1 = load_image("уровни1.png", 600, 500)
        obl1 = pygame.sprite.Sprite(all_sprites8)  # level1
        obl1.image = obla1
        obl1.rect = obl1.image.get_rect()
        obl1.rect.x = 0
        obl1.rect.y = 0

        pygame.display.flip()
        running8 = True
        while running8:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen8.fill(pygame.Color(117, 187, 253))
                    running8 = False
                    main()
            all_sprites8.draw(screen8)
            pygame.display.flip()
        pygame.quit()


class Urov:
    def __init__(self):
        size = 1000, 650
        screen4 = pygame.display.set_mode(size)
        screen4.fill(pygame.Color(117, 187, 253))
        all_sprites4 = pygame.sprite.Group()

        obla1 = load_image("pravil.png", 100, 100)
        obl1 = pygame.sprite.Sprite(all_sprites4)  # level1
        obl1.image = obla1
        obl1.rect = obl1.image.get_rect()
        obl1.rect.x = 110
        obl1.rect.y = 10

        obla1 = load_image("3.jpg", 100, 200)
        obl1 = pygame.sprite.Sprite(all_sprites4)  # level1
        obl1.image = obla1
        obl1.rect = obl1.image.get_rect()
        obl1.rect.x = 700
        obl1.rect.y = 300

        obla1 = load_image("home.png", 100, 100)
        obl1 = pygame.sprite.Sprite(all_sprites4)  # звук
        obl1.image = obla1
        obl1.rect = obl1.image.get_rect()
        obl1.rect.x = 10
        obl1.rect.y = 10

        rada = load_image("2.png", 100, 200)
        rad = pygame.sprite.Sprite(all_sprites4)  # level2
        rad.image = rada
        rad.rect = rad.image.get_rect()
        rad.rect.x = 400
        rad.rect.y = 150

        obla = load_image("1.jpg", 100, 200)
        obl = pygame.sprite.Sprite(all_sprites4)  # level3
        obl.image = obla
        obl.rect = obl.image.get_rect()
        obl.rect.x = 100
        obl.rect.y = 300

        global l1, l2, l3
        if l1:
            obla = load_image("zvezd.png", 200, 100)
            obl = pygame.sprite.Sprite(all_sprites4)  # level3
            obl.image = obla
            obl.rect = obl.image.get_rect()
            obl.rect.x = 50
            obl.rect.y = 450

        if l2:
            obla = load_image("zvezd.png", 200, 100)
            obl = pygame.sprite.Sprite(all_sprites4)  # level3
            obl.image = obla
            obl.rect = obl.image.get_rect()
            obl.rect.x = 350
            obl.rect.y = 300

        if l3:
            obla = load_image("zvezd.png", 200, 100)
            obl = pygame.sprite.Sprite(all_sprites4)  # level3
            obl.image = obla
            obl.rect = obl.image.get_rect()
            obl.rect.x = 650
            obl.rect.y = 450

        pygame.display.flip()
        running4 = True
        while running4:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen4.fill(pygame.Color(117, 187, 253))
                    running4 = False
                    main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 400 <= pos[0] <= 600 and 100 <= pos[1] <= 400:
                        n1 = Lavel2()
                    if 100 <= pos[0] <= 300 and 250 <= pos[1] <= 550:
                        n2 = Lavel1()
                    if 700 <= pos[0] <= 900 and 250 <= pos[1] <= 550:
                        n3 = Lavel3()
                    if 10 <= pos[0] <= 110 and 10 <= pos[1] <= 110:
                        screen4.fill(pygame.Color(117, 187, 253))
                        running4 = False
                        main()
                    if 110 <= pos[0] <= 210 and 10 <= pos[1] <= 110:
                        p = Pravila()
            all_sprites4.draw(screen4)
            pygame.display.flip()
        pygame.quit()

class Menu:
    def __init__(self):
        size = 1000, 650
        screen5 = pygame.display.set_mode(size)
        screen5.fill(pygame.Color(117, 187, 253))
        all_sprites5 = pygame.sprite.Group()

        obla1 = load_image("home.png", 100, 100)
        obl1 = pygame.sprite.Sprite(all_sprites5)  # звук
        obl1.image = obla1
        obl1.rect = obl1.image.get_rect()
        obl1.rect.x = 10
        obl1.rect.y = 10



        obla1 = load_image("zv12.png", 100, 100)
        obl1 = pygame.sprite.Sprite(all_sprites5)  # звук
        obl1.image = obla1
        obl1.rect = obl1.image.get_rect()
        obl1.rect.x = 150
        obl1.rect.y = 300

        rada = load_image("zv0.png", 100, 100)
        rad = pygame.sprite.Sprite(all_sprites5)  # без звука
        rad.image = rada
        rad.rect = rad.image.get_rect()
        rad.rect.x = 750
        rad.rect.y = 300

        running5 = True
        while running5:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen5.fill(pygame.Color(117, 187, 253))
                    running5 = False
                    main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 150 <= pos[0] <= 250 and 300 <= pos[1] <= 400:
                        pygame.mixer.music.stop()
                        global zvuk
                        zvuk = False
                    if 750 <= pos[0] <= 850 and 300 <= pos[1] <= 400:
                        pygame.mixer.music.play(-1)
                        zvuk = True
                    if 10 <= pos[0] <= 110 and 10 <= pos[1] <= 110:
                        screen5.fill(pygame.Color(117, 187, 253))
                        running5 = False
                        main()

            all_sprites5.draw(screen5)
            pygame.display.flip()
        pygame.quit()




def main():
    pygame.init()
    global zvuk
    if zvuk:
        pygame.mixer.music.load('data\muz0.mp3')
        pygame.mixer.music.play(-1)
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color(117,187,253))
    pygame.display.flip()
    running = True


    ra = load_image("rad1.png", 800, 500)
    r = pygame.sprite.Sprite(all_sprites)  # радуга
    r.image = ra
    r.rect = r.image.get_rect()
    r.rect.x = 100
    r.rect.y = 300

    rada = load_image("pict1.png", 200, 100)
    rad = pygame.sprite.Sprite(all_sprites)  # облако начать
    rad.image = rada
    rad.rect = rad.image.get_rect()
    rad.rect.x = 400
    rad.rect.y = 100

    obla = load_image("pict12.png", 200, 100)
    obl = pygame.sprite.Sprite(all_sprites)  # облако меню
    obl.image = obla
    obl.rect = obl.image.get_rect()
    obl.rect.x = 100
    obl.rect.y = 250

    obla1 = load_image("pict13.png", 200, 100)
    obl1 = pygame.sprite.Sprite(all_sprites)  # облако уровни
    obl1.image = obla1
    obl1.rect = obl1.image.get_rect()
    obl1.rect.x = 700
    obl1.rect.y = 250


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 400 <= pos[0] <= 600 and 100 <= pos[1] <= 200:
                    nach = Lavel1()
                if 100 <= pos[0] <= 300 and 250 <= pos[1] <= 350:
                    menu = Menu()
                if 700 <= pos[0] <= 900 and 250 <= pos[1] <= 350:
                    urov = Urov()


        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()