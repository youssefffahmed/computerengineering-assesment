
#import the libraries that are needed
from roboticstoolbox import( Bicycle , RandomPath, VehicleIcon,RangeBearingSensor,LandmarkMap)
import matplotlib.pyplot as plt 
from math import atan2, pi
import matplotlib.image as mpimg
import numpy as np

#creating robot model and initialising its starting position
initial_pos = [-35, -35, 0]
anim = VehicleIcon('robo', scale=5)
veh = Bicycle(
    animation= anim,
    control= RandomPath,
    dim=50,
    x0=(initial_pos[0], initial_pos[1],0),
)

veh.init(plot=True)
#plotting the map and random obstacles and inputing the amount of random obstacles the user wants
obstacles= int(input("how many obstacles do you want on the map? (recommended 40-60) "))
map = LandmarkMap(obstacles, 50)
map.plot()

#inserting the maze image
image = mpimg.imread("mapp.png")
plt.imshow(image, extent = [-50,50,-50,50])

#making the goal
goal = [-35,35]
goal_marker_style = {
    'marker':'D',
    'markersize': 6,
    'color': 'b'
}

#plotting goal
plt.plot(goal[0], goal[1], **goal_marker_style)

# create array with points free of obstacle
goal_arr = [[-15,-20], [0, -2], [35, -5], [30, 20]]  
goal_arr.append(goal)
goal_arr.insert(0, initial_pos)

# splitting x and y points into seperate arrays
x_arr = [item[0] for item in goal_arr]  
y_arr = [item[1] for item in goal_arr]
#Creating sensor
sensor=RangeBearingSensor(robot=veh,map=map,animate=True)

#Printing sensor readings (to detect obstacles)
print('sensor readings: ', sensor.h(veh.x))
veh._animation.update(veh.x)
plt.pause(1)
 
#Defining function for avoiding obstacles
def detect_obstacles(readings):
    for i in sensor.h(veh.x):
        if (i[0] < 6 and abs(i[1]) < pi/4):
            veh.step(4,pi/3)
        else: 
            run = True 

#Defining function for moving to the target while avoiding the obstacles
def gotarget(goal):
    goal_heading=atan2(
            goal[1] - veh.x[1],
            goal[0] - veh.x[0]
        )
    detect_obstacles(sensor.h(veh.x))
    steer = goal_heading -veh.x[2]
    if steer>pi:
        steer =steer-2*pi
    veh.step(10, steer)
    veh._animation.update(veh.x)
    plt.pause(0.005)

#Defining function to make the robot avoid all obstacles and reach all goals as well    
def gocollision(goal):
    goal_heading=atan2(
            goal[1] - veh.x[1],
            goal[0] - veh.x[0]
        )
    detect_obstacles(sensor.h(veh.x))
    gotarget(goal)
    steer = goal_heading -veh.x[2]
    if steer>pi:
        steer =steer-2*pi
    veh.step(6, steer)
    veh._animation.update(veh.x)
    plt.pause(0.005)

#Loop that uses all three functions to escape the maze and avoids all obstacles
for n in range(len(goal_arr)-1):
    run = True
    goal = [x_arr[n+1], y_arr[n+1]]
    while (run):
        gotarget(goal)
        gocollision(goal)
        if((abs(goal[0]-veh.x[0]) <0.5) or (abs(goal[1] -veh.x[1]) < 0.5)):
            break
        veh._animation.update(veh.x)
        plt.pause(0.005)
plt.pause(1000) 
