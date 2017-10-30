
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
    image = None

    run_frames=0

    LEFT_RUN,RIGHT_RUN,LEFT_STAND,RIGHT_STAND = 0,1,2,3

    def __init__(self):
        self.x,self.y = random.randint(100,700),90
        self.frame = random.randint(0,7)
        self.dir =1
        self.state =self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def update(self):
        self.frame=(self.frame+1 )%8
        self.handle_state[self.state](self)

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1
        if self.x < 0:
            self.state = self.RIGHT_RUN
            self.x = 0
        if self.run_frames == 100:
            self.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames+=1
        if self.stand_frames ==50:
            self.state =self.LEFT_RUN
            self.run_frames =0

    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames == 100:
            self.state = self.RIGHT_RUN
            self.stand_frames = 0

    def handle_right_stand(self):
        self.stand_frames += 1

        if self.stand_frames == 50:
             self.state = self.RIGHT_RUN
             self.run_frames = 0

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }

    def draw(self):
        self.image.clip_draw(self.frame*100,self.state*100,100,100,self.x,self.y)


class Ball:
    image = None

    def __init__(self):
        self.elapsedtime = 0
        self.bound = 0.55
        self.x,self.y = random.randint(50,750),600
        self.spd = random.randint(2,5)
        if Ball.image == None:
            Ball.image = load_image('ball.png')

    def update(self):
        self.y -= self.spd+(self.elapsedtime*3)
        self.elapsedtime=self.elapsedtime+1
        if self.y <= 62:
            self.y = 62
            self.spd=-((self.spd+(self.elapsedtime*3))*self.bound)
            if(self.spd > -8 ):
                self.spd=0
            self.elapsedtime=0

    def draw(self):
        self.image.draw(self.x,self.y)



#초기화 코드


open_canvas()

team = [Boy() for i in range(12)]
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

    delay(0.01)

#종료 코드
close_canvas()