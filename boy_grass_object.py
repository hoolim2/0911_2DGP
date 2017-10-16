
import random
from pico2d import *

# 게임 오브젝트 클래스의 정의를 여기에


def handle_events():
    global running
    events = get_events()
    for evevt in events:
        if evevt.type == SDL_QUIT:
            running = False
        elif evevt.type == SDL_KEYDOWN and evevt.key == SDLK_ESCAPE:
            running = False


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)


class Boy:
    def __init__(self):
        self.x,self.y = random.randint(100,500),90
        self.frame = random.randint(0,7)
        self.image = load_image('boy.png')

    def update(self):
        self.frame = (self.frame +1)% 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)


class Ball:
    def __init__(self):
        self.elapsedtime = 0
        self.x,self.y = random.randint(50,750),600
        self.spd = random.randint(2,5)
        self.image = load_image('ball.png')
        self.down=0

    def update(self):
        self.y -= self.spd+(self.elapsedtime*3)
        self.elapsedtime=self.elapsedtime+1
        if self.y <= 62:
            self.spd=-40
            self.elapsedtime=0

    def draw(self):
        self.image.draw(self.x,self.y)

#초기화 코드


open_canvas()

team = [Boy() for i in range(11)]
ball_group = [Ball() for i in range(20)]
grass = Grass()

running = True

#게임 루프 코드

while running:
    handle_events()

    for boy in team:
        boy.update()

    for ball in ball_group:
        ball.update()

    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()

    for ball in ball_group:
        ball.draw()

    update_canvas()

    delay(0.02)

#종료 코드
close_canvas()