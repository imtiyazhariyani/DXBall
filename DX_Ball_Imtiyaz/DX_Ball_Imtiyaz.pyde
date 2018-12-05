add_library('minim')
import os, random
path=os.getcwd()
player = Minim(this)

#Dimensions of the screen
WIDTH=1500
HEIGHT=960

#Initial paramaters of the ball
vx=0
vy=0

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
            image(self.paddle,self.w-200+i*50,35,31,7)
        
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
    def __init__(self,x,vx,y,vy):
        self.x=x
        self.vx=vx
        self.y=y
        self.vy=vy
        
    def display(self):
            if dxb.nextlife:
                self.ground=10000000
                self.vy=-15
                dxb.nextlife=False
            elif self.x==0 and self.y==0:
                self.vx=10
                self.vy=15
            elif self.x > p.w:
                self.vx=-10 
            elif self.x < 0: 
                self.vx=10
            elif self.y < 0:
                self.vy=-self.vy
            elif self.y > p.ground:
                if b.x in range(p.paddleX-92,p.paddleX-75):
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
                elif b.x in range(p.paddleX+76,p.paddleX+93):
                    self.vy=-self.vy
                    self.vx=30
            self.x+=self.vx
            self.y+=self.vy
            fill(150)
            #stroke(150)
            ellipse(self.x,self.y,25,25)
        
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

    def game(self,paddleX):
        if self.mode == "PLAY":
            self.gameTrack.play()
            if b.x in range(p.paddleX-p.paddleWidth/2,p.paddleX+(p.paddleWidth/2)+1) and b.y in range (p.paddleh-15,p.paddleh):
                if dxb.flag != 1:
                    self.boink.rewind()
                    self.boink.play()
                self.flag=0
                p.ground=p.paddleh-15
                
            elif b.y < p.paddleh or b.y > p.paddleh:
                p.ground=p.h+1500
                if b.y == p.h+1500:
                    self.flag=1
                    self.powerDown.rewind()
                    self.powerDown.play()
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
                    
        if self.mode == "GAME OVER":
            b.vx=0
            b.vy=0
            b.x=10000
            b.y=10000  
            
    def nextLife(self):
        self.nextlife=True  
  
    def lifelost(self):
        self.lives=self.lives-1
        
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

class DisplayTile:
    def __init__ (self):
        self.x=300
        self.y=125
        self.board=[]
        
    def display(self):
        for i in range(10):
            for s in range(15 -3,-2,-1):
                if s-i==-1 or s-i==1:
                    fill(196,129,0)
                else:
                    fill(0,188,137)
                    stroke(133,124,132)
                rect(self.x+(75*s),self.y+(50*i),75,50,7)                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
p = Paddle(WIDTH,HEIGHT)
b = Ball(p.paddleX,vx,p.paddleh,vy)   
dxb = DXBall() 
animation_electricity = Animation(12)
d = DisplayTile()
#t = Tile()

def setup():
    size(p.w,p.h)

def draw ():
    if dxb.mode == "MENU":
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
        d.display()
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
               # if dxb.pause == True:
        #    dxb.music.pause()
        #else:
         #   dxb.music.play()
    elif keyCode == 77:
        dxb.mode = "MENU"
        cursor(POINT)

        

    
