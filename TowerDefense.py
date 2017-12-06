import invader
import tower
import path
import bullet
import pygame, sys
from pygame.locals import *

class Controller:
	def __init__(self,width=700,height=650):
		"""
		Descr: __init__ sets initial variables,lists,groups,buttons and music for the game
		Params: self, width/height (int)
		Returns: none """
		
		pygame.init() #Calls the init
		pygame.mixer.init()
		self.width = width
		self.height = height
        
		#Creates the window and title
		self.mainscreen = pygame.display.set_mode((self.width,self.height))
		pygame.display.set_caption("Tower Defense")
		self.background = pygame.Surface(self.mainscreen.get_size()).convert()
		self.clock = pygame.time.Clock()

		#Starting Variables: Initial starting values recieved at beginning of game
		self.money = 500
		self.health = 20
		self.tower = []
		self.invader = []
		self.bullets = []
		# make a sprites Group
		self.sprites = pygame.sprite.Group(tuple(self.tower))

		#Fonts
		self.largefont = pygame.font.SysFont('arial',100,True)
		self.font = pygame.font.SysFont('arial',30,True)
		
		# Load and set the sound
		pygame.mixer.music.load('Daydream.ogg')
		pygame.mixer.music.set_volume(0.5)
		self.soundcanplay = True

	################################################
		
		#Buttons 
		#Start button
		self.start = pygame.draw.rect(self.mainscreen,(255,255,255),(260,245,180,100))
		#Tower button
		self.towerimg = pygame.image.load('assets/' + "tower.png").convert_alpha()
		self.towerRect = self.towerimg.get_rect()
		#Instruction button
		self.instruction_button = pygame.draw.ellipse(self.mainscreen,(255,255,255),(565,570,40,65))
		#Sound button
		self.sound_button = pygame.draw.ellipse(self.mainscreen,(255,255,255),(635,575,50,60))# fix
		#Mainmenu button
		self.mainmenu_button = pygame.draw.rect(self.mainscreen,(255,255,255),(225,450,250,100))
		#Wave Start Button
		self.wave_start_button = pygame.draw.circle(self.mainscreen,(255,255,255),(605,560),44)
		#Restart Button
		self.restart_button = pygame.draw.rect(self.mainscreen,(255,255,255),(260,245,180,100))
		
		
		
    ##################################################

	#Screens 
	def startMenu(self):
		"""
		Descr: startMenu sets GUI for menu Screen
		Params: self		
		Returns: none """
		
		#Create background, and text on background
		pygame.mouse.set_visible(True)
		#Background of start menu
		menuscreen = pygame.image.load('assets/' + "frontpage.png").convert()
		menuscreen = pygame.transform.scale(menuscreen,(self.width,self.height))
		self.mainscreen.blit(menuscreen,(0,0))


	def interface(self):
		"""
		Descr: interface sets map and interface for Game Screen
		Params: self
		Returns: none """
		
		# Make background of interface
		mapscreen = pygame.image.load("assets/" + "mapscreen.png").convert()
		self.mainscreen.blit(mapscreen,(0,0))
		
		#To see variables on screen
		self.towerRect.center = (425,555)
		self.mainscreen.blit(self.towerimg,self.towerRect)
		
		#Money
		moneytext = self.font.render(str(self.money),True, (255,255,255))
		self.mainscreen.blit(moneytext,(175,510))
		#Health
		healthtext = self.font.render(str(self.health),True, (255,255,255))
		self.mainscreen.blit(healthtext,(175,585))
		#HealthBar
		for invading in self.invader:
			invading.healthbar(self.mainscreen)

	def instruction_Menu(self):
		"""
		Descr: instructionMenu sets GUI for menu Screen
		Params: self
		Returns: none """
		
		# Make background of instruction menu
		instructionima = pygame.image.load('assets/' + "instruction.png").convert()
		self.mainscreen.blit(instructionima,(0,0))
	
	def gameWon(self):
		"""
		Descr: gameWon sets GUI for Win Screen
		Params: self
		Returns: none """
		
		# Make background of gameWon
		endmenu = pygame.image.load('assets/' + "winpage.png").convert()
		self.endmenu = pygame.transform.scale(endmenu,(self.width,self.height))
		self.mainscreen.blit(self.endmenu,(0,0))

	def gameLost(self):
		"""
		Descr:gameLost sets GUI for Game Over Screen
		Params: self
		Returns: none """
		
		# Make background of gamelost
		endmenu = pygame.image.load('assets/' + "endpage.png").convert()
		self.endmenu = pygame.transform.scale(endmenu,(self.width,self.height))
		self.mainscreen.blit(self.endmenu,(0,0))
		
	####################################################	
 	# Sound controller 
	def soundplay(self):
		"""soundplay turns music off or on
		Params: self
		Returns: none """
		
		if self.soundcanplay == True:
			pygame.mixer.music.unpause()
		
		elif self.soundcanplay == False:
			pygame.mixer.music.pause()
	#####################################################
	def emptyOut(self):
		"""
		Descr: emptyOut resets initial variables
		Params: self
		Returns: none """
		
		self.health = 20
		self.money = 500
		self.tower = []
		self.invader = []
		self.bullets = []
		self.sprites.empty()
	#######################################################
	
	# Screens with events
	def winpageScr(self):
		"""
		Descr: winpageScr contains events for creating the Win Screen
		Params: self
		Returns: none """
		
		while self.winpage_Scr:
			self.gameWon()
			
			for event in pygame.event.get():
				# quit
				if event.type == pygame.QUIT:
					return pygame.quit()
			
				elif event.type == MOUSEBUTTONDOWN:
					# Click the restart button
					if self.restart_button.collidepoint(pygame.mouse.get_pos()):
						return self.startMenuScr()
					# Click instruction button
					if self.instruction_button.collidepoint(pygame.mouse.get_pos()):
						self.whereClickInstructionMenu = 3
						return self.instructionMenuScr()
					# Click sound button -- play and stop the sound
					if self.sound_button.collidepoint(pygame.mouse.get_pos()):
						if self.soundcanplay == False:
							self.soundcanplay = True
						elif self.soundcanplay == True:
							self.soundcanplay = False
						self.soundplay()
			pygame.display.flip()
			
	def endpageScr(self):
		"""
		Descr: endpageScr contains events for creating the Game Over Screen
		Params: self			
		Returns: none """
		
		while self.endpage_Scr:
			self.gameLost()
			
			for event in pygame.event.get():
				# quit
				if event.type == pygame.QUIT:
					return pygame.quit()
				
				elif event.type == MOUSEBUTTONDOWN:
					# Click the restart button
					if self.restart_button.collidepoint(pygame.mouse.get_pos()):
						return self.startMenuScr()
					# Click instruction button
					elif self.instruction_button.collidepoint(pygame.mouse.get_pos()):
						self.whereClickInstructionMenu = 2
						return self.instructionMenuScr()
					# Click sound button -- play and stop the sound
					elif self.sound_button.collidepoint(pygame.mouse.get_pos()):
						if self.soundcanplay == False:
							self.soundcanplay = True
						elif self.soundcanplay == True:
							self.soundcanplay = False
						self.soundplay()	
			pygame.display.flip()
		
	
	def instructionMenuScr(self):
		"""
		Descr: instructionMenuScr contains events for creating the Instruction Screen
		Params: self
		Returns: none """
		
		while self.instruction_Menu_Scr:
			self.instruction_Menu() #Creates the instruction menu screen
        	
			for event in pygame.event.get():
				# quit
				if event.type == pygame.QUIT:
					return pygame.quit()
					
				# Click the Mainmenu button and return to the main screen
				elif event.type == MOUSEBUTTONDOWN: 
					if self.mainmenu_button.collidepoint(pygame.mouse.get_pos()):
						if self.whereClickInstructionMenu == 1:
							return self.startMenuScr()
						elif self.whereClickInstructionMenu == 2:
							return self.endpageScr()
						elif self.whereClickInstructionMenu == 3:
							return self.winpageScr()
			
			pygame.display.flip()
        	
        	
	def gamemapScr(self):
		"""
		Descr: gameMapScr contains events for creating the Game Screen
		Params: self
		Returns: none """
		
		#initial values
		self.wavenum = 0
		self.inWave = False
		
		while self.gamemap_Scr:
			self.interface() #Creates the game menu screen
			mousepos = (pygame.mouse.get_pos())
			mousepos_change = (pygame.mouse.get_rel())
			
			# Game loss and return to the endpage
			if self.health == 0:
				self.emptyOut()
				return self.endpageScr()
			elif self.wavenum == 11:
				self.emptyOut()
				return self.winpageScr()
        	
			for event in pygame.event.get():
				# quit
				if event.type == pygame.QUIT:
					return pygame.quit()
					
				# Move tower and lose money
				elif event.type == MOUSEBUTTONDOWN:
					if self.towerRect.collidepoint(pygame.mouse.get_pos()):
						if self.money >= tower.Tower(mousepos).cost:
							self.tower.append(tower.Tower(mousepos))
							self.sprites.add(self.tower)
							self.tower[-1].ablemove = True
					elif self.wave_start_button.collidepoint(mousepos):
						if self.inWave == False:
							self.inWave = True
							self.num = 0
							self.wavenum += 1
							self.invadernum = ((self.wavenum*3)+5)
					
				elif event.type == MOUSEMOTION and self.tower != []:
					if self.tower[-1].ablemove == True:
						self.tower[-1].image = pygame.image.load('assets/' + 'tower2.png').convert_alpha()
						self.tower[-1].followmouse(mousepos_change)

				elif event.type == MOUSEBUTTONUP and self.tower != []:
					if self.tower[-1].ablemove == True:
						self.tower[-1].image = self.towerimg
						self.money -= self.tower[-1].cost
						self.tower[-1].ablemove = False


			#INVADERS IN WAVE
			if self.inWave == True:
				if self.num<self.invadernum:
					slime = invader.Invader("slime.png", (20,80))
					self.invader.append(slime)
					self.sprites.add(self.invader)
					self.num += 1
				elif self.num == self.invadernum:
					self.inWave = False
			
			#INVADER MOVEMENT
			for monsters in self.invader:
				direction = monsters.path()
				monsters.move(direction)
				#pygame.time.delay(100)
				
				#Health Decreasing when Invade reach castle
				if monsters.rect == (680,110,20,20):
					self.health -= 1
					self.sprites.remove(monsters)
					self.invader.remove(monsters)
				
				#Invaders in Tower Range get Shot
			for defenders in self.tower:
				for monsters in self.invader:
					if defenders.inRange(monsters.rect.x,monsters.rect.y):
						ammo = bullet.Bullet((defenders.rect.center))
						self.bullets.append(ammo)
						self.sprites.add(self.bullets)
						break

					#Bullet MOVEMENT
					for shoot in self.bullets:
						#Bullets Move to Invader Location
						shoot.to_invader(monsters.rect.center)
						if pygame.sprite.collide_rect(shoot,monsters):
							monsters.health -= 25
							self.sprites.remove(shoot)
							self.bullets.remove(shoot)
							
							#Monster Killed By Bullets
							if monsters.health == 0:
								self.money += 5
								self.sprites.remove(monsters)
								self.invader.remove(monsters)
				
			# upload the image
			self.interface()
			self.sprites.draw(self.mainscreen)
			pygame.display.flip()
    
    
	def startMenuScr(self):
		"""
		Desscr: startMenuScr contains events for creating the Start Menu Screen
		Params: self
		Returns: none """
		self.soundplay()
		while self.start_Menu_Scr:
			self.startMenu() #Creates the start menu screen
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return pygame.quit()
				
				elif event.type == MOUSEBUTTONDOWN:
					# Click start button
					if self.start.collidepoint(pygame.mouse.get_pos()):
						return self.gamemapScr()
					
					# Click instruction button
					elif self.instruction_button.collidepoint(pygame.mouse.get_pos()):
						self.whereClickInstructionMenu = 1
						return self.instructionMenuScr()
					
					# Click sound button -- play and stop the sound
					elif self.sound_button.collidepoint(pygame.mouse.get_pos()):
						if self.soundcanplay == False:
							self.soundcanplay = True
						elif self.soundcanplay == True:
							self.soundcanplay = False
						self.soundplay()
			pygame.display.flip()

	def mainLoop(self):
		"""
		Descr: mainLoop contains initial events and opens up Start Menu Screen
		Params: self
		Returns: none """
		
		# set different menu loop
		self.start_Menu_Scr = True
		self.instruction_Menu_Scr =True
		self.gamemap_Scr = True
		self.endpage_Scr = True
		self.winpage_Scr = True
		self.whereClickInstructionMenu = 0
		pygame.mixer.music.play(-1)
		
		#creates start menu
		self.startMenuScr()
		pygame.quit()

def main():
	main_window = Controller()
	main_window.mainLoop()

main()
