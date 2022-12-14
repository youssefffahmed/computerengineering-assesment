# Aim of the Code
The aim of this code is to start the robot (robo) at a certain position and make this robot navigate through walls and random obstacles to escape a maze by reaching a goal position (the blue diamond).

# Requirements to use this code
Most importantly install python 3.6 or newer, then preferably use Ubuntu(64-bit) 18.04 as the oparting system (more reliable). Then you should install Oracle VM Virtual Box and Roboticstoolbox to import all the libraries used. This code was made using VS code but an alternate program that can use python could be used if wanted.

# What The Code Does

## How It Works (High-Level Language)
Robo is given an initial postion and an end position, he then passes through specified points that have been already selected. Throughout his path if he finds an obstacle that is closer than 4 points away the sensor will pick it up and he will turn at a 60 degree angle (pi/3 in radians) move 4 steps to the left then continue his path to the target.

## How It Works (Low Level Language)
First we have to make the robot. To do this we must first download an image we want to be the robot and save it as a png, in this instance we called him Robo. We then imported the needed libraries to make the image come to life and make it an actuaal robot that moves as shown in he code below.

anim = VehicleIcon('robo', scale=5)

veh = Bicycle(

    animation= anim,

    control= RandomPath,

    dim=50,

    x0=(initial_pos[0], initial_pos[1],0),

    )
  
### Meet Robo
![Meet Robo!](https://user-images.githubusercontent.com/114486423/206735543-c5ffe806-c18b-43d2-adc8-1cfed8ede85a.png)


We then plotted the map and gave the user the option to insert however many obstacles they want and imported an image of a maze to better simulate the code. We then put the free points available that the robot can pass through without colliding with the walls of the maze into an array [goal_arr] and made a for loop so that we can make the robot pass through these points. In the for loop we had 3 funtions in order to make Robo avoid the obstacles he meets, move along the specified paths and also make it out of the maze.

### Function 1            
`detect_obstacles` This function reads the sensor readings (made earlier in the code in line 49) and creates a For loop to make the robot turn 60 degrees and move 4 steps so that it avoids the obstacles.

### Function 2
`gotarget` This function is responsible for making the robot move to the target by calculating the steer angle and uses a set velocity to make the robot move to the target, it is also a nested funtion because it includes `detect_obstacles` inside it to simultaneously avoid the obstacles.

### Function 3
`gocollision` This function is responsible for make the robot move to the specified target after avoiding the obstacle. Again this is a nesteed funvtion including both `detect_obstacles` and `gotarget` , it was made because there was en error that made Robo avoid the obstacles but not go to the specified targets points.

They are then all then used in a For loop `for n in range(len(goal_arr)-1)` to use the functions and breaks the loop only when Robo reaches his end goal (the blue diamond) 

# Flowchart
Thie flowchart shows our throught process while brainstorming the steps of the code and writing the outcome of each process done by the robot.
# <img width="405" alt="Flowchart" src="https://user-images.githubusercontent.com/114486423/206733963-da906261-0e0c-4084-a40f-d8f9f7079115.png">

# Collaboration and Contribution of Team Members
No specific task was assigned to each member as most of the time we found it best to brainstorm together and write the code together. The first half of the code was done by both of us which included importing the libraries needed, creating the robot,plotting the map and goal, creating the array of points for the path and setting up the rangebearing sensor. As for the second half, the first 2 functions were done by Youssef Awadllah and the third function and the for and while loop were done by Omar Kazem, but the whole process involved both team members.

# Critical Assesment Of Limitations
In this code there is a room for improvement just like anything else in the world. For example; it has a set target and a set starting position because the path is set on an array of points `goal_arr[]`, it could be altered to make these variables rather than constant. It also does steer a bit too much sometimes while avoiding obstacles. The maze is also only an image and could be improved to be set as an obstacle and Robo would automatically avoid it. Robo also still does not understand how to steer and move in a direction that would be the best path to be taken to the goal. This is not much of a limitation but Robo's movement is also not the smoothest. Any helpful critisism is also much appreciated.

# Real Life Applications
Robo could be used in a warehouse where he knows the map exactly and picks up packages from one place in the warehouse to another while avoiding any contact with people working and any other obstacles he might face. He could also be programmed to become an autonomous vehicle that can navigate around a whole city with a satellite map.

# Results
The results were perfect other than the limitations described above. The robot reached the target point while moving through the maze and avoiding all obstacles. These images show the initial position of Robo, Robo during the process and the final position it reached.

<img width="300" alt="Initial" src="https://user-images.githubusercontent.com/114486423/206741465-10351607-4359-47e6-a6f0-c17c32b2f068.png">
<img width="300" alt="During" src="https://user-images.githubusercontent.com/114486423/206741514-1875a9c2-4e0b-4ecd-b9cc-e7ce0b9f4430.png">
<img width="300" alt="Final" src="https://user-images.githubusercontent.com/114486423/206741563-9c2f82d2-67d0-4cb6-8c05-96994960d55b.png">



