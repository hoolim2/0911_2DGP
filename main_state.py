import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

pause = None
boy = None
grass = None
font = None
pausecheck=False



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def enter():
    global boy,grass
    boy = Boy()
    grass = Grass()
    pass


def exit():
    global boy,grass
    del(boy)
    del(grass)
    del(pause)
    pass


def pause():
    global pausecheck
    pausecheck = True
    pause = Pause()
   # game_framework.running=False
    if pausecheck == True:
        clear_canvas()
        grass.draw()
        boy.draw()
        pause.draw()
        update_canvas()
        delay(0.5)
        clear_canvas()
        grass.draw()
        boy.draw()
        update_canvas()
        delay(0.5)

    pass


def resume():
    global pausecheck
    pausecheck = False
    pass


def handle_events():
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(PauseState)
#       elif event.type == SDL_KEYDOWN and event.key == SDLK_p and pausecheck == False:
#            pause()
#       elif event.type == SDL_KEYDOWN and event.key == SDLK_p and pausecheck == True:
#           resume()
    pass


def update():
    if(pausecheck == False):
        boy.update()
    if(pausecheck == True):
        pause()
    pass


def draw():
    if (pausecheck == False):
        clear_canvas()
        grass.draw()
        boy.draw()
        update_canvas()
    pass





