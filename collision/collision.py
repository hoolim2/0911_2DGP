from pico2d import *

import game_framework


from boy import Boy # import Boy class from boy.py
from ball import Ball, BigBall
from grass import Grass



name = "collision"

boy = None
balls = None
big_balls = None
grass = None
brick=None

brickX=0

class Brick:
    image = None;

    def __init__(self):
        self.x, self.y = 200,200
        self.dir=200
        if Brick.image == None:
            Brick.image = load_image('brick180x40.png')

    def update(self, frame_time):
        global brickX
        self.x += frame_time * self.dir
        brickX=frame_time * self.dir
        if(self.x >600):
            self.x = 600
            self.dir=-200
        elif(self.x <100 ):
            self.x = 100
            self.dir = 200
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 90 , self.y -20, self.x +90, self.y +20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


def create_world():
    global boy, grass, balls, big_balls,brick
    boy=Boy()
    big_balls=[BigBall() for i in range(10)]
    balls =[Ball() for i in range(10)]
    balls = big_balls+balls
    grass = Grass()
    brick = Brick()




def destroy_world():
    global boy, grass, balls, big_balls

    del(boy)
    del(balls)
    del(grass)
    del(big_balls)
    del(brick)



def enter():
    open_canvas()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                boy.handle_event(event)



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a>right_b: return False
    if right_a<left_b: return False
    if top_a<bottom_b: return False
    if bottom_a>top_b: return False

    return  True


def UPcollide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return  True


def update(frame_time):
    global brickX
    boy.update(frame_time)
    brick.update(frame_time)
    if UPcollide(brick, boy):
        brickcollide=True
        stoprange = 260
        boy.stop(stoprange, brickX,brickcollide)
    if UPcollide(grass, boy):
        brickcollide = False
        stoprange = 90
        boy.stop(stoprange, brickX,brickcollide)

    for ball in balls:
        ball.update(frame_time)

    for ball in balls:
        pass

    for ball in balls:
        if collide(brick,ball):
            pass

    for ball in big_balls:
        if UPcollide(brick,ball):
            stoprange=240
            ball.stop(stoprange,brickX)
        if UPcollide(grass,ball):
            stoprange=70
            ball.stop(stoprange,brickX)



def draw(frame_time):
    print(brickX)
    clear_canvas()
    grass.draw()
    boy.draw()
    brick.draw()
    for ball in balls:
        ball.draw()

    grass.draw_bb()
    boy.draw_bb()
    for ball in balls:
        ball.draw_bb()

    delay(0.01)

    update_canvas()






