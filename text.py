from settings import *

class Text(pg.sprite.Sprite):

    def __init__(self,x,y,msg,game,size,ind=0,color=BLACK,button=0):
        super().__init__()
        self.ind = ind 
        self.game = game
        self.msg = msg
        self.pos = x,y
        self.size = size
        self.color = color
        self.origcolor = color
        self.active = False
        self.hidden= True
        
        self.darker = GRAY
        self.button = button

        if self.button:
            self.sheet = pg.image.load('Images/Button%d.png'%self.button).convert_alpha()
        self.update()

        
    
    def hide(self):
        self.active = False
        self.image = pg.Surface((self.rect.width,self.rect.height))
        self.image.fill((254,67,236))
        self.image.set_colorkey((254,67,236))
        
    

    def update(self):
        
        


        if self.active:
            self.color = self.darker
        else:
            self.color = self.origcolor


        self.font = pg.font.Font(FONT,self.size)
        self.image = self.font.render(self.msg,True,self.color)
        self.rect = self.image.get_rect()
    
        if self.button:
            but = pg.transform.scale(self.sheet,(self.rect.width+self.size+len(self.msg)*3,self.rect.height+self.size+4))
            butrect = but.get_rect()
            self.rect.center = butrect.center 
            if self.button==3:
                self.rect.y = butrect.height - self.size - self.size//2 +6
                if self.ind==0:
                    self.rect.y +=10

            but.blit(self.image,self.rect)
            self.image = but
            self.rect = self.image.get_rect()
        
        self.rect.topleft = self.pos

        if self.ind<0 and not self.game.waiting:
            self.hide()
        
    

        
        