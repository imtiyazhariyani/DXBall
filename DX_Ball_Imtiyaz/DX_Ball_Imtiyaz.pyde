import os
path=os.getcwd()

WIDTH=1200
HEIGHT=800
x=400
vx=10
y=300
vy=12

class Paddle:
    def __init__(self):
        self.paddle=loadImage(path+"/images/paddle.jpg")

    def display(self,x):
        background(0)
        image(self.paddle,x-50,HEIGHT-250,200,200)
        print "hello"

class Ball:
    def __init__(self,x,vx,y,vy):
        self.x=x
        self.vx=vx
        self.y=y
        self.vy=vy
    
    def display(self):
        if self.x > width or self.x < 0: 
            self.vx=-(self.vx)
        if self.y > height or self.y < 0:
            self.vy=-(self.vy)
        self.x+=self.vx
        self.y+=self.vy
        fill(220,220,220)
        ellipse(self.x,self.y,25,25)
        
p = Paddle()
b = Ball(x,vx,y,vy)    

def setup():
    size(WIDTH,HEIGHT)

def draw ():
    p.display(mouseX)
    b.display()
    
    
