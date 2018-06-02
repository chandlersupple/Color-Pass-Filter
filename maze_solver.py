import io
import pygame
from PIL import Image
from urllib2 import urlopen

#url = str(input('Maze Url: '))
url = 'http://www.fun-roadtrip-games.info/images/maze%207.gif'
url_open = urlopen(url).read()
img = io.BytesIO(url_open)
img_open = Image.open(img)
pix_val = list(img_open.getdata())
pix = img_open.load()
dimensions = img_open.size

pygame.init()

master = pygame.display.set_mode((dimensions[0], dimensions[1]))
pygame.display.set_caption('Black and White Maze')
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

pix_num = 0
for y in range (0, dimensions[1]):
    if (pix_num >= len(pix_val) - 1):
        break
    for x in range(0, dimensions[0]):
        if (pix[x,y] > 0):
            pygame.draw.rect(master, white, (x, y, 1, 1), 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.display.flip()
    clock.tick(30)
