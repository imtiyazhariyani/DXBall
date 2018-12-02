add_library('minim')
import os, random
path=os.getcwd()
player = Minim(this)

WIDTH=1500
HEIGHT=900
x=0
vx=10
y=0
vy=15

class Paddle:
    def __init__(self):
        self.paddle=loadImage(path+"/images/paddle.jpg")
        self.ground=10000000
        self.h=HEIGHT-120
        self.paddleX=None
        self.electricity=loadImage(path+"/images/electricity.jpg")
    
    def display(self,x):
        background(0)
        for i in range(dxb.lives-1):
            image(self.paddle,WIDTH-200+i*50,35,31,7)
        if x in range(0,92):
            self.paddleX=91
        elif x in range(WIDTH-92,WIDTH):
            self.paddleX=WIDTH-92
        else:
            self.paddleX=x
        if dxb.flag == 1 and dxb.lives != 0:
            b.x=p.paddleX
            fill(102,104,106)
            #rect(self.paddleX-78,self.h-27,10,35)
            #rect(self.paddleX+65,self.h-27,10,35)
            animation_electricity.display()
            frameRate(18)
        else:
            frameRate(60)
            #for e in self.electricityimgs:
                #image(e,self.paddleX-92,self.h-60,184,92)
        #fill(255)
        #rect(self.paddleX-46,self.h,92,12)
        image(self.paddle,self.paddleX-92,self.h,184,38)
    
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
            elif self.x > width:
                self.vx=-10 
            elif self.x <= 0: 
                self.vx=10
            elif self.y <= 0:
                self.vy=-self.vy
            elif self.y > p.ground:
                if b.x in range(p.paddleX-94,p.paddleX-75):
                    self.vy=-self.vy
                    self.vx=-40
                elif b.x in range(p.paddleX-75,p.paddleX-55):
                    self.vy=-self.vy
                    self.vx=-16
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
            ellipse(self.x,self.y,25,25)
        
class DXBall:
    def __init__(self):
        self.mode="MENU"
        self.pause=False
        self.lives=4
        self.flag=0
        self.nextlife=False
        self.menuMusic = player.loadFile(path+"/music/menu.mp3")
        self.boink = player.loadFile(path+"/music/boink.mp3")
        self.menuMusic.play()

    def game(self,paddleX):
        if self.mode == "PLAY":
            if b.x in range(p.paddleX-98,p.paddleX+97) and b.y in range (p.h-16,p.h):
                self.boink.rewind()
                self.boink.play()
                self.flag=0
                p.ground=p.h-13
                
            elif b.y < p.h or b.y > p.h:
                p.ground=HEIGHT+1500
                if b.y == HEIGHT+1500:
                    self.flag=1
                    self.lifelost()
                    if self.lives == 0:
                        self.mode="GAME OVER"
                        return
                    b.vx=0
                    b.vy=0 
                    b.y=p.h
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
            image(self.imagelist[self.frames],p.paddleX-72,p.h-48,142,71,0,i*200,400,(i+1)*200)
                                                                                            
p = Paddle()
b = Ball(x,vx,y,vy)   
dxb = DXBall() 
animation_electricity = Animation(12)

def setup():
    size(WIDTH,HEIGHT)

def draw ():
    if dxb.mode == "MENU":
        background(0)
        textSize(36)
        fill(70)
        rect(WIDTH//2.5,HEIGHT//3,250,50)
        if WIDTH//2.5 < mouseX < WIDTH//2.5+250 and HEIGHT//3 < mouseY < HEIGHT//3+50:
            fill(0,255,0)
        else:
            fill(255)
        text("Play Game",WIDTH//2.5+20,HEIGHT//3+40)
        fill(70)
        rect(WIDTH//2.5,HEIGHT//3+100,250,50)
        if WIDTH//2.5 < mouseX < WIDTH//2.5+250 and HEIGHT//3+100 < mouseY < HEIGHT//3+150:
            fill(0,255,0)
        else:
            fill(255)
        text("Instructions",WIDTH//2.5+20,HEIGHT//3+140)
    
    elif dxb.mode == "PLAY" or dxb.mode == "GAME OVER":
        noCursor()
        if dxb.pause == False:
            p.display(mouseX)
            b.display()
            dxb.game(mouseX)
        else:
            textSize(30)
            fill(255,0,0)
            text("Paused",WIDTH//2-45,HEIGHT//2)
   
def mouseClicked():
    if dxb.mode == "MENU":
        if WIDTH//2.5 < mouseX < WIDTH//2.5+250 and HEIGHT//3 < mouseY < HEIGHT//3+50:
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

        

    
