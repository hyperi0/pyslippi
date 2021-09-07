import math
import slippi
from slippi import Game

game = Game('./ex-game.slp')

myPort = 0 if game.metadata.players[0].netplay.code == "DAB#823" else 1
theirPort = (myPort+1)%2
findState = slippi.id.ActionState.ATTACK_DASH
flag = True # if state should be recorded (new action)
foundFrames = []

def frameTime(frame):
    return([math.floor(frame/3600),math.floor((frame%3600)/60)])

for frame in game.frames:
    state = frame.ports[theirPort].leader.post.state

    if flag:
        if state == findState:
            foundFrames.append(frame.index)
            flag = False
    else:
        if state != findState:
            flag = True

for frame in foundFrames:
    time = frameTime(frame)
    print(f'{time[0]}:{time[1]}')
