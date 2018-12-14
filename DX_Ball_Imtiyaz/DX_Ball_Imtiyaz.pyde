#This game serves as the Final Project for Imtiyaz Hariyani, Introduction to Computer Science, Fall 2018.

add_library('minim')
import os
from random import randint
path=os.getcwd()
player=Minim(this)

#Dimensions of the screen
WIDTH=1675
HEIGHT=960

#Starting Parameters
SPEED=10
PWIDTH=184

class Paddle:
    """This class defines parameters and attributes of the paddle, which the user will control with a mouse to bounce the ball off its surface"""
    def __init__(self,w,h,pw):
        self.w=w
        self.h=h
        self.paddle=loadImage(path+"/images/paddle.jpg")
        self.paddleh=self.h-120
        self.paddleX=None
        self.paddleWidth=pw
        self.imageCount=12
        self.frames=0
        self.imagelist=[]
        for num in range(self.imageCount):
            self.imagelist.append(loadImage(path+"/images/electricity/"+str(num)+".jpeg"))
    
    def display(self,x):
        #Condition to make sure paddle is entirely on screen
        if x in range(0,self.paddleWidth/2):
            self.paddleX=(self.paddleWidth/2)
        elif x in range(self.w-self.paddleWidth/2,self.w):
            self.paddleX=self.w-self.paddleWidth/2
        else:
            self.paddleX=x
       
        #Display electricity animation when ball is on paddle
        if dxb.grabpaddle and dxb.lives != 0:
            b.x=p.paddleX
            frameRate(18)
            self.frames=(self.frames+1)%self.imageCount
            for i in range(self.imageCount):
                image(self.imagelist[self.frames],p.paddleX-72,p.paddleh-48,142,71) 
        else:
            frameRate(60)
        
        #Display paddle image
        image(self.paddle,self.paddleX-self.paddleWidth/2,self.paddleh,self.paddleWidth,38)
                    
class Ball:
    """The Ball class defines parameters and attributes of the ball, including its position and velocity"""
    def __init__(self,x,y,s):
        self.x=x
        self.vx=0
        self.y=y
        self.vy=0
        self.speed=s
        self.frames=0
        self.imageCount=79
        self.imagelist=[]
        self.bounce=player.loadFile(path+"/music/bounce.mp3")
        for num in range(self.imageCount):
            self.imagelist.append(loadImage(path+"/images/ball_edited2/frame_"+str(num)+"_delay-0.05s.png"))
        
    def display(self):
        #Conditions to bounce the ball back into play
        if self.x >= p.w:
            self.vx=-self.vx
            self.bounce.rewind()
            self.bounce.play()
        elif self.x <= 0: 
            self.vx=-self.vx
            self.bounce.rewind()
            self.bounce.play()
        elif self.y <= 0:
            self.vy=-self.vy
            self.bounce.rewind()
            self.bounce.play()
        
        #Constantly update the ball's position        
        self.x+=self.vx
        self.y+=self.vy
        
        #Display the ball image 
        self.frames=(self.frames+1)%self.imageCount
        for i in range(self.imageCount):
            image(self.imagelist[self.frames],self.x-20,self.y-25,30,30)                                                                                                                                                                                                                                                                                                                            

class Board:
    """The Board class helps create a board of tiles, which is stored in a 1D list"""
    def __init__ (self):
        self.tiles=[]
        self.row=9
        self.column=16
        self.totaltiles=self.row*self.column
        for r in range(self.row):
            for c in range(self.column):
                self.tiles.append(Tile(r,c))
        
    def display(self):
        for t in self.tiles:
            if t.visible:
                t.display()

class Tile:
    """The Tile class is used to separate the attributes of the tiles from the rest of the game"""
    def __init__(self,r,c):
        self.r=r
        self.c=c
        self.w=75
        self.h=50
        self.x=self.c*self.w+240
        self.y=self.r*self.h+140
        self.visible=True
        self.powerUp=False
        self.kill=False
        self.extralife=False
        self.thrubrick=False
        self.explosion=player.loadFile(path+"/music/explosion.mp3")
        #self.tilehit=player.loadFile(path+"/music/tile.mp3")
        
    def isBallOn(self,ballx,bally):
        #Method to check if the ball's coordinates match those of a tile
        if self.x <= ballx <= self.x+self.w and self.y <= bally <= self.y+self.h:
            return True
        return False
    
    def getTile(self,x,y):
        #Method to return the identity of the tile based on the row and column
        for tile in board.tiles:
            if tile.c == x and tile.r == y:
                return tile
        return None
                                    
    def display(self):
        #Method to display each tile based on several conditions, including whether it is hidden and the pattern of the board
        if self.isBallOn(b.x,b.y):
            #Condition to check for the 'V' pattern and blast those tiles in level 1
            if (self.c-self.r==0 or self.r+self.c==15) and dxb.level==1:
                for r in range(board.row):
                    for c in range(board.column):
                        if (c-r==0 or r+c==15):
                            ntile=self.getTile(c,r)
                            ntile.visible=False
                            dxb.score+=10 
                            self.explosion.rewind()
                            self.explosion.play()
                            board.totaltiles-=1
                            dxb.checkLevel()
            #Condition to check for the same 'V' pattern in level 3 and fix the tiles permanently
            elif (self.c-self.r==0 or self.r+self.c==15) and dxb.level==3:
                b.bounce.rewind()
                b.bounce.play()
            
            #Extra points for hitting the 'V' in level 2
            elif (self.c-self.r==0 or self.r+self.c==15) and dxb.level==2:
                #self.tilehit.rewind()
                #self.tilehit.play()
                self.visible=False
                dxb.score+=50
                board.totaltiles-=1
                dxb.checkLevel()
            
            #Otherwise simply hide the tile and add to the score for the remaining tiles at all levels
            else:
                #self.tilehit.rewind()
                #self.tilehit.play()
                self.visible=False
                dxb.score+=10
                board.totaltiles-=1
                dxb.checkLevel()
                
            #Rebound the ball in the y-direction from the tile unless the Thru Brick power up is applied    
            if not dxb.thrubrick:
                b.vy=-b.vy
        
        #If ball does not hit the tile, then the tile must be displayed
        else:
            #Different patterns for the different levels
            if dxb.level == 1:
                if self.c-self.r==0 or self.r+self.c==15:
                    fill(255,randint(120,223),0)
                    rect(self.x,self.y,75,50,17)
                else:
                    fill(220,20,60)
                    rect(self.x,self.y,75,50,7)
            elif dxb.level == 2:
                if self.c-self.r==0 or self.r+self.c==15:
                    fill(255,randint(0,255),255)
                    rect(self.x,self.y,75,50,17)
                else:
                    fill(0,164,180)
                    rect(self.x,self.y,75,50,7)
            elif dxb.level >= 3:
                if self.c-self.r==0 or self.r+self.c==15:
                    fill(120,120,120)
                    rect(self.x,self.y,75,50,17)
                else:
                    fill(120,randint(120,240),255)
                    rect(self.x,self.y,75,50,7)

class PowerUp:
    """Class to define the common features of a powerup object""" 
    def __init__(self,img,w,h,x,y,r,c):
        self.img = loadImage(path+"/images/"+img)
        self.w=w
        self.h=h
        self.x=x
        self.y=y
        self.r=r
        self.c=c
        self.vy=8
        self.coin=player.loadFile(path+"/music/coin.mp3")
        self.tilehit=player.loadFile(path+"/music/tile.mp3")
    
    def getTile(self,x,y):
        #Method to return the identity of the tile based on the row and column
        for tile in board.tiles:
            if tile.c == x and tile.r == y:
                return tile
        return None
    
    def update(self):
        self.y+=self.vy
    
    def action(self):
        pass
    
    def display(self):
        tile=self.getTile(self.c,self.r)
        if not tile.visible and tile.powerUp:
            self.update()
            image(self.img,self.x,self.y,self.w,self.h)
            if self.x in range(p.paddleX-p.paddleWidth/2,p.paddleX+(p.paddleWidth/2)+1) and self.y in range (p.paddleh-self.vy,p.paddleh):
                self.action()
            elif self.y>p.h:
                self.delete()
                
class ExtraLife(PowerUp):
    """Inherited class to define the features of the extra life power up"""
    def __init__(self,img,w,h,x,y,r,c):
        PowerUp.__init__(self,img,w,h,x,y,r,c)
            
    def action(self):
        self.coin.rewind()
        self.coin.play()
        dxb.lives+=1
        self.delete()
        
    def delete(self):
        dxb.extralives.remove(self)
        del self
    
class Kill(PowerUp):
    """Inherited class to define the features of the kill/levelup power up"""
    def __init__(self,img,w,h,x,y,r,c):
        PowerUp.__init__(self,img,w,h,x,y,r,c)

    def action(self):
        dxb.powerDown.rewind()
        dxb.powerDown.play()
        dxb.score+=500
        dxb.lives-=1
        board.totaltiles=0
        dxb.checkLevel()
        
    def delete(self):
        dxb.kills.remove(self)
        del self

class Thrubrick(PowerUp):
    """Inherited class to define the features of the thrubrick power up"""
    def __init__(self,img,w,h,x,y,r,c):
        PowerUp.__init__(self,img,w,h,x,y,r,c)

    def action(self):
        dxb.thrubrick=True
        self.tilehit.rewind()
        self.tilehit.play()
        self.delete()
        
    def delete(self):
        dxb.thrubricks.remove(self)
        del self
    
class DXBall:
    """This is the main game class from where the game is controlled for levels, scores, lives, and other action"""
    def __init__(self):
        self.mode="MENU"
        self.backimage=loadImage(path+"/images/background.jpg")
        self.name=""
        self.highscore = {}
        self.nums = []
        self.names = []
        self.highscoreimg=loadImage(path+"/images/highscoreimg.png")
        self.pause=False
        self.lives=4
        self.grabpaddle=True
        self.level=1
        self.score=0
        self.menuMusic = player.loadFile(path+"/music/menu.mp3")
        self.gameTrack = player.loadFile(path+"/music/gametrack.mp3")
        self.gameOver = player.loadFile(path+"/music/gameover.mp3")
        self.powerDown = player.loadFile(path+"/music/powerdown.mp3")
        self.boink = player.loadFile(path+"/music/boink.mp3")
        self.menuMusic.play()
        self.menuimagelist=[]
        self.ballimagelist=[]
        self.frames1=0
        self.numFramesmenu=43
        self.frames2=0
        self.numFramesball=10
        for num in range(self.numFramesmenu):
            self.menuimagelist.append(loadImage(path+"/images/menu/frame_"+str(num)+"_delay-0.1s.png"))
        for num in range(self.numFramesball):
            self.ballimagelist.append(loadImage(path+"/images/menuball/frame_0"+str(num)+"_delay-0.1s.png"))
        
        self.thrubrick=False
        self.kills=[]
        self.extralives=[]
        self.thrubricks=[]
        self.numkills=2
        self.numextralives=2
        self.numthrubricks=2
        self.assignPowerUps()
        self.appendPowers()
        
    def appendPowers(self):   
        self.kills=[]
        self.extralives=[]
        self.thrubricks=[] 
        for tile in board.tiles:
            if tile.kill:
                self.kills.append(Kill("kill.png",60,60,tile.x,tile.y,tile.r,tile.c))
            if tile.extralife:
                self.extralives.append(ExtraLife("+1.png",60,60,tile.x,tile.y,tile.r,tile.c))
            if tile.thrubrick:
                self.thrubricks.append(Thrubrick("thrubrick.png",60,60,tile.x,tile.y,tile.r,tile.c))

    def game(self,paddleX):
        if self.mode == "MENU":
            frameRate(30)
            #Display menu images
            self.frames1=(self.frames1+1)%self.numFramesmenu
            for i in range(self.numFramesmenu):
                image(self.menuimagelist[self.frames1],575,130) 
            
            self.frames2=(self.frames2+1)%self.numFramesball   
            for i in range(self.numFramesball):
                image(self.ballimagelist[self.frames2],p.w-300,70) 
        
        elif self.mode == "PLAY":
            #Display images of paddles at the top right to show remaining lives
            for i in range(self.lives-1):
                image(p.paddle,p.w-300+i*50,35,31,7)
              
            #Display the score on the top left      
            fill(255)
            textSize(32)
            text(str(dxb.score),75,45)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            
            #Play the game sound track      
            self.gameTrack.play()
            
            for e in dxb.extralives:
                e.display()
            for k in dxb.kills:
                k.display()
            for t in dxb.thrubricks:
                t.display()
            
            #Condition to test whether ball is in range of paddle
            if b.x in range(p.paddleX-p.paddleWidth/2,p.paddleX+(p.paddleWidth/2)+1) and b.y in range (p.paddleh-b.speed,p.paddleh):
                #Condition to check if grab paddle is turned on
                if not self.grabpaddle:
                    #Conditions to determine position of paddle where ball hits and determine velocity accordingly
                    if b.x in range(p.paddleX-p.paddleWidth/2,p.paddleX-75):
                        b.y=p.paddleh-1
                        b.vy=-b.vy
                        b.vx=-20
                    elif b.x in range(p.paddleX-75,p.paddleX-55):
                        b.y=p.paddleh-1
                        b.vy=-b.vy
                        b.vx=-14
                    elif b.x in range(p.paddleX-55,p.paddleX-18):
                        b.y=p.paddleh-1
                        b.vy=-b.vy
                        b.vx=-6
                    elif b.x in range(p.paddleX-18,p.paddleX+19):
                        b.y=p.paddleh-1
                        b.vy=-b.vy
                        b.vx=2
                    elif b.x in range(p.paddleX+19,p.paddleX+56):
                        b.y=p.paddleh-1
                        b.vy=-b.vy
                        b.vx=8
                    elif b.x in range(p.paddleX+56,p.paddleX+76):
                        b.y=p.paddleh-1
                        b.vy=-b.vy
                        b.vx=16
                    elif b.x in range(p.paddleX+76,p.paddleX+(p.paddleWidth/2)+1):
                        b.y=p.paddleh-1
                        b.vy=-b.vy
                        b.vx=20
                    #Play ball bouncing on paddle sound
                    self.boink.rewind()
                    self.boink.play()
                self.grabpaddle=False
            
            #Condition to check if ball has already crossed the paddle-Y        
            elif b.y > p.paddleh:
                self.powerDown.rewind()
                self.powerDown.play()
                if b.y >= p.h+200:
                    self.grabpaddle=True
                    self.lifelost()
                    #Condition to check if there are any remaining lives
                    if self.lives == 0:
                        self.mode="GAME OVER"
                        return
                    #If there are remaining lives, return ball to paddle
                    b.vx=0
                    b.vy=0 
                    b.y=p.paddleh
                    b.x=p.paddleX
        
    #When mode is switched to game over, make the ball disappear, turn off the music, play game over sound, enter name for high score                   
    def gameover(self):
        b.vx=0
        b.vy=0
        b.x=10000
        b.y=10000
        self.gameTrack.pause()
        self.gameOver.play()

    def assignPowerUps(self):
        for i in range(self.numkills):
            while True:
                rand=randint(1,(board.row*board.column)-1)
                if not board.tiles[rand].powerUp:
                    board.tiles[rand].powerUp = True
                    board.tiles[rand].kill = True
                    break
                
        for i in range(self.numextralives):
            while True:
                rand=randint(1,(board.row*board.column)-1)
                if not board.tiles[rand].powerUp:
                    board.tiles[rand].powerUp = True
                    board.tiles[rand].extralife = True
                    break
                
        for i in range(self.numthrubricks):
            while True:
                rand=randint(1,(board.row*board.column)-1)
                if not board.tiles[rand].powerUp:
                    board.tiles[rand].powerUp = True
                    board.tiles[rand].thrubrick = True
                    break
    
    #Method to deduct a life from total lives
    def lifelost(self):
        self.lives=self.lives-1
        self.thrubrick=False 
 
    #Method to check if a level has been completed and if so, increment the level, make all tiles visible, return ball to paddle and reset total tiles
    def checkLevel(self):
        global SPEED
        if (board.totaltiles==0 and self.lives>0) or (board.totaltiles==18 and dxb.level==3 and self.lives>0):
            self.level+=1
            self.thrubrick=False
            self.grabpaddle=True
            b.x=p.paddleX
            b.y=p.paddleh
            b.vx=0
            b.vy=0
            b.speed=SPEED+3*(self.level-1)
            board.totaltiles=board.row*board.column
            for tile in board.tiles:
                tile.visible=True
                tile.powerUp=False
            self.assignPowerUps()
            self.appendPowers()
        if self.lives == 0:
            self.mode="GAME OVER"
            return  
         
    def highScores(self):
        file = open('highscores.txt','r')
        for l in file:
            l = l.strip().split(':')
            if self.highscore.get(l[0]) <= int(l[1]):            
                self.highscore[l[0]]=int(l[1])
        self.nums=list(self.highscore.values())
        self.nums.sort()
        self.nums.reverse()
        for value in self.nums:
            for h in self.highscore:
                if self.highscore[h]==value:
                    self.names.append(h)
                    del self.highscore[h]
                    break
        file.close()
        textSize(36)
        fill(120)
        for i in range (5):
            text(str(self.names[i])+'  ',800,320+60*i)
            textAlign(RIGHT)
            text(str(self.nums[i]),1000,320+60*i)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
p = Paddle(WIDTH,HEIGHT,PWIDTH)
b = Ball(p.paddleX,p.paddleh,SPEED)   
board = Board()
dxb = DXBall() 

def setup():
    size(p.w,p.h)

def draw ():
    if dxb.mode == "MENU":
        background(0)
        tint(255,64)
        image(dxb.backimage,0,0,p.w,p.h)
        noTint()
        textAlign(LEFT)
        textSize(32)
        fill(70)
        rect(p.w//2.5+45,p.h//3+2,250,50,40)
        if p.w//2.5 < mouseX < p.w//2.5+250 and p.h//3 < mouseY < p.h//3+50:
            fill(0,164,180)
        else:
            fill(255)
        text("PLAY GAME",p.w//2.5+80,p.h//3+40)
        fill(70)
        rect(p.w//2.5+45,p.h//3+102,250,50,40)
        if p.w//2.5 < mouseX < p.w//2.5+250 and p.h//3+100 < mouseY < p.h//3+150:
            fill(0,164,180)
        else:
            fill(255)
        text("HIGH SCORES",p.w//2.5+67,p.h//3+140)
        dxb.game(mouseX)
    elif dxb.mode == "HIGH SCORE":
        background(0)
        image(dxb.highscoreimg,WIDTH/2-220,100)
        dxb.highScores()
        if 900<= mouseX<=1200 and 550<=mouseY<=675:
            fill(0,255,0)
        text("BACK", 1100,650) 
    elif dxb.mode == "PLAY":
        background(0)
        board.display()
        noCursor()
        if dxb.pause == False:
            p.display(mouseX)
            b.display()
            dxb.game(mouseX)
        else:
            textSize(30)
            fill(255,255,255)
            text("Paused",p.w//2-60,p.h//2)
    elif dxb.mode == "GAME OVER":
        dxb.gameover()
        background(0)
        image(dxb.highscoreimg,WIDTH/2-220,100)
        fill(255,255,255)
        textSize(36)
        text("Your Score: "+str(dxb.score),600,350)
        text("Enter your name: ",600,450)
        text(str(dxb.name),920,450)
   
def mouseClicked():
    if dxb.mode == "MENU":
        if p.w//2.5 < mouseX < p.w//2.5+250 and p.h//3 < mouseY < p.h//3+50:
            dxb.menuMusic.pause()
            dxb.mode="PLAY"
        elif p.w//2.5 < mouseX < p.w//2.5+250 and p.h//3+100 < mouseY < p.h//3+150:
            dxb.mode="HIGH SCORE"
    elif dxb.mode == "HIGH SCORE":
        if 900<= mouseX<=1200 and 550<=mouseY<=675:
            fill(0,255,0)
            dxb.mode = "MENU"
            dxb.menuMusic.play()
    elif dxb.mode == "PLAY" and dxb.grabpaddle:
        b.vy=-b.speed
        
def keyPressed():
    if dxb.mode == "PLAY":
        #Press P for pausing the game
        if keyCode == 80:
            dxb.pause = not dxb.pause
            if dxb.pause == True:
                dxb.gameTrack.pause()
            else:
                dxb.gameTrack.play()
        #Press M for going back to the main menu
        elif keyCode == 77:
            dxb.mode = "MENU"
            cursor(POINT)
    elif dxb.mode == "GAME OVER":
        fill(255)
        if type(key) == int:
            pass
        elif keyCode == 10:
            f = open('highscores.txt','a')
            f.write(dxb.name+':'+str(dxb.score)+'\n')
            f.close()
            p.__init__(WIDTH,HEIGHT,PWIDTH)
            b.__init__(p.paddleX,p.paddleh,SPEED)
            board.__init__()
            dxb.__init__()
            dxb.mode="MENU"
            cursor(POINT)
        elif keyCode == 8:
            dxb.name = dxb.name[:len(dxb.name)-1]
        else:
            dxb.name+=key
