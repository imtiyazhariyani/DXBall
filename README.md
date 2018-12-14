# DXBall
Introduction to Computer Science Final Project

Imtiyaz Hariyani (ieh211@nyu.edu)

Fall 2018

New York University Abu Dhabi

## **Project Description**
 I intend to recreate an Arcade Game from the 90s called DX-Ball. It is a classic ball and paddle single-player game where the player controls the paddle at the bottom of the screen (on the x-axis) using the mouse. The ball is then deflected off to hit color-patterned blocks without letting the ball fall below the paddle. The player gets four lives before the game ends. The aim is to score as many points as possible by hitting all the blocks and leveling up. There are several power-ups/downs, including Kill Paddle, Thru Brick, Extra Life etc. that fall from the colored blocks and can be collected using the paddle to race through the game. My aim is to build the same arcade game with improved graphics and design and implement a modifiable, non-hard coded interface that includes difficulty level (depending on speed, number of power-ups etc.). I will be working alone on this project.

## **Instructions**
Installation & Running the Program:
You need to have the latest version of Processing installed on your computer to run this game. Make sure to download all files contained in this repository. Open the .pyde file and click the 'play' button to run the code. 

General:
Upon starting, the player may choose to play the game or view high scores by clicking on the relevant menu option. The player will start by left clicking the mouse to release the ball from the paddle, and control the x-coordinate of the paddle using the mouse (or trackpad). The aim is to score as many points as possible with the four given lives, with there being infinitely many levels, each with increasing speed in the vertical direction. The ball deflects off the sides and top of the screen, as well as off a tile in the vertical direction. A life is lost if the ball falls below the paddle. The ball will then be returned to the paddle, allowing the player to click the mouse and release the ball once again. 

Levels & Scoring:
The game consists of infinitely many levels and only ends when the player loses all four lives. 10 points are scored when the ball hits a tile unless otherwise mentioned below.

Level 1 - The "V" fires up if a single tile in the V is hit.
Level 2 - Tiles in the "V" score 50 points per tile.
Level 3 - Tiles in the "V" are blocked and the ball deflects off them, without scoring any points.
Level 4 & above - All tiles score 10 points; the pattern is only for aesthetics.

Power-ups/downs: 
A power-up/down is randomly contained within some tiles and will fall once the tile is hit by the ball. If caught using the paddle, the functionality of the power-up/down will be implemented. This game contains three different kinds of power-ups/downs:
1. Kill Paddle - The player loses a life and advances to the next level; however 500 points are earned.
2. Thru Brick - Instead of bouncing back when the ball hits the tile, it goes through in the vertical direction.
3. Extra Life - The player gains an extra life.


## **Code**
General:
The code makes use of object-oriented programming with a different class for each object in the game, including the ball, paddle, board, tiles, each of the power-ups and the main game. Most parameters can be changed 

Components used to build the code:
Royalty free music and images from the internet were used to build the code, besides in-built Processing features.

## **Credits & Acknowledgement**
I would like to thank Professor Yasir Zaki and Mr Khalid Mengal for their support and guidance.

This game is based on DX-Ball, a project by Michael P. Welch (1996-98). 

## **Disclaimer**
The game should not be distributed for commercial purposes.

