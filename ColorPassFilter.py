# Chandler Supple, 6/2/2018

# The algorithm may be unresponsive for a few seconds after having initialized depending on the file size.

import io
import pygame
from PIL import Image
from urllib2 import urlopen

url = raw_input('Image Url (png, jpg): ')
color_scale = raw_input('Color Pass Filter (red, blue, green, grey): ')

url_open = urlopen(url).read()
img = io.BytesIO(url_open)
img_open = Image.open(img)
pix_val = list(img_open.getdata())
pix = img_open.load()
dimensions = img_open.size

try:
    pygame.init()
    master = pygame.display.set_mode((dimensions[0], dimensions[1]))
    pygame.display.set_caption('Color Pass Filter')
    clock = pygame.time.Clock()
    master.fill((0, 0, 0))
    quit = 0
    
    if (color_scale == 'grey'):
        global pix
        pix_num = 0
        for y in range (0, dimensions[1]):
            if (pix_num >= len(pix_val) - 1):
                break
            for x in range(0, dimensions[0]):
                listed_rbg = [pix[x,y][0], pix[x,y][1], pix[x,y][2]]
                color = (sorted(listed_rbg)[2], sorted(listed_rbg)[2], sorted(listed_rbg)[2])
                pygame.draw.rect(master, color, (x, y, 1, 1), 0)
    if (color_scale == 'red'):
        global pix
        pix_num = 0
        for y in range (0, dimensions[1]):
            if (pix_num >= len(pix_val) - 1):
                break
            for x in range(0, dimensions[0]):
                color = (pix[x,y][0], 0, 0)
                pygame.draw.rect(master, color, (x, y, 1, 1), 0)
    if (color_scale == 'green'):
        global pix
        pix_num = 0
        for y in range (0, dimensions[1]):
            if (pix_num >= len(pix_val) - 1):
                break
            for x in range(0, dimensions[0]):
                color = (0, pix[x,y][1], 0)
                pygame.draw.rect(master, color, (x, y, 1, 1), 0)
    if (color_scale == 'blue'):
        global pix
        pix_num = 0
        for y in range (0, dimensions[1]):
            if (pix_num >= len(pix_val) - 1):
                break
            for x in range(0, dimensions[0]):
                color = (0, 0, pix[x,y][2])
                pygame.draw.rect(master, color, (x, y, 1, 1), 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = 1
                pygame.quit()
        pygame.display.flip()
        clock.tick(60)
    
except:
    if (quit != 1):
        print("Sorry, but an error occured. It's likely that the image you inputted was invalid.")
