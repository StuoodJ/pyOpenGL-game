import pygame

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

#specific variables

w = 1
h = 1
d = 1

#verticies

verticies = (
    (w, 0-h, 0-d),
    (w, h, 0-d),
    (0-w, h, 0-d),
    (0-w, 0-h, 0-d),
    (w, 0-h, d),
    (w, h, d),
    (0-w, 0-h, d),
    (0-w, h, d)
)

#edges

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

#Cube Function

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
    
#Main Function

def main():
  #pygame setup
  
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
  #opengl setup
  
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)
    
  #Running
  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

      #inputsystem
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            glTranslatef(0, 0, .1)
        if keys[pygame.K_s]:
            glTranslatef(0, 0, -.1)
        if keys[pygame.K_a]:
            glTranslatef(.1, 0, 0)
        if keys[pygame.K_d]:
            glTranslatef(-.1, 0, 0)
        if keys[pygame.K_UP]:
            glTranslatef(0, -.1, 0)
        if keys[pygame.K_DOWN]:
            glTranslatef(0, .1, 0)
        
      #opengl render
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        
      #pygame render
      
        pygame.display.flip()
        pygame.time.wait(10)

main()