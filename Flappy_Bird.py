# Flappy Bird
    # by Dyuman Aditya

from tkinter import *
import random


class FlappyBird:
    def __init__(self):
        self.window = Tk()
        self.window.title('Flappy Bird')

        self.canvasHeight = 380
        self.canvasWidth = 620

        self.canvas = Canvas(self.window, height = self.canvasHeight, width = self.canvasWidth, bg = 'white')
        self.canvas.pack(fill = BOTH)

#---------------------------------------------------------------------- IMPORTING IMAGES -----------------------------------------------------------------

        flappyBG = PhotoImage(file = 'assets/flappy-bird-gif-bg1.png')      		# Background Image
        self.movementBars = PhotoImage(file = 'assets/movementBar.gif')   		# Movement Bars
        self.flappy_bird_upflap = PhotoImage(file = 'assets/redbird-upflap.png')        # The bird (upflap)
        self.flappy_bird_downflap = PhotoImage(file = 'assets/redbird-downflap.png')    # The bird (downflap)
        self.flappy_bird_midflap = PhotoImage(file = 'assets/redbird-midflap.png')      # The bird (midflap)
        self.flappy_bird_upflap_rotated = PhotoImage(file = 'assets/redbird-upflap-rotated.png')       # The bird (upflap rotated)
        self.flappy_bird_downflap_rotated = PhotoImage(file = 'assets/redbird-downflap-rotated.png')   # The bird (downflap rotated)
        self.flappy_bird_midflap_rotated = PhotoImage(file = 'assets/redbird-midflap-rotated.png')     # The bird (midflap rotated)
        self.flappy_bird_dead = PhotoImage(file = 'assets/redbird-deadbird.png')        # Dead bird
        self.startLogo = PhotoImage(file = 'assets/flappyStartText.png')       		# Flappy logo
        self.gameOverText = PhotoImage(file = 'assets/gameover.png')          		# Game Over logo
        self.startInstructions = PhotoImage(file = 'assets/startmessage.png')    	# Tap Tap
        self.getReady = PhotoImage(file = 'assets/getReady.png')                   	# Get Ready text
        self.scoreBoard = PhotoImage(file = 'assets/scoreboard.png')               	# Get scoreBoard
        self.newBest = PhotoImage(file = 'assets/new_best.png')                    	# new Best icon
        self.restartImage = PhotoImage(file = 'assets/startbutton.png')


	# List for score images
        self.score = []                 
        for i in range(0, 10):
            self.score.append(PhotoImage(file = 'assets/' + str(i) + '.png'))


	# Create list for pipes
        self.upPipes = []               
        self.downPipes = []
	# The pipes (set 1-6, from bottom small)
        for i in range(1, 7):
            self.upPipes.append(PhotoImage(file = 'assets/' + 'pipeUp' + str(i) + '.png'))   
        for i in range(1, 7):
            self.downPipes.append(PhotoImage(file = 'assets/' + 'pipeDown' + str(i) + '.png'))

#------------------------------------------------------------------------------ LISTS --------------------------------------------------------------------

        # Lists for flap positions
        self.wingPos = []
        self.wingPos.append(self.flappy_bird_upflap)
        self.wingPos.append(self.flappy_bird_midflap)
        self.wingPos.append(self.flappy_bird_downflap)

        self.wingPosRotated = []
        self.wingPosRotated.append(self.flappy_bird_upflap_rotated)
        self.wingPosRotated.append(self.flappy_bird_midflap_rotated)
        self.wingPosRotated.append(self.flappy_bird_downflap_rotated)


#--------------------------------------------------------------------------- CREATE IMAGES -----------------------------------------------------------------

        # Create bg image
        self.canvas.create_image(0, 0, anchor = NW, image = flappyBG)


#------------------------------------------------------------------------- START RUNNING CODE --------------------------------------------------------------
	# Display the Start text and setup the game.
        self.startInit()    
        self.window.mainloop()



#----------------------------------------------------------------------------- FUNCTIONS -------------------------------------------------------------------


    def moveBars(self):
        if not self.gameOver:
            self.canvas.move('rec', -5, 0)
            self.moveBarPipeSpeed = 50      #Adjust this value to change bar movement speed and pipe speed
            self.canvas.after(self.moveBarPipeSpeed, self.moveBars)

    def createBar(self):
        if not self.gameOver:
            self.canvas.create_image(608, 329, image = self.movementBars, tags = 'rec')
            movementTime = self.moveBarPipeSpeed * 6
            self.canvas.after(movementTime, self.createBar)

    def flapWingsStraight(self):
        if not self.gameOver and self.straightFlap:
            if self.flapWingIndex > 2:
                self.flapWingIndex = 0
            self.canvas.delete('bird')
            self.canvas.create_image(self.birdPosX, self.birdPosY, image = self.wingPos[self.flapWingIndex], tags = 'bird')
            self.flapWingIndex += 1
            self.canvas.after(180, self.flapWingsStraight)

    def flapWingsRotated(self):
        if not self.gameOver and self.rotatedFlap:
            if self.flapWingIndexRotated > 2:
                self.flapWingIndexRotated = 0
            self.canvas.delete('bird')
            self.canvas.create_image(self.birdPosX, self.birdPosY, image = self.wingPosRotated[self.flapWingIndexRotated], tags = 'bird')
            self.flapWingIndexRotated += 1
            self.canvas.after(180, self.flapWingsRotated)




    def startInit(self):
        self.gameOver = False           

        self.canvas.delete('scoreboard', 'score', 'best', 'gameOverText', 'playButton', 'bird', 'pipes', 'rec')
        self.canvas.create_image(self.canvasWidth/2+10, self.canvasHeight/2+65, image = self.startInstructions, tags = 'instructions')
        self.canvas.create_image(self.canvasWidth/2, self.canvasHeight/2-145, image = self.startLogo, tags = 'startLogo')
        self.canvas.create_image(self.canvasWidth/2, self.canvasHeight/2-60, image = self.getReady, tags = 'getReady')

        # Create Bird
        self.birdPosX = self.canvasWidth/2 + 10
        self.birdPosY = self.canvasHeight/2 - 10
        self.straightFlap = True
        self.rotatedFlap = False
        self.flapWingIndex = 0 	    # Flap position
        self.flapWingIndexRotated = 0
        self.flapWingsStraight()    # Start flapping the bird's wings

        # Define bird parameters
        self.overlapBirdX1 = self.birdPosX - 18
        self.overlapBirdY1 = self.birdPosY - 11
        self.overlapBirdX2 = self.birdPosX + 13
        self.overlapBirdY2 = self.birdPosY + 12



        # Create Moving bars
        for i in range(0, 21):
            xPos = 608 - 30*i
            self.canvas.create_image(xPos, 329, image = self.movementBars, tags = 'rec')


        self.moveBars()     # Start moving the bars
        self.createBar()    # Create new bars


        self.pipeBottomPosY = 309
        self.window.bind('<space>', self.startGame)

    def startGame(self, event):
        self.canvas.delete('instructions', 'getReady', 'startLogo')

        self.startAfter = 2000                  # Time to start seeing the pillars
        self.changeScoreTime = self.startAfter  # Time to change score

        self.scoreIndex = -1                    # Set score to -1 to initialise
        self.fall = False                       # bird is starting to fall
        self.updateScore = True

        self.window.bind('<KeyPress-space>', self.flapUp)

        self.collideCheck()
        self.changeScore()
        self.movePipes()
        self.canvas.after(self.startAfter, self.createPipes)
        self.flapUp(event)

#---------------------------------------------------------------------- THE RISE AND FALL OF THE BIRD -----------------------------------------------------------

    def flapUp(self, event):
        if not self.gameOver:

            # Get bird to change orientation when climbing
            self.straightFlap = False
            self.rotatedFlap = True
            self.flapWingsRotated()

            self.fall = False
            upRange = 20
            for i in range(upRange):
                if i <= upRange and i > int(upRange/2) and not self.gameOver:
                    self.canvas.move('bird', 0, -1)
                    self.birdPosY = self.birdPosY-1
                    self.overlapBirdY1 -= 1
                    self.overlapBirdY2 -= 1
                if i <= int(upRange/2) and not self.gameOver:
                    self.canvas.move('bird', 0, -3)
                    self.birdPosY = self.birdPosY-3
                    self.overlapBirdY1 -= 3
                    self.overlapBirdY2 -= 3
                self.canvas.after(5)
                self.canvas.update()
            self.fall = True
            self.downfallCount = 0
            self.canvas.after(180, self.birdFall)


    def birdFall(self):
        dy = 2
        if not self.gameOver and self.fall:
            self.canvas.move('bird', 0, dy)
            self.birdPosY = self.birdPosY+dy
            self.overlapBirdY1 += dy
            self.overlapBirdY2 += dy

            # Set straight flap again
            if self.downfallCount == 7:
                self.straightFlap = True
                self.rotatedFlap = False
                self.flapWingsStraight()
            # Increase velocity of downfall
            if self.downfallCount <= 17:
                self.fallRate = 12
            if self.downfallCount > 17 and self.downfallCount <= 30:
                self.fallRate = 6
            if self.downfallCount > 30:
                self.fallRate = 4
            self.canvas.after(self.fallRate, self.birdFall)
            self.downfallCount += 1



#----------------------------------------------------------------------------- Create and move Pipes ---------------------------------------------------------------


    def createPipes(self):
        if not self.gameOver:
            x = random.randint(0, 5)               # Set a random couple of pipes

            self.canvas.create_image(700, 0, image = self.upPipes[x], anchor = N, tags = 'pipes')
            self.canvas.create_image(700, 309, image = self.downPipes[x], anchor = S, tags = 'pipes')
            self.canvas.after(self.startAfter, self.createPipes)

    def movePipes(self):
        if not self.gameOver:
            self.canvas.move('pipes', -5, 0)
            self.canvas.tag_raise('score')          # So that score is always in front
            self.canvas.tag_raise('bird')           # So that bird is always in front

            self.canvas.after(self.moveBarPipeSpeed, self.movePipes)

#--------------------------------------------------------------------------------- COLLIDE CHECK -------------------------------------------------------------------

    def collideCheck(self):
        if not self.gameOver:
            overlap = self.canvas.find_overlapping(self.overlapBirdX1, self.overlapBirdY1, self.overlapBirdX2, self.overlapBirdY2)
            if len(overlap)>2 or self.overlapBirdY2 >= self.pipeBottomPosY or self.overlapBirdY1 <= 0:
                self.gameOver = True
                self.updateScore = False
                self.finalScore = self.scoreIndex
                self.GameOver()
            self.canvas.after(1, self.collideCheck)

#--------------------------------------------------------------------------------- CHANGE THE SCORE -----------------------------------------------------------------

    def changeScore(self):
        self.scoreIndex += 1
        if self.updateScore and self.scoreIndex == 0:
            self.canvas.after(100, lambda : self.canvas.create_image(self.canvasWidth/2-20, self.canvasHeight/2-145, image = self.score[self.scoreIndex], tags = 'score'))
            self.changeScoreTime1 = self.startAfter + ((700 - self.birdPosX)*self.moveBarPipeSpeed)/5
            self.canvas.after(int(self.changeScoreTime1), self.changeScore)

        if self.updateScore and self.scoreIndex != 0:

            self.canvas.delete('score')         # Delete previous score

            if self.scoreIndex < 10:
                self.canvas.create_image(self.canvasWidth/2-20, self.canvasHeight/2-145, image = self.score[self.scoreIndex], tags = 'score')

            if self.scoreIndex >= 10 and self.scoreIndex < 100:
                scoreDigit1 = self.scoreIndex // 10
                scoreDigit2 = self.scoreIndex % 10
                self.canvas.create_image(self.canvasWidth/2-46, self.canvasHeight/2-145, image = self.score[scoreDigit1], tags = 'score')
                self.canvas.create_image(self.canvasWidth/2-22, self.canvasHeight/2-145, image = self.score[scoreDigit2], tags = 'score')

            if self.scoreIndex >= 100 and self.scoreIndex < 1000:
                scoreDigit1 = self.scoreIndex // 100
                scoreDigit2 = self.scoreIndex // 10 % 10
                scoreDigit3 = self.scoreIndex % 10
                self.canvas.create_image(self.canvasWidth/2-22, self.canvasHeight/2-145, image = self.score[scoreDigit3], tags = 'score')
                self.canvas.create_image(self.canvasWidth/2-46, self.canvasHeight/2-145, image = self.score[scoreDigit2], tags = 'score')
                self.canvas.create_image(self.canvasWidth/2-70, self.canvasHeight/2-145, image = self.score[scoreDigit1], tags = 'score')


            self.canvas.after(self.changeScoreTime, self.changeScore)



#------------------------------------------------------------------------------------- GAME OVER --------------------------------------------------------------------


    def GameOver(self):
        self.window.unbind('<space>')
        self.window.unbind('<Up>')
        self.window.unbind('<Down>')
        self.canvas.delete('score')

        deadFall = self.pipeBottomPosY - self.birdPosY      # How much the bird should fall after it is dead
        self.canvas.delete('bird')
        self.canvas.after(120)
        self.canvas.create_image(self.birdPosX, self.birdPosY, image = self.flappy_bird_dead, tags = 'bird')
        for i in range(int(deadFall-10)):
            self.canvas.move('bird', 0, 1)
            self.canvas.after(1)
            self.canvas.update()


        self.canvas.after(1400, lambda : self.canvas.create_image(self.canvasWidth/2, self.canvasHeight/2-90, image = self.gameOverText, tags = 'gameOverText'))
        self.canvas.after(2200, lambda : self.canvas.create_image(self.canvasWidth/2, self.canvasHeight/2+10, image = self.scoreBoard, tags = 'scoreboard'))
        self.canvas.after(2800, self.checkBestScore)        # Check best score and then display score


        

#------------------------------------------------------------------------------------ DISPLAY SCORE AT END --------------------------------------------------------------

    # Check best score from file and display it!
    def checkBestScore(self):  
        with open('assets/SCORE_BEST', 'r') as best_score:
            prev_score = int(best_score.read())
            best_score.close()
            if prev_score < self.finalScore:
                with open('assets/SCORE_BEST', 'w') as best_score:
                    best_score.write(str(self.finalScore))
                    best_score.close()
                    best = self.finalScore
                    self.canvas.create_image(self.canvasWidth/2, self.canvasHeight/2+45, image = self.newBest, tags = 'best')
            else:
                best = prev_score

        self.canvas.create_text(self.canvasWidth/2+20, self.canvasHeight/2+45, text = str(best), fill = 'black', font = ('Helvetica', 15, 'bold'), anchor = W, tags = 'best')
        self.displayScore(0)
        


    # displays rolling score numbers after game is over
    def displayScore(self, cnt):  
        self.canvas.delete('score')
        self.canvas.create_text(self.canvasWidth/2+20, self.canvasHeight/2, text = str(cnt), fill = 'black', font = ('Helvetica', 15, 'bold'), anchor = W, tags = 'score')
        cnt += 1
        if cnt <= self.finalScore:
            self.canvas.after(100, lambda : self.displayScore(cnt))
        else:
            # Restart Button
            self.playButton = Button(self.canvas, image = self.restartImage, command = self.restartGame)
            self.canvas.after(800, lambda : self.playButton.place(x = self.canvasWidth/2-55, y = self.canvasHeight/2+126))
           
            

#------------------------------------------------------------------------------------- RESTART --------------------------------------------------------------------------------

    def restartGame(self):
        self.playButton.place_forget()
        self.startInit()
#===================================================================================== THE END =================================================================================

FlappyBird()


