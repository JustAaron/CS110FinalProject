def main():
    #Invader
    print("Testing one Invader----------------------")
	test_invader = invader.Invader() #Creates object
    #############################################
    print("Positioning test for Invader----------------")
    #############################################
	print("Standard LEFT test for Invader----------------")
	test_invader.moveLeft(2)	
	assert test_invader.position() == (8,0)

    print("Zero Input LEFT test for Invader----------------")
	test_invader.moveLeft(0)
	assert test_invader.position() == (8,0)

	print("Standard UP test for Invader----------------")
	test_invader.moveUp(2)
	assert test_invader.position() == (7,2)

	print("Zero Input UP test for Invader----------------")
	test_invader.moveUp(0)
	assert test_invader.position() == (7,2)

	print("Standard DOWN test for Invader----------------")
	test_invader.moveDown(2)
	assert test_invader.position() == (7,0)

	print("Zero Input DOWN test for Invader----------------")
	test_invader.moveDown(0)
	assert test_invader.position() == (7,0)

	print("Standard RIGHT test for Invader----------------")
	test_invader.moveUp(2)
	assert test_invader.position() == (9,0)

	print("Zero Input DOWN test for Invader----------------")
	test_invader.moveDown(0)
	assert test_invader.position() == (9,0)
    #############################################
	print("Health Bar Testing for Invader----------------")
    #############################################
	print("Standard Bullet Shot ----------------")
	test_invader.getBullet(1)
	assert test_invader.healthbar() == 95
	
	print("No Bullet Shot ----------------")
	test_invader.getBullet(0)
	assert test_invader.healthbar() == 95

    print("Multiple Bullet Shots ----------------")
    test_invader.getBullet(2)
    assert test_invader.healthbar() == 85

    print("Multiple Bullet Shots ----------------")
    test_invader.getBullet(5)
    assert test_invader.healthbar() == 60

    #Castle
    print("Testing Castle-------------------------")
    test_castle = castle.Castle()
    #############################################
    print("Castle Invasion ---------------")
    #############################################
    print("Standard Invader in Castle ---------------")
    test_castle.getInvader(1)
    assert test_castle.healthbar() == 95

    print("Zero Invader in Castle ---------------")
    test_castle.getInvader(0)
    assert test_castle.healthbar() == 95

    print("Multiple Invader in Castle ---------------")
    test_castle.getInvader(3)
    assert test_castle.healthbar() == 80

    #Tower Bullet
    print("Testing one Bullet ----------------------")
    test_tower = tower.Tower()
    test_bullet = bullet.Bullet()
    #############################################
    print("Testing positioning of bullet ----------------------")
    #############################################
    print("Beginning of Bullet------------------")
    test_bullet.time(0)
    assert test_bullet.position() == test_tower.position()


                              
main()


        
     


