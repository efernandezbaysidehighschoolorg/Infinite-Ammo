'''
Game Name: Infinite Ammo
Company Name: ProBlood by Barry Yang, Elliot Fernandez, and Andrew Park
Objects:
1. Gangster+
2. Runner
Game Loop Decisions:
1. When the gangster collides with the mouse or crosshiar and left button, the score increase by 10
2. When the runner collides with the mouse or crosshiar and left button, the score decrease by 10
3. You win by getting over 200 points
4. You love by having less than or equal to -100.

Problems:
1. The gangster and runner moves to fast
2. the objects still have their own background.
3. the objects move in the wrong directions '''

#Game essentials
from gamelib import* #imports the functions and variables to create games
game = Game(800,600,"Infinite Ammo",60)
bk = Image("Street3.jpg",game)
game.setBackground(bk)
bk.resizeTo(800,600)
game.drawText("Infinite Ammo",game.width/3 ,game.height/8,Font(blue,90,yellow))
game.drawText("Press [SPACE] to Start",game.width/3,game.height/8 + 80,Font(green,50,red))
game.drawText("By Problood",game.width/3 ,game.height/2,Font(blue,90,red))
game.drawText("Barry Yang, Elliot Fernandez, and Andrew Park",game.width/3-100,game.height/2+50,Font(blue,45,red))
game.drawText("Instructions: Your goal is to kill the 5 gangsters before they touch the runner. If you fail to do your objective to protect the runner, you lose!",game.width/3-200,game.height/2+150,Font(blue,45,red)) 
game.wait(K_SPACE)
game.update()
gangster = []


for times in range(5):
    gangster.append(Animation("Gangman.png",6,game,450/3,470/2,5))

for g in gangster:
    x = randint(-1000,-100) 
    y = 500
    g.moveTo(x,y)
    g.setSpeed(4,-90)

runner = []

for times in range(1):
    runner.append(Animation("Runner.fw.png",6,game,1000/3,888/2,5))

for r in runner :
    x = g.width+1
    y = 500
    r.moveTo(x,y)
    r.setSpeed(1,-90)
    r.resizeTo(100,300)


crosshair = Image("crosshair.png",game)



while not game.over: 
    game.processInput()
    game.scrollBackground("right",2)
    game.scrollBackground("left",2)
    crosshair.moveTo(mouse.x,mouse.y)
    crosshair.resizeTo(80,60) 
    game.displayScore()
   

    for g in gangster:
        g.move() 
       
        g.health = 5
        if g.collidedWith(mouse) and mouse.LeftButton:
            g.health-=1
            game.score+=10
            g.visible= False



    for r in runner:
       
        r.move()
       
        r.health = 10
        if r.collidedWith(mouse) and mouse.LeftButton:
            r.health-=10
            game.score-=10
            r.visible = False


    if game.score>=50 or g.health<=0:
        game.drawText("You're a Weiner!",150,300,Font(yellow,90,red))
        game.over = True

    if game.score<=-10 or r.health<=0 or g.isOffScreen("right"):
        game.drawText("Ha! You're a Loser!",150,300,Font(yellow,90,red))
        game.over = True



    game.update(60)

game.drawText("Press [SPACE] to Exit  "+ str(game.score),320,400)
game.update(1)
game.wait(K_SPACE)
game.quit()








