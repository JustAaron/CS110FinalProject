import pygame
import invader
import tower
import path
import bullet

def main():
	pygame.init()
	screen = pygame.display.set_mode((600,600))
	pygame.display.set_caption("Tower Defense")

	#Invader
	print("Testing one Invader----------------------")
	test_invader = invader.Invader("slime.png",(0,100)) #Creates object
	
	#############################################
	print("Positioning test for Invader----------------")
	#############################################
	print("Standard LEFT test for Invader----------------")
	test_invader.move("right")
	assert test_invader.rect == (30,100,20,20)
	
	print("Zero Input LEFT test for Invader----------------")
	test_invader.move("up")
	assert test_invader.rect == (30,70,20,20)

	print("Standard UP test for Invader----------------")
	test_invader.move("down")
	assert test_invader.rect == (30,100,20,20)

	print("Zero Input UP test for Invader----------------")
	test_invader.move("left")
	assert test_invader.rect == (0,100,20,20)
	
	#############################################
	print("Direction test for Invader----------------")
	#############################################
	print("Standard First Path")
	direction = test_invader.getDirection(path.Path())
	assert direction == "right"
	
	
	#Tower
	print("Testing one Tower ----------------------")
	test_tower = tower.Tower((0,0)) #Creates object
	
	############################################
	print("Testing positioning of tower icon ----------------------")
	#############################################
	print("Following x change----------")
	test_tower.followmouse((2,0))
	assert test_tower.rect == (2,0,50,50)
	
	print("Following y change----------")
	test_tower.followmouse((0,5))
	assert test_tower.rect == (2,5,50,50)

	print("Following both x and y change---------")
	test_tower.followmouse((3,5))
	assert test_tower.rect == (5,10,50,50)
	

	############################################
	print("Invader in Range ----------------------")
	#############################################
	print("Invader in Range---------")
	range = test_tower.inRange(4,8)
	assert range == True

	print("Invader NOT in Range---------")
	notrange = test_tower.inRange(500,200)
	assert notrange == False




	#Path
	print("Testing Path --------------------------")
	test_path = path.Path() #Creates object

	############################################
	print("Getting Path ----------------------")
	#############################################
	print("Coordinates of First Path-------")
	coordinates = test_path.getPathXY(1)
	assert coordinates == (0,50)
	
	print("Coordinates of First Path-------")
	pathnum = test_path.getNextPath(test_invader)
	assert pathnum == 2

                  
main()


        
     


