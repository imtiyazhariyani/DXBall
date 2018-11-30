import os
path=os.getcwd()

WIDTH=1500
HEIGHT=900
x=0
vx=10
y=0
vy=10

class Paddle:
    def __init__(self):
        self.paddle=loadImage(path+"/images/paddle.jpg")
        self.ground=10000000
        self.h=HEIGHT-120
        self.paddleX=None
        

    def display(self,x):
        background(0)
        if x in range(0,92):
            self.paddleX=92
        elif x in range(WIDTH-92,WIDTH):
            self.paddleX=WIDTH-92
        else:
            self.paddleX=x
        fill(255)
        #rect(self.paddleX-46,self.h,92,12)
        image(self.paddle,self.paddleX-92,self.h,184,38)
        dxb.game()
    
class Ball:
    def __init__(self,x,vx,y,vy):
        self.x=x
        self.vx=vx
        self.y=y
        self.vy=vy
        self.num=1
    
    def display(self):
        if self.num in range(3):
            if self.x > width:
                self.vx=-10 
            if self.x < 0: 
                self.vx=10
            if self.y < 0:
                self.vy=-self.vy
            if self.y > p.ground:
                if b.x in range(p.paddleX-94,p.paddleX-75):
                    self.vy=-self.vy
                    self.vx=-30
                elif b.x in range(p.paddleX-75,p.paddleX-55):
                    self.vy=-self.vy
                    self.vx=-10
                elif b.x in range(p.paddleX-55,p.paddleX-18):
                    self.vy=-self.vy
                    self.vx=-5
                elif b.x in range(p.paddleX-18,p.paddleX+19):
                    self.vy=-self.vy
                    self.vx=0
                elif b.x in range(p.paddleX+19,p.paddleX+56):
                    self.vy=-self.vy
                    self.vx=5
                elif b.x in range(p.paddleX+56,p.paddleX+76):
                    self.vy=-self.vy
                    self.vx=10
                elif b.x in range(p.paddleX+76,p.paddleX+95):
                    self.vy=-self.vy
                    self.vx=30
            self.x+=self.vx
            self.y+=self.vy
            fill(220,220,220)
            ellipse(self.x,self.y,25,25)
        
class DXBall:
    def __init__(self):
        self.mode="MENU"
        self.pause=False
        
       
        
    def game(self):
        if self.mode == "PLAY":
            if b.x in range(p.paddleX-92,p.paddleX+92) and b.y in range (p.h-13,p.h-9):
                p.ground=p.h-13
                
            elif b.y < p.h or b.y > p.h:
                p.ground=HEIGHT+200
                if b.y > p.ground:
                    self.mode="GAME OVER"
p = Paddle()
b = Ball(x,vx,y,vy)   
dxb = DXBall() 

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
        if dxb.pause == False:
            p.display(mouseX)
            b.display()
        else:
            textSize(30)
            fill(255,0,0)
            text("Paused",WIDTH//2-45,HEIGHT//2)
   
def mouseClicked():
    if WIDTH//2.5 < mouseX < WIDTH//2.5+250 and HEIGHT//3 < mouseY < HEIGHT//3+50:
        #dxb.menuMusic.pause()
        #dxb.music.play()
        dxb.mode="PLAY"
        
def keyPressed():
    if keyCode == 80:
        dxb.pause = not dxb.pause
        #dxb.pauseSound.rewind()
        #dxb.pauseSound.play()
        
       # if dxb.pause == True:
        #    dxb.music.pause()
        #else:
         #   dxb.music.play()
    
