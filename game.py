import pygame, math, random, time, sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtGui import QColor, QIcon, QPalette
from PyQt5.QtCore import pyqtSlot
pygame.init()
display_width = 1200
display_height = 800
screen = pygame.display.set_mode([display_width, display_height])
pygame.display.set_caption("Kalambury")
clock = pygame.time.Clock()
draw_on = False
last_pos = (0, 0)
color = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 200)
red = (200, 0, 0)
green = (0, 200, 0)
white = (255, 255, 255)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)
bright_blue = (0, 0, 255)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def button(msg, x, y, width, height, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, width, height))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, width, height))

    smallText = pygame.font.SysFont('comicsansms', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x + (width / 2)), (y + (height / 2)))
    screen.blit(TextSurf, TextRect)


def clear():
    screen.fill(white)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Kalambury", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        screen.blit(TextSurf, TextRect)

        button('PLAY', 400, 400, 100, 50, green, bright_green, game_loop)
        button('QUIT', 700, 400, 100, 50, red, bright_red, quit)


        pygame.display.update()
        clock.tick(15)


def roundline(srf, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0]+float(i)/distance*dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(srf, color, (x, y), radius)


def game_loop():
    screen.fill(white)
    radius = x = 5
    scroll = (1100, 700)
    circle = False

    try:
        while True:
            e = pygame.event.wait()
            if e.type == pygame.QUIT:
                raise StopIteration
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 4:
                    radius += 1
                if e.button == 5:
                    radius -= 1
                    if radius == 0:
                        radius = 1
                if e.button == 1:
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                    pygame.draw.circle(screen, color, e.pos, radius)
                    draw_on = True

            if e.type == pygame.MOUSEBUTTONUP:
                draw_on = False

            if e.type == pygame.MOUSEMOTION:
                if draw_on:
                    pygame.draw.circle(screen, color, e.pos, radius)
                    roundline(screen, color, e.pos, last_pos, radius)
                last_pos = e.pos
            if circle == False:
                pygame.draw.circle(screen, black, scroll, radius)
                circle = True
                x = radius
            if circle == True and x != radius:
                pygame.draw.circle(screen, white, scroll, max(radius, x))
                pygame.draw.circle(screen, black, scroll, radius)
                circle = False

            button('RESET', 1100, 550, 80, 50, blue, bright_blue, clear)
            button('Color', 1100, 490, 80, 50, blue, bright_blue)
            pygame.display.flip()


    except StopIteration:
        pass


game_intro()
game_loop()
pygame.quit()
quit()



