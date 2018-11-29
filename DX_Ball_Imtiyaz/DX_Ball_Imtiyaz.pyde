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
    
    def display(self):
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
        self.r=5
        
    def game(self):
        if b.x in range(p.paddleX-92,p.paddleX+92) and b.y in range (p.h-13,p.h-9):
            p.ground=p.h-13
            
        elif b.y < p.h or b.y > p.h:
            p.ground=10000000

            
p = Paddle()
b = Ball(x,vx,y,vy)   
dxb = DXBall() 

def setup():
    size(WIDTH,HEIGHT)

def draw ():
    p.display(mouseX)
    b.display()
    
    
