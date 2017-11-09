# adjust_run_and_action.py : regulate run speed and action speed as well

import random
import json
from pico2d import *

running = None

class Field:
    def __init__(self):
        self.image = load_image('background30M.bmp')

    def draw(self):
        self.image.draw(480, 136)


class Boy:

    # fill here

    PIXEL_PER_METER = (10.0/0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM=(RUN_SPEED_KMPH*1000/60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS=(RUN_SPEED_MPS*PIXEL_PER_METER)

    #TIME_PER_ACTION =0.5
    #ACTION_PER_TIME = 1.0/TIME_PER_ACTION
    #FRAMES_PER_ACTION =8

    font = None

    image = None

    LEFT_RUN, RIGHT_RUN = 0, 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = random.randint(0, 7)
        self.total_frames = 0.0
        self.dir = 1
        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')
        if(Boy.font) == None:
            Boy.font = load_font('ENCR10B.TTF', 16)


    def update(self, frame_time):
        distance = Boy.RUN_SPEED_PPS * frame_time
        self.total_frames += 1.0
        self.frame = (self.frame +1) % 8
        self.x += (self.dir * distance)

        if self.x > 960:
            self.dir = -1
            self.x =960
            self.state = self.LEFT_RUN
            print("Change Time: %f, Total Frames: %d"%(get_time(),self.total_frames))
        elif self.x < 0:
            self.dir =1
            self.x =0
            self.state =self.RIGHT_RUN
            print("Change Time: %f, Total Frames: %d" % (get_time(),self.total_frames))
        pass


    def draw(self):
        Boy.font.draw(self.x -40, self.y + 50,'Time: %3.2f' % get_time(),(255,255,0))
       # self.image.opacify(random.random())
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

class Bird:

    # fill here

    PIXEL_PER_METER = (10.0/0.3)
    FLY_SPEED_KMPH = 60.0#60km/h=500pixel/s
    FLY_SPEED_MPM=(FLY_SPEED_KMPH*1000/60.0)
    FLY_SPEED_MPS = (FLY_SPEED_MPM/60.0)
    FLY_SPEED_PPS=(FLY_SPEED_MPS*PIXEL_PER_METER)

    #TIME_PER_ACTION =0.5
    #ACTION_PER_TIME = 1.0/TIME_PER_ACTION
    #FRAMES_PER_ACTION =8

    font = None

    image = None

    LEFT_RUN, RIGHT_RUN = 0, 1

    def __init__(self):
        self.x, self.y = 0, 200
        self.frame = random.randint(0, 7)
        self.total_frames = 0.0
        self.dir = 1
        self.state = self.RIGHT_RUN
        if Bird.image == None:
            Bird.image = load_image('bird.png')


    def update(self, frame_time):
        distance = Bird.FLY_SPEED_PPS * frame_time
        self.total_frames += 1.0
        self.frame = (self.frame +1) % 8
        self.x += (self.dir * distance)

        if self.x > 960:
            self.dir = -1
            self.x =960
            print("Change Time: %f, Total Frames: %d"%(get_time(),self.total_frames))
        elif self.x < 0:
            self.dir =1
            self.x =0
            print("Change Time: %f, Total Frames: %d" % (get_time(),self.total_frames))
        pass


    def draw(self):

        self.image.clip_draw(0,0,128,128,self.x,self.y)


def handle_events(frame_time):
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



current_time = 0.0


def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def main():

    open_canvas(960, 272)

    global running
    global current_time

    god = Bird()
    hero = Boy()
    field = Field()

    running = True
    current_time = get_time()

    while running:

        # Game Logic
        frame_time = get_frame_time()
        handle_events(frame_time)
        hero.update(frame_time)
        god.update(frame_time)
        # fill here


        # Game Rendering
        clear_canvas()
        field.draw()
        hero.draw()
        god.draw()
        update_canvas()

        delay(0.03)


    close_canvas()


if __name__ == '__main__':
    main()