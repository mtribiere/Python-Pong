#!/usr/bin/env python
# coding: utf-8

##################################################
#####Pong game in Python using Tkinter library####
##################################################

import sys
from Tkinter import *


# Definition des variables de jeu
screenSizeY = 250
screenSizeX = 500
playerSizeY = 50
playerSizeX = 20
ballSize = 20
delayInterval = 10

ballColor = "white"
playerColor = "white"
backgroundColor = "black"

playerCoordY = 0
ballCoords = [screenSizeX//2,screenSizeY//2]
ballVel = [2,2]

# Fonction associant les touches et les actions du joueur
def keyPressed(event):
	global playerCoordY
	
	key = event.keysym

	if key == "Up" and playerCoordY>0:
		playerCoordY -= 20
	elif key == "Down" and playerCoordY+playerSizeY<screenSizeY:
		playerCoordY += 20
	
	canvas.coords(player,0,playerCoordY,playerSizeX,playerCoordY+playerSizeY)
	


# Fonction de mise a jour
def updateBall():

	if ballCoords[0]+ballSize >= screenSizeX or (ballCoords[0]<=playerSizeX and ((ballCoords[1] >= playerCoordY and ballCoords[1]<= playerCoordY+playerSizeY) or ballCoords[1]+ballSize >= playerCoordY and ballCoords[1]+ballSize<= playerCoordY+playerSizeY)):
		ballVel[0] = -ballVel[0]

	if ballCoords[1]+ballSize >= screenSizeY or ballCoords[1] <= 0:
                ballVel[1] = -ballVel[1]


	ballCoords[0] += ballVel[0]
	ballCoords[1] += ballVel[1]
	canvas.coords(ball,ballCoords[0],ballCoords[1],ballCoords[0]+ballSize,ballCoords[1]+ballSize)


# Création da la fenetre
window = Tk()
canvas = Canvas(window, width=screenSizeX, height=screenSizeY, bg=backgroundColor)

# Création du joueur
player = canvas.create_rectangle(0,0,playerSizeX,playerSizeY,fill=playerColor)
canvas.focus_set()
canvas.bind("<Key>",keyPressed)

# Creation de la balle
ball = canvas.create_oval(screenSizeX//2,screenSizeY//2,screenSizeX//2+ballSize,screenSizeY//2+ballSize,fill=ballColor)


# Fonction de mise a jour
def update():
	updateBall()
	if ballCoords[0] < 0-ballSize:
		print("GAME OVER")
		sys.exit()
	else:
		window.after(delayInterval,update)

# Ajouter tout les elements au Canvas et afficher le tout
canvas.pack()
window.after(100,update)
for i in range(0,100):
	print " coucou pierre et Lore ! bise ;) "
window.mainloop()
