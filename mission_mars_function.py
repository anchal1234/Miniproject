import pygame,sys,random

pygame.init()
pygame.mixer.init()
spriteGroup=pygame.sprite.OrderedUpdates()
textboxGroup=pygame.sprite.OrderedUpdates()
backgroundImage=None
musicPaused=False

keydict={"esc":pygame.K_ESCAPE,"up":pygame.K_UP,"down":pygame.K_DOWN,"left":pygame.K_LEFT,"right":pygame.K_RIGHT}

screen=""
bgSurface=""

class newSprite(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.images.append(loadImage(filename))
        self.image=pygame.Surface.copy(self.images[0])
        self.rect=self.image.get_rect()
    def addImage(self,filename):
        self.images.append(loadImage(filename))

    def move(self,xpos,ypos,centre=False):
        if centre:
            self.rect.center=[xpos,ypos]
        else:
            self.rect.topleft=[xpos,ypos]

def screenSize(sizex,sizey):
    global screen

    screen=pygame.display.set_mode([sizex,sizey])
    pygame.display.set_caption("Mission Mars")
    bgSurface=screen.copy()
    pygame.display.update()
    return screen

def keyPressed(keyCheck=""):
    global keydict
    pygame.event.clear()
    keys=pygame.key.get_pressed()
##    if sum(keys)>0:
    if keyCheck=="" or keys[keydict[keyCheck.lower()]]:
        return True
##    return False


def loadImage(fileName):
        image=pygame.image.load(fileName)
        image=image.convert_alpha()
        return image

def setBackgroundImage(img):
    global bgSurface,backgroundImage
    surf=loadImage(img)
    backgroundImage=surf
    screen.blit(surf,[0,0])
    bgSurface=screen.copy()
    updateDisplay()

def makeSprite(filename):
    thisSprite=newSprite(filename)
    return thisSprite

def moveSprite(sprite,x,y,centre=False):
    sprite.move(x,y,centre)
    updateDisplay()


def showSprite(sprite):
    spriteGroup.add(sprite)
    updateDisplay()

def touch(sprite1,sprite2):
    collide=pygame.sprite.collide_mask(sprite1,sprite2)
    return collide

def makeMusic(filename):
    pygame.mixer.music.load(filename)


def playMusic(loops=0):
    global musicPaused
    if musicPaused:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.play(loops)
    musicPaused=False

def updateDisplay():
    global bgSurface
    spriteRects=spriteGroup.draw(screen)
    textboxRects=textboxGroup.draw(screen)
    pygame.display.update()
    keys=pygame.key.get_pressed()
    if (keys[pygame.K_ESCAPE]):
        pygame.quit()
        sys.exit()
    spriteGroup.clear(screen,bgSurface)
    textboxGroup.clear(screen,bgSurface)



if __name__=="__main__":
    print("mission mars pygame_functions")
