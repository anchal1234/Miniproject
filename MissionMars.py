from mission_mars_function import *
import random

red=(255,0,0)
white=(0,0,0)
sc=0


screen=screenSize(1000,750)
screenrect=screen.get_rect()

background=setBackgroundImage("space.bmp")
background2=setBackgroundImage("space.bmp")



rocket=makeSprite("Rocket_Ship.png")
showSprite(rocket)


obstacle1=makeSprite("obstacle3.png")
showSprite(obstacle1)

obstacle2=makeSprite("apache.png")
showSprite(obstacle2)

obstacle3=makeSprite("obstacle1.png")
showSprite(obstacle3)

makeMusic("music.mp3")
playMusic(1)

sy=0
screen_height=750

xPos=450
yPos=500

x=0
y=0

x1=5
y1=5

x2=0
y2=0

moveSprite(rocket,xPos,yPos)
moveSprite(obstacle1,x,y)
moveSprite(obstacle2,x1,y1)
moveSprite(obstacle3,x2,y2)

while True:
##    screen.blit(background,(sy,0))
##    screen.blit(background2,(sy-screen_height,0))
##    sy=sy+1
##    if sy==screen_height:
##        sy=0

    
    y=y+2
    y1=y1+1
    y2=y2+4  
    if y==1000:
        x=random.randint(0,750)
        y=0
        sc+=10
        
    if y1==1000:
        x1=random.randint(5,800)
        y1=0
        sc+=10

    if y2==1000:
        x2=random.randint(0,700)
        y2=0
        sc+=10
    
##    if keyPressed("up"):
##        yPos-=1
##    elif keyPressed("down"):
##        yPos+=1

    if keyPressed("right"):
        xPos+=5
    

    elif keyPressed("left"):
        xPos-=5

    if xPos<=0 or xPos>=1000:
        print("boundaries")
        Right=False
        Left=False
    
    if touch(rocket,obstacle1) and touch(rocket,obstacle2) and touch(rocket,obstacle3):
        y1=0
        y=0
        y2=0
    if touch(rocket,obstacle1):
        y=0
    if touch(rocket,obstacle2):
        y1=0
    if touch(rocket,obstacle3):
        y2=0
        
        
    
    moveSprite(rocket,xPos,yPos)
    moveSprite(obstacle1,x,y)
    moveSprite(obstacle2,x1,y1)
    moveSprite(obstacle3,x2,y2)

    font1=pygame.font.SysFont("monospace",20,bold=True,italic=True)
    text1=font1.render("Esc:Exit",True,red)
    screen.blit(text1,(0,0))

    score=pygame.font.SysFont("monospace",20,bold=True,italic=True)
    text2=score.render("Score: %d"% sc,True,red)
    updateDisplay()
    screen.blit(text2,(0,20))
    




