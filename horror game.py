from gamelib import*
game = Game(1000,800,"Escape the Mad House")
bk = Image("bk.jpg",game)
zombie1 = Image("zombie 1.png",game)
zombie1.resizeBy(-60)
zombie1.y = 500
zombie1.x = 127                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
bedroom = Image("bedroom.jpg",game)
bedroom.resizeTo(game.width,game.height)
zombie3 = Image("zombie3.png",game)
zombie3.resizeBy(-60)
keys = Image("keys.png",game)
keys.resizeBy(-90)
zombiegirl = Image("zombie girl.png",game)
zombiegirl.y = 500
zombiegirl.x = 850
bk3 = Image("background3.jpg",game)
bk3.resizeTo(game.width,game.height)
door = Image("door.gif",game)
door.resizeBy(-30)
door1pt2 = Image("door1pt2.gif",game)
door1pt2.resizeBy(-30)
door2pt2 = Image("door2pt2.gif",game)
door2pt2.resizeBy(-30)
door2 = Image("door2.gif",game)
door2.resizeBy(-30)
door3 = Image("door3.gif",game)
door3.resizeBy(-30)
door3pt2 = Image("door3pt2.gif",game)
door3pt2.resizeBy(-30)
door4 = Image("door4.gif",game)
door4.resizeBy(-30)
door5 = Image("door5.gif",game)
door5.resizeBy(-30)
door5pt2 = Image("door5pt2.gif",game)
door5pt2.resizeBy(-30)
zombiegirl.resizeBy(40)
zombie2 = Image("zombie 2.png",game)
zombie2.resizeBy(-80)
dragon = Image("dragon.png",game)
dragon.resizeBy(-10)
zombie5 = Image("zombie5.png",game)
zombie5.resizeBy(-60)
dragon.moveTo(700,300)
man = Image("mario.png",game)
man.resizeBy(-70)
bk.resizeTo(game.width,game.height)
grenade = Image("grenade.png",game)
grenade.resizeBy(-30)
grenade2 = Image("grenade2.png",game)
grenade2.resizeBy(-30)
grenade3 = Image("grenade3.png",game)
grenade3.resizeBy(-30)
theend = Image("the end.gif",game)
theend.resizeTo(game.width,game.height)
stairs = Image("stairs.jpg",game)
stairs.resizeTo(game.width,game.height)
cornerhall = Image("corner hallway.jpg",game)
keys6 = Image("keys6.png",game)
keys6.resizeBy(-90)
cornerhall.resizeTo(game.width,game.height)
howtoplay = Image("how to play.jpg",game)
howtoplay.resizeTo(game.width,game.height)
keys2 = Image("keys2.png",game)
keys2.resizeBy(-90)
background2 = Image("background 2.jpg",game)
background2.resizeTo(game.width,game.height)
keys3 = Image("keys3.png",game)
keys3.resizeBy(-90)
keys4 = Image("keys4.png",game)
keys4.resizeBy(-90)
bk3 = Image ("background3.jpg",game)
bk3.resizeTo(game.width,game.height)
keys5 = Image("keys5.png",game)
keys5.resizeBy(-90)
bk4 = Image("background4.jpg",game)
bk4.resizeTo(game.width,game.height)
bosstitle = Image("boss title.jpg",game)
bosstitle.resizeTo(game.width,game.height)
play = Image("play2.jpg",game)
play.resizeBy(-30)
start = Image("start.jpg",game)
start.resizeBy(-30)
play2 = Image("play.jpg",game)
play2.resizeBy(-30)
fire = Image("firee.gif",game)
zombie4 = Image("zombie4.png",game)
zombie4.resizeBy(-80)
level2 = Image("level2.jpg",game)
level2.resizeTo(game.width,game.height)
level3 = Image("level3.jpg",game)
level3.resizeTo(game.width,game.height)
level4 = Image("level4.jpg",game)
level4.resizeTo(game.width,game.height)
level5 = Image("level5.jpg",game)
level5.resizeTo(game.width,game.height)
nextb = Image("nextbutton.png",game)
nextb.resizeBy(-30)
nextb2 = Image("nextbutton2.png",game)
nextb2.resizeBy(-30)
nextb3 = Image("nextbutton3.png",game)
nextb3.resizeBy(-30)
nextb4 = Image("nextbutton4.png",game)
nextb4.resizeBy(-30)
nextb5 = Image("nextbutton5.png",game)
nextb5.resizeBy(-30)
#Title Screen
while not game.over:
    
    game.processInput()
    bk.draw()
    
    
    zombie1.draw()
    zombiegirl.draw()
    game.drawText("єscαpє thє mαd hσusє",game.width-570,game.height-350)
    start.draw()
    start.y = 230

    if start.collidedWith(mouse)and mouse.LeftButton:
        game.over = True
        
    game.drawText("Click Start to Begin",game.width-570,game.height-250)

    game.update(60)
game.over = False

#how to play
while not game.over:
    game.processInput()
    howtoplay.draw()
    play.draw()
    play.y = 600
    if play.collidedWith(mouse)and mouse.LeftButton:
        game.over = True
    game.drawText("Click Play to Begin",game.width-570,game.height-280)

    game.update(60)
game.over = False 

#level 1

while not game.over:
    game.processInput()
    bedroom.draw()
    man.move(True)
    man.moveTo(mouse.x, mouse.y)
    keys.move(True)
    keys.setSpeed(10,30)
    zombie2.move(True)
    zombie2.setSpeed(11,50)
    if man.collidedWith(zombie2):
        man.health-=10
    if man.collidedWith( zombie2 ):
        game.score  -= 10
        zombie2.speed += 15
        
        x = randint(zombie2.width,game.width-zombie2.width)
        y = randint(zombie2.height,game.height-zombie2.height)
        zombie2.moveTo(x,y)
        a = randint( 0 , 360 )
        zombie2.angle = a
   
    if man.collidedWith(keys):
        keys.visible = False
        game.score+=10
        game.over = True   
   
        
    

    game.displayScore(10,10)
    game.drawText("Health "+str(man.health),100,100)


    game.update(60)
game.over = False


#Level 1 pt2
while not game.over:
    game.processInput()
    bedroom.draw()
    man.move(True)
    man.moveTo(mouse.x, mouse.y)
    door.draw()
    door1pt2.draw()
    door.x = 300
    door.y = 300
    door1pt2.x = 800
    door1pt2.y = 300
    if man.collidedWith(door):
        game.over = True

    game.displayScore(10,10)
    
    game.update(60)
game.over = False

#Level 2 Screen
while not game.over:
    game.processInput()
    level2.draw()
    nextb.draw()
    nextb.x = 500
    nextb.y = 200
    if nextb.collidedWith(mouse)and mouse.LeftButton:
        game.over = True
    game.update(60)
game.over = False

#Level 2
while not game.over:
    
    game.processInput()
    stairs.draw()
    man.draw()
    man.moveTo(mouse.x, mouse.y)
    keys2.move(True)
    keys2.setSpeed(11,150)
 
    
    game.displayScore(10,10)
    zombie2.move(True)
    zombie2.setSpeed(11,50)
    zombie4.move(True)
    zombie4.setSpeed(15,20)
    
    if man.collidedWith(zombie2):
        man.health-=10
    if man.collidedWith( zombie2 ):
        game.score  -= 10
        zombie2.speed += 15
        x = randint(zombie2.width,game.width-zombie2.width)
        y = randint(zombie2.height,game.height-zombie2.height)
        zombie2.moveTo(x,y)
        a = randint( 0 , 360 )
        zombie2.angle = a

    if man.collidedWith(zombie4):
        man.health-=10
    if man.collidedWith( zombie4 ):
        game.score  -= 10
        zombie4.speed += 1
        x = randint(zombie4.width,game.width-zombie4.width)
        y = randint(zombie4.height,game.height-zombie4.height)
        zombie4.moveTo(x,y)
        a = randint( 0 , 360 )
        zombie4.angle = a

    if man.collidedWith(keys2):
        keys2.visible = False
        game.score+=10
        game.over = True

    
   
    game.displayScore(10,10)
    game.drawText("Health "+str(man.health),100,100)


    game.update(60)
game.over = False

#level 2 pt2
while not game.over:
    game.processInput()
    stairs.draw()
    man.moveTo(mouse.x,mouse.y)
    door2.draw()
    door2pt2.draw()
    door2.x = 800
    door2.y = 300
    door2pt2.x = 300
    door2pt2.y = 300
    if man.collidedWith(door2):
        game.over = True

    game.displayScore(10,10)
    
    game.update(60)
game.over = False


#Level 3 Screen
while not game.over:
    game.processInput()
    level3.draw()
    nextb2.draw()
    nextb2.x = 500
    nextb2.y = 200
    game.update(60)
    if nextb2.collidedWith(mouse)and mouse.LeftButton:
        game.over = True

game.over = False

#Level 3
while not game.over:
    game.processInput()
    background2.draw()
    man.draw()
    man.moveTo(mouse.x,mouse.y)
    keys3.move(True)
    keys3.setSpeed(12,35)
    game.displayScore(10,10)
    zombie3.move(True)
    zombie3.setSpeed(11,50)
    zombie5.move(True)
    zombie5.setSpeed(15,20)
    if man.collidedWith(keys3):
        keys3.visible = False
        game.score+=10
        
    if man.collidedWith( zombie3 ):
        game.score  -= 10
        zombie3.speed += 15
        


        game.over = True

    game.update(60)
game.over = False

#Level 3 pt2
while not game.over:
    game.processInput()
    background2.draw()
    door3pt2.draw()
    door3pt2.x = 800
    door3pt2.y = 300 
    man.draw()
    man.moveTo(mouse.x,mouse.y)
    door3.draw()
    door3.x = 300
    door3.y = 300 
    if man.collidedWith(door3):
        game.over = True

    game.displayScore(10,10)
    
    game.update(60)
game.over = False

#Level 4 Screen
while not game.over:
    game.processInput()
    level4.draw()
    nextb4.draw()
    nextb4.x = 500
    nextb4.y = 200
    if nextb4.collidedWith(mouse)and mouse.LeftButton:
        game.over = True
        
    game.update(60)
game.over = False
    
#Level 4
while not game.over:
    game.processInput()
    bk3.draw()
    man.draw()
    man.moveTo(mouse.x,mouse.y)
    keys4.draw()
    
    game.displayScore(10,10)

    zombie2.move(True)
    zombie2.setSpeed(11,50)
    zombie4.move(True)
    zombie4.setSpeed(15,20)


    
    if man.collidedWith(keys4):
        keys4.visible = False
        game.score+=10
        game.over = True
        
    game.update(60)
game.over = False


#Level 4 pt2
while not game.over:
    game.processInput()
    bk3.draw()
    man.move(True)
    man.moveTo(mouse.x, mouse.y)
    door.draw()
    door4.x = 200
    door4.y = 300
    if man.collidedWith(door4):
        game.over = True

    game.displayScore(10,10)
    
    game.update(60)
game.over = False


#Level 5 Screen
while not game.over:
    game.processInput()
    level5.draw()
    nextb5.draw()
    nextb5.x = 500
    nextb5.y = 200
    if nextb5.collidedWith(mouse)and mouse.LeftButton:
        game.over = True
        
    game.update(60)
game.over = False

#Level 5
while not game.over:
    game.processInput()
    bk4.draw()
    man.draw()
    man.moveTo(mouse.x,mouse.y)
    keys5.draw()
    keys5.y = 100
    keys5.x = 500
    game.displayScore(10,10)
    zombie3.move(True)
    zombie3.setSpeed(11,50)
    zombie5.move(True)
    zombie5.setSpeed(15,20)
    zombie2.move(True)
    zombie2.setSpeed(11,50)

    if man.collidedWith(keys5):
        keys5.visible = False
        game.score+=10
        game.over = True

    game.update(60)
game.over = False


#Level 5 pt2
while not game.over:
    game.processInput()
    bk4.draw()
    man.move(True)
    man.moveTo(mouse.x, mouse.y)
    door5pt2.draw()
    door5.draw()
    door5pt2.y = 300
    door5pt2.x = 300
    door5.x = 800
    door5.y = 300
    if man.collidedWith(door5):
        game.over = True

    game.displayScore(10,10)
    
    game.update(60)
game.over = False

#Boss Instructions
while not game.over:
    game.processInput()
    
    bosstitle.draw()
    play2.draw()
    play2.y = 500
    play2.x = 340
    if play2.collidedWith(mouse)and mouse.LeftButton:

        game.over = True

    game.update(60)
game.over = False

#Boss Level
bossbattle = Image("boss battle bk.jpg",game)
bossbattle.resizeTo(game.width,game.height)
while not game.over:
    game.processInput()
    bossbattle.draw()
    dragon.draw()
    man.draw()
    man.moveTo(mouse.x,mouse.y)
    grenade.move()
    
    grenade2.draw()
    grenade2.y = 200
    grenade3.draw()
    grenade3.x =360
    game.displayScore(10,10)
   
    if man.collidedWith(grenade):
        grenade.moveTo(mouse.x+50,mouse.y+45)
    if grenade.collidedWith(dragon):
        fire.draw()
        grenade.visible=False
        game.score+=100
    if man.collidedWith(grenade2):
        grenade2.moveTo(mouse.x+50,mouse.y+45)
    if grenade2.collidedWith(dragon):
        fire.draw()
        grenade2.visible=False
        game.score+=100
    if man.collidedWith(grenade3):
        grenade3.moveTo(mouse.x+50,mouse.y+45)
    if grenade3.collidedWith(dragon):
        fire.draw()
        grenade3.visible=False
        game.score+=1000
        dragon.visible = False





    game.update(60)
game.over = False

#Escaping Screen
while not game.over:
    game.processInput()
    cornerhall.draw()
    man.draw()
    man.moveTo(mouse.x,mouse.y)



        

    game.update(60)
game.over = False

#Final Screen
while not game.over:

    game.processInput()
    theend.move()

    game.update(60)
game.over = True











































































