#https://leetcode.com/problems/robot-bounded-in-circle/

def isRobotBounded(instructions):
    x,y=0,0
    dx=0
    dy=1
    for i in instructions:
        if i=="L":
            dx, dy=-dy, dx
        if i=="R":
            dx, dy= dy, -dx
        if i=="G":
            x+=dx
            y+=dy
    return (x,y)==(0,0) or (dx,dy)!=(0,1)
