import pygame, random, sys

pygame.init()
clock = pygame.time.Clock()

def new_game(count_bombs): 
    free_field = [[x,y] for y in range(0,16) for x in range(0,16)] 
    coordinat = []
    for x in range(count_bombs):
        rand_element = random.choice(free_field)
        coordinat.append(rand_element)
        free_field.remove(rand_element)
    count_bombs = bombs
    massive = [[0 for i in range(stolb)] for j in range(stroki)]
    massive_kletki = [[0 for i in range(stolb)] for j in range(stroki)]
    massive_test = [[0 for i in range(stolb)] for j in range(stroki)]       
    finded = False
    timer = False
    second = "000"
    for y in coordinat:
        massive[int(y[0])][int(y[1])] = 9

    for i in range(stroki):
        for j in range(stolb):
            if massive[i][j] == 0:
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < stroki and 0 <= y < stolb and massive[x][y] == 9:
                            massive[i][j] += 1
    for y in range(16):
        for x in range(16):
            if massive[y][x] == 0:
                picture = "d0.png"
            elif massive[y][x] == 1:
                picture = "d1.png"
            elif massive[y][x] == 2:
                picture = "d2.png"
            elif massive[y][x] == 3:
                picture = "d3.png"
            elif massive[y][x] == 4:
                picture = "d4.png"
            elif massive[y][x] == 5:
                picture = "d5.png"
            elif massive[y][x] == 6:
                picture = "d6.png"
            elif massive[y][x] == 7:
                picture = "d7.png"
            elif massive[y][x] == 8:
                picture = "d8.png"
            elif massive[y][x] == 9:
                picture = "bomb1.png"
            gr_sign.add(Sign((x * 35 + 23, y * 35 + 120), picture))
    for y in range(16):
        for x in range(16):
            gr_kletka.add(Kletka((x * 35 + 23, y * 35 + 120), "kletka1.png" ,0))
    btn1.win = 1
    return massive_kletki, massive, massive_test, count_bombs, timer, second
            
class Kletka(pygame.sprite.Sprite):
    def __init__(self, coord, picture, state):
        super().__init__()
        self.image = pygame.image.load(picture).convert()
        self.rect = self.image.get_rect(topleft = coord)
        self.state = state


class Sign(pygame.sprite.Sprite):
    def __init__(self, coord, picture):
        super().__init__()
        self.image = pygame.image.load(picture).convert()
        self.rect = self.image.get_rect(topleft = coord)

        
class Knop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("btn1.png").convert()
        self.rect = self.image.get_rect(center=(300, 60))
        self.state = 0
        self.win = 1

        
class Digit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.long_image = pygame.image.load("Digit1.png").convert()
        self.image = pygame.Surface((28,50))
        self.rect = self.image.get_rect(topleft = (x, y))

        
    def update_digit(self, number):
        if number == "0":
            self.image.blit(self.long_image, (0, 0), (28, 0, 28, 50))
        elif number == "1":
            self.image.blit(self.long_image, (0, 0), (56, 0, 28, 50))
        elif number == "2":
            self.image.blit(self.long_image, (0, 0), (84, 0, 28, 50))
        elif number == "3":
            self.image.blit(self.long_image, (0, 0), (112, 0, 28, 50))
        elif number == "4":
            self.image.blit(self.long_image, (0, 0), (140, 0, 28, 50))
        elif number == "5":
            self.image.blit(self.long_image, (0, 0), (168, 0, 28, 50))
        elif number == "6":
            self.image.blit(self.long_image, (0, 0), (196, 0, 28, 50))
        elif number == "7":
            self.image.blit(self.long_image, (0, 0), (224, 0, 28, 50))
        elif number == "8":
            self.image.blit(self.long_image, (0, 0), (252, 0, 28, 50))
        elif number == "9":
            self.image.blit(self.long_image, (0, 0), (280, 0, 28, 50))
        elif number == "-":
            self.image.blit(self.long_image, (0, 0), (0, 0, 28, 50))
            
        
        

window = pygame.display.set_mode((607, 704))
pygame.display.set_caption("Сапёр")
gr_kletka = pygame.sprite.Group()
gr_sign = pygame.sprite.Group()
background = pygame.image.load("pole1.png").convert()
btn1 = Knop()
stroki = 16
stolb = 16
bombs = 40

count_bombs = bombs
str_bomb = str(bombs).zfill(3)
press = False
timer = False
second = "000"
close_kletka = 256
digit_1 = Digit(33, 34)
digit_2 = Digit(61, 34)
digit_3 = Digit(89, 34)
clock1 = Digit(490, 34)
clock2 = Digit(518, 34)
clock3 = Digit(546, 34)
massive_kletki, massive,massive_test, count_bombs, timer, second = new_game(count_bombs)
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.MOUSEMOTION:
            if btn1.state == 1 and not (btn1.rect.collidepoint(pygame.mouse.get_pos())) and btn1.win == 1:
                btn1.state = 0
                btn1.image=pygame.image.load("btn1.png").convert()
            elif btn1.state == 1 and not (btn1.rect.collidepoint(pygame.mouse.get_pos())) and btn1.win == 2 and press == True:
                btn1.state = 3
                btn1.image = pygame.image.load("btn5.png").convert()
            elif btn1.state == 1 and not (btn1.rect.collidepoint(pygame.mouse.get_pos())) and btn1.win == 0:
                btn1.state = 2
                btn1.image = pygame.image.load("btn3.png").convert()
            elif btn1.state == 2 and btn1.rect.collidepoint(pygame.mouse.get_pos()) and btn1.win == 0 and press == True:
                btn1.state = 1
                btn1.image = pygame.image.load("btn4.png").convert()
            elif btn1.state == 3 and btn1.rect.collidepoint(pygame.mouse.get_pos()) and btn1.win == 2 and press == True:
                btn1.state = 1
                btn1.image = pygame.image.load("btn4.png").convert()
                
        if ev.type == pygame.MOUSEBUTTONUP:
            press = False
            if ev.button == pygame.BUTTON_LEFT:
                if btn1.rect.collidepoint(pygame.mouse.get_pos()):
                    if btn1.state == 1:
                        massive_kletki, massive, massive_test, count_bombs, timer, second=new_game(count_bombs)
                    btn1.state = 0
                    btn1.image = pygame.image.load("btn1.png").convert()
            if btn1.state == 1 and btn1.rect.collidepoint(pygame.mouse.get_pos()) and btn1.win == 0:
                btn1.state = 0
                btn1.image = pygame.image.load("btn1.png").convert()
                massive_kletki, massive,massive_test, count_bombs, timer, second = new_game(count_bombs)
                
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == pygame.BUTTON_RIGHT:
                if btn1.win == 1 and 23 < pygame.mouse.get_pos()[0]<583 and 120 < pygame.mouse.get_pos()[1] < 680:
                    coord = (pygame.mouse.get_pos()[1] - 120) // 35,(pygame.mouse.get_pos()[0] - 23) // 35
                    if massive_kletki[(pygame.mouse.get_pos()[1] - 120) // 35][(pygame.mouse.get_pos()[0] - 23) // 35] == 0:
                        for kl in gr_kletka:
                            if kl.rect.collidepoint(pygame.mouse.get_pos()):
                                state=kl.state
                                kl.kill()
                        if state == 0:
                            gr_kletka.add(Kletka((coord[1] * 35 + 23, coord[0] * 35 + 120), "flag.png", 1))
                            count_bombs -= 1
                        elif state == 1:
                            gr_kletka.add(Kletka((coord[1] * 35 + 23, coord[0] * 35 + 120), "quest.png", 2))
                            count_bombs += 1
                        elif state == 2:
                            gr_kletka.add(Kletka((coord[1] * 35 + 23, coord[0] * 35 + 120), "kletka1.png", 0))
            if ev.button == pygame.BUTTON_LEFT:
                press = True
                if btn1.win == 1:
                    if btn1.rect.collidepoint(pygame.mouse.get_pos()): 
                        btn1.image = pygame.image.load("btn4.png").convert()
                        btn1.state = 1
                    for kl in gr_kletka: 
                        if kl.rect.collidepoint(pygame.mouse.get_pos()):
                            if timer == False:
                                start = pygame.time.get_ticks() 
                            timer = True
                            if kl.state == 0: 
                                massive_kletki[(pygame.mouse.get_pos()[1] - 120) // 35][(pygame.mouse.get_pos()[0] - 23) // 35] = 1
                                if massive[(pygame.mouse.get_pos()[1] - 120) // 35][(pygame.mouse.get_pos()[0] - 23) // 35] == 0:
                                    coord = (pygame.mouse.get_pos()[1] - 120) // 35,(pygame.mouse.get_pos()[0] - 23) // 35
                                    for i in range(coord[0] - 1, coord[0] + 2):
                                        for j in range(coord[1] - 1, coord[1] + 2):
                                            for kl in gr_kletka:
                                                if kl.rect.topleft == (j * 35 + 23, i * 35  +120):
                                                    kl.kill()
                                            if 0 <= i < 16 and 0 <= j< 16: 
                                                massive_kletki[i][j] = 1
                                    massive_test[coord[0]][coord[1]] = 1
                                    finded = True
                                    while finded:
                                        finded = False
                                        for i in range(stroki):
                                            for j in range(stolb):
                                                if massive_kletki[i][j] == 1 and massive[i][j] == 0 and massive_test[i][j] == 0:
                                                    finded = True
                                                    for m in range(i - 1, i + 2):
                                                        for n in range(j - 1,j + 2):
                                                            for kl in gr_kletka:
                                                                if kl.rect.topleft == (n * 35 + 23, m * 35 + 120):
                                                                    kl.kill()
                                                            if 0 <= m < 16 and 0 <= n < 16: 
                                                                massive_kletki[m][n] = 1
                                                                massive_test[i][j] = 1

                                    sum_flag = 0                    
                                    for x in gr_kletka:
                                        if x.state == 1:
                                            sum_flag += 1
                                    count_bombs = bombs-sum_flag
                                elif massive[(pygame.mouse.get_pos()[1] - 120) // 35][(pygame.mouse.get_pos()[0] - 23) // 35] == 9:
                                    btn1.image = pygame.image.load("btn3.png").convert()
                                    btn1.state = 2
                                    btn1.win = 0
                                    timer = False
                                    for x in gr_sign:
                                        if x.rect.collidepoint(pygame.mouse.get_pos()):
                                            bomb_rect = x.rect[0], x.rect[1]
                                            x.kill()
                                            gr_sign.add(Sign((bomb_rect), "bomb2.png"))                         
                                    for i in range(stroki):
                                        for j in range(stolb):
                                            if massive[i][j] == 9:
                                                for x in gr_kletka:
                                                    if x.rect[:2] == [j*35+23, i*35+120]:
                                                        x.kill()
                                if btn1.win == 1:
                                    summa = 0
                                    for i in massive_kletki:
                                        summa += i.count(0)
                                    if summa == bombs:
                                        btn1.image = pygame.image.load("btn5.png").convert()
                                        btn1.wi = 2
                                        btn1.state = 3 
                                        timer = False
                                        for x in gr_kletka:
                                            x.image = pygame.image.load("flag.png").convert()   
                                for kl in gr_kletka:
                                    if kl.rect.collidepoint(pygame.mouse.get_pos()):
                                        kl.kill()
            
                else:
                    if btn1.rect.collidepoint(pygame.mouse.get_pos()): 
                        btn1.image = pygame.image.load("btn4.png").convert()
                        btn1.state = 1
    if timer:
        second = str((pygame.time.get_ticks()-start) // 1000).zfill(3)
    window.blit(background, (0, 0))
    gr_sign.draw(window)
    gr_kletka.draw(window)
    window.blit(btn1.image,btn1.rect)
    str_bomb=str(count_bombs).zfill(3)
    clock1.update_digit(second[-3:-2])
    clock2.update_digit(second[-2:-1])
    clock3.update_digit(second[-1:])
    digit_1.update_digit(str_bomb[:1])
    digit_2.update_digit(str_bomb[1:2])
    digit_3.update_digit(str_bomb[2:])
    window.blit(digit_1.image ,digit_1.rect)
    window.blit(digit_2.image, digit_2.rect)
    window.blit(digit_3.image ,digit_3.rect)
    window.blit(clock1.image, clock1.rect)
    window.blit(clock2.image, clock2.rect)
    window.blit(clock3.image, clock3.rect)
    pygame.display.update()
    clock.tick(50)
