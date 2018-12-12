add_library('minim')
import os, random
path=os.getcwd()
player = Minim(this)

#Dimensions of the screen
WIDTH=1500
HEIGHT=960

class Paddle:
    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.paddle=loadImage(path+"/images/paddle.jpg")
        self.ground=10000000
        self.paddleh=self.h-120
        self.paddleX=None
        self.paddleWidth=184
        self.electricity=loadImage(path+"/images/electricity.jpg")
    
    def display(self,x):
        
        #Image of paddle at the top of the screen to show remaining lives
        for i in range(dxb.lives-1):
            image(self.paddle,self.w-400+i*50,35,31,7)
        
        #Condition to make sure paddle is entirely on screen
        if x in range(0,self.paddleWidth/2):
            self.paddleX=(self.paddleWidth/2)+1
        elif x in range(self.w-self.paddleWidth/2,self.w):
            self.paddleX=self.w-self.paddleWidth/2
        else:
            self.paddleX=x
       
        #Condition to display electricity animation when ball is on paddle
        if dxb.flag == 1 and dxb.lives != 0:
            b.x=p.paddleX
            fill(102,104,106)
            #rect(self.paddleX-78,self.paddleh-27,10,35)
            #rect(self.paddleX+65,self.paddleh-27,10,35)
            animation_electricity.display()
            frameRate(18)
        else:
            frameRate(60)
            #for e in self.electricityimgs:
                #image(e,self.paddleX-self.paddleWidth/2,self.paddleh-60,self.paddleWidth,self.paddleWidth/2)
        
        #Display paddle image
        #fill(255)
        #rect(self.paddleX-46,self.paddleh,self.paddleWidth/2,12)
        image(self.paddle,self.paddleX-self.paddleWidth/2,self.paddleh,self.paddleWidth,38)
    
class Ball:
    def __init__(self,x,y):
        self.x=x
        self.vx=0
        self.y=y
        self.vy=0
        self.frames=0
        self.imageCount=79
        self.imagelist=[]
        self.bounce = player.loadFile(path+"/music/bounce.mp3")
        
        for num in range(self.imageCount):
            self.imagelist.append(loadImage(path+"/images/ball_edited2/frame_"+str(num)+"_delay-0.05s.png"))
    
        
    def display(self):
            if dxb.nextlife:
                self.ground=10000000
                self.vy=-15
                dxb.nextlife=False
            elif (self.x==0 and self.y==0) and (self.x==p.w and self.y==0):
                self.vx=10
                self.vy=15
                self.bounce.rewind()
                self.bounce.play()
            elif self.x > p.w:
                self.vx=-10 
                self.bounce.rewind()
                self.bounce.play()
            elif self.x < 0: 
                self.vx=10
                self.bounce.rewind()
                self.bounce.play()
            elif self.y < 0:
                self.vy=-self.vy
                self.bounce.rewind()
                self.bounce.play()
            elif self.y > p.ground:
                if b.x in range(p.paddleX-94,p.paddleX-75):
                    self.vy=-self.vy
                    self.vx=-30
                elif b.x in range(p.paddleX-75,p.paddleX-55):
                    self.vy=-self.vy
                    self.vx=-17
                elif b.x in range(p.paddleX-55,p.paddleX-18):
                    self.vy=-self.vy
                    self.vx=-5
                elif b.x in range(p.paddleX-18,p.paddleX+19):
                    self.vy=-self.vy
                    self.vx=2
                elif b.x in range(p.paddleX+19,p.paddleX+56):
                    self.vy=-self.vy
                    self.vx=7
                elif b.x in range(p.paddleX+56,p.paddleX+76):
                    self.vy=-self.vy
                    self.vx=23
                elif b.x in range(p.paddleX+76,p.paddleX+95):
                    self.vy=-self.vy
                    self.vx=30
            self.x+=self.vx
            self.y+=self.vy
            fill(150)
            #stroke(150)
            #ellipse(self.x,self.y,25,25)
            self.frames=(self.frames+1)%self.imageCount
            for i in range(self.imageCount):
                image(self.imagelist[self.frames],self.x-20,self.y-25,30,30)                                                                                                                                                            
        
class Animation:
    def __init__(self,imageCount):
        self.imageCount=imageCount
        self.frames=0
        self.imagelist=[]
        
        for num in range(self.imageCount):
            self.imagelist.append(loadImage(path+"/images/electricity/"+str(num)+".jpeg"))
    
    def display(self):
        self.frames=(self.frames+1)%self.imageCount
        for i in range(12):
            image(self.imagelist[self.frames],p.paddleX-72,p.paddleh-48,142,71,0,i*200,400,(i+1)*200)                                                                                                                                                                   

class Board:
    def __init__ (self):
        self.tiles=[]
        self.row=8
        self.column=16
        for r in range(self.row):
            for c in range(self.column):
                self.tiles.append(Tile(r,c))
        
    def display(self):
        for t in self.tiles:
            if t.visible:
                t.display()

class Tile:
    def __init__(self,r,c):
        self.r=r
        self.c=c
        self.w=75
        self.h=50
        self.x=self.c*self.w+140
        self.y=self.r*self.h+140
        self.visible=True
        self.powerUp=False
        self.brickimage=loadImage(path+"/images/brick.jpeg")
        #self.brickimage2=loadImage(path+"/images/brick.jpg")
    def isBallOn(self,mx,my):
        if  self.x <= mx <= self.x+self.w and self.y <= my <= self.y+self.h:
            return True
        return False
            
    def display(self):
        if self.isBallOn(b.x,b.y):
            self.visible=False
            dxb.score+=10
            #if abs(b.vx) > abs(b.vy):
            #b.vx=-b.vx
            #else:
            b.vy=-b.vy
        else:
            if self.c-self.r==0 or self.r+self.c==15: #or self.r+self.c==7 or self.r+self.c==22:
                fill(255,255,0)
                #image(self.brickimage,self.x,self.y,75,50)
                rect(self.x,self.y,75,50,17)
            else:
                fill(0,120,255)
                #stroke(255)
                #image(self.brickimage2,self.x,self.y,75,50)
                rect(self.x,self.y,75,50,7)
        power.display(self.r,self.c)        
        fill(255)
        #textFont(scorefont)
        textSize(24)
        text("Score: "+str(dxb.score),10,30)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

class PowerUp:
    def __init__(self):
        self.num=5
        self.assignPowerUps()
        self.vx=0
        self.vy=15
        self.powerimage=loadImage(path+"/images/+1.png")
    
    def assignPowerUps(self):
        for i in range(self.num):
            while True:
                rand=random.randint(1,(board.row*board.column)-1)
                if not board.tiles[rand].powerUp:
                    board.tiles[rand].powerUp = True
                    break                        
    
    def getTile(self,x,y):  #Return the index of the tile if coordinates match
        for tile in board.tiles:
            if tile.c == x and tile.r == y:
                return tile
        return None
    
    def update(self):
        self.y=self.y+self.vy
    
    def display(self,r,c):
        tile=self.getTile(c,r)
        self.y=tile.y
        if tile.powerUp==True and tile.visible==False:
                image(power.powerimage,tile.x,tile.y,75,50)
                self.update()
                dxb.lives+=1
            #tile.y=tile.y+power.vy

class ExtraLife(PowerUp):
    def __init__(self):
        PowerUp.__init__(self)
        

class DXBall:
    def __init__(self):
        self.mode="MENU"
        self.pause=False
        self.lives=4
        self.flag=1
        self.nextlife=False
        self.menuMusic = player.loadFile(path+"/music/menu.mp3")
        self.gameTrack = player.loadFile(path+"/music/gametrack.mp3")
        self.gameOver = player.loadFile(path+"/music/gameover.mp3")
        self.powerDown = player.loadFile(path+"/music/powerdown.mp3")
        self.boink = player.loadFile(path+"/music/boink.mp3")
        self.menuMusic.play()
        self.level=1
        self.score=0
        self.imagelist=[]
        self.frames=0
        for num in range(43):
            self.imagelist.append(loadImage(path+"/images/menu/frame_"+str(num)+"_delay-0.1s.png"))

    def game(self,paddleX):
        if self.mode == "PLAY":
            self.gameTrack.play()
            if b.x in range(p.paddleX-p.paddleWidth/2,p.paddleX+(p.paddleWidth/2)+1) and b.y in range (p.paddleh-15,p.paddleh):
                if dxb.flag != 1:
                    self.boink.rewind()
                    self.boink.play()
                self.flag=0
                p.ground=p.paddleh-15
                
            elif b.y > p.paddleh:
                self.powerDown.rewind()
                self.powerDown.play()
                p.ground=p.h+1500
                if b.y == p.h+1500:
                    self.flag=1
                    self.lifelost()
                    if self.lives == 0:
                        self.mode="GAME OVER"
                        self.gameTrack.pause()
                        self.gameOver.play()
                        return
                    b.vx=0
                    b.vy=0 
                    b.y=p.paddleh
                    b.x=paddleX
                    
        elif self.mode == "GAME OVER":
            b.vx=0
            b.vy=0
            b.x=10000
            b.y=10000
    
    def menuDisplay(self):
        if self.mode == "MENU":
            self.frames=(self.frames+1)%43
            for i in range(43):
                image(self.imagelist[self.frames],100,100)        
        
    def nextLife(self):
        self.nextlife=True  
  
    def lifelost(self):
        self.lives=self.lives-1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
p = Paddle(WIDTH,HEIGHT)
b = Ball(p.paddleX,p.paddleh)   
dxb = DXBall() 
animation_electricity = Animation(12)
board = Board()
power = PowerUp()

def setup():
    size(p.w,p.h)
    scorefont=createFont("Chalkduster-48.vlw",48)

def draw ():
    if dxb.mode == "MENU":
        #dxb.menuDisplay()
        dxb.frames=(dxb.frames+1)%43
        for i in range(43):
            image(dxb.imagelist[dxb.frames],100,100) 
        background(0)
        textSize(36)
        fill(70)
        rect(p.w//2.5,p.h//3,250,50)
        if p.w//2.5 < mouseX < p.w//2.5+250 and p.h//3 < mouseY < p.h//3+50:
            fill(0,255,0)
        else:
            fill(255)
        text("Play Game",p.w//2.5+20,p.h//3+40)
        fill(70)
        rect(p.w//2.5,p.h//3+100,250,50)
        if p.w//2.5 < mouseX < p.w//2.5+250 and p.h//3+100 < mouseY < p.h//3+150:
            fill(0,255,0)
        else:
            fill(255)
        text("Instructions",p.w//2.5+20,p.h//3+140)
    
    elif dxb.mode == "PLAY" or dxb.mode == "GAME OVER":
        background(0)
        board.display()
        noCursor()
        if dxb.pause == False:
            p.display(mouseX)
            b.display()
            dxb.game(mouseX)
        else:
            textSize(30)
            fill(255,0,0)
            text("Paused",p.w//2-45,p.h//2)
   
def mouseClicked():
    if dxb.mode == "MENU":
        if p.w//2.5 < mouseX < p.w//2.5+250 and p.h//3 < mouseY < p.h//3+50:
            dxb.menuMusic.pause()
            #dxb.music.play()
            dxb.mode="PLAY"
    elif dxb.mode == "PLAY" and dxb.flag == 1:
        dxb.nextLife()
        
def keyPressed():
    if keyCode == 80:
        dxb.pause = not dxb.pause
        #dxb.pauseSound.rewind() 
        #dxb.pauseSound.play()
        if dxb.pause == True:
            dxb.gameTrack.pause()
        else:
            dxb.gameTrack.play()
    elif keyCode == 77:
        dxb.mode = "MENU"
        cursor(POINT)

        

    
