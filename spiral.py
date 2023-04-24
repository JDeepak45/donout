import math
import pygame
pygame.init()
white = (255,255,255)
black= (0,0,0)
width=1920
height=1080
xs,ys=0,0
xsep,ysep=10,20
row=height//ysep
coloumn=width//xsep
size=row*coloumn
xoffset=coloumn/2
yoffset=row/2
A,B=0,0
teta=10
p=1
chars= ".,-~:;=!*#$@"
screen=pygame.display.set_mode((width,height))
display=pygame.display.set_mode((width,height))
pygame.display.set_caption("drawing")
font=pygame.font.SysFont('Arial',20,bold=True)

def text(letter,xs,ys):
    text=font.render(str(letter),True,white)
    display.blit(text,(xs,ys))

run=True
while(run):
    screen.fill((black))
    z=[0]*size
    b=[' ']*size
    for j in range(0,628,teta):
        for i in range(0,628,p):
            c=math.sin(i)
            d=math.cos(j)
            e=math.sin(A)
            f=math.sin(j)
            g=math.cos(A)
            h=d+2
            D=1/(c*h*e+f*g+5)
            l=math.cos(i)
            m=math.cos(B)
            n=math.sin(B)
            t=c*h*g-f*e
            x=int(xoffset + 40 *D*(l*h*m-t*n) )
            y=int(yoffset + 20 *D*(l*h*n-t*m) )
            o=int(x+coloumn*y)
            N=int(8*((f*e-c*d*g)*m-c*d*e-f*g-l*d*n))
            if row>y>0 and 0<x<coloumn and D>z[o]:
                z[o]=D
                b[o]=chars[N if N>0 else 0]
    if ys==row*ysep-ysep:
        ys=0
    for i in range(len(b)):
        A+=0.000002
        B+=0.000001
        if i==0 or i%coloumn:
            text(b[i],xs,ys)
            xs+=xsep
        else:
            ys+=ysep
            xs=0
            text(b[i],xs,ys)
            xs+=xsep


    pygame.display.update()
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False   