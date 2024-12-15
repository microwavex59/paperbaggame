import pgzero
import time, random
WIDTH=800
HEIGHT=600
CENTER=(400,300)
FINAL_LEVEL=6
START_SPEED=10
ITEMS={"bag","bottle","chips","battery"}
game_over=False
game_complete=False
current_level=1
items=[]
animations=[]

def draw():
    screen.clear()
    screen.blit("background",(0,0))