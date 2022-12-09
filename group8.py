
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
