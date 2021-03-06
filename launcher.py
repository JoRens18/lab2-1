import pygame, sys, math

Max_Mag = 100
Min_Mag = 10
Max_Ang = 90
Min_Ang = 0

RED=(255,0,0)

def class launcher:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.mag = 20
    self.ang = 45

  def changeMagnitude(self,delta):
    self.mag = self.mag + delta
    if(self.mag > Max_Mag):
      self.mag = Max_Mag
    if(self.mag < Min_Mag):
      self.mag = Min_Mag
  
  def changeAngle(self,delta):
    self.ang = self.ang + delta
    if(self.ang > Max_Ang):
      self.ang = Max_Ang
    if(self.ang < Min_Ang):
      self.mag = Min_Ang

  def draw(self,surf):
    ex=self.x+self.mag*math.cos(math.radians(self.ang))
    ey=self.y-self.mag*math.sin(math.radians(self.ang))
    pygame.draw.line(surf, RED, (self.x, self.y), (ex,ey), 6)
    ##pygame.display.update() #I do not know if we want this here or somewhere else

