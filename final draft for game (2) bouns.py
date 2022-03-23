# Tic-Tac-Toe with numbers.
# Start with  player1 choosing number from [0,2,4,6,8]
# then player2 choosing number from [1,3,5,7,9]  
# and the player who reach sum of 15 first win
# Author: Ahmed Alaa Mohamed
# Date: 3-3-2022


# libraries which we need
from turtle import color, delay, width
import pygame as p
import os , sys

# p.init() will initialize all

p.init()

# it will display on screen
screen= p.display.set_mode((1000,750))

# for framerate
clock = p.time.Clock()

# basic font for user typed
font = p.font.SysFont('Bahnschrift',26,)
midfont = p.font.SysFont('bahnshrift',40,)


# varibales which i need in while loop and check winner
board = [0, 0, 0, 0, 0, 0,0, 0, 0]
lisst_even=[0,2,4,6,8]
lisst_odd=[1,3,5,7,9]
player = 1

#draw board in triminal and to check draw and winner
def tic_tac_toe ():
    print ('|' ,board[0],'|',board[1] ,'|', board[2],'|')
    print ('--------------------')
    print ('|' ,board[3],'|',board[4] ,'|', board[5],'|')
    print ('--------------------')
    print ('|' ,board[6],'|',board[7] ,'|', board[8],'|')


#start game button 
# button to choose from them the number which needed
def numButton(posx,posy,text):
    color = (23,23,23)

    if text  in lisst_even or text  in lisst_odd:
        color = (64,142,198)
   
    
    btn= p.Rect(posx, posy, 40, 40)
    p.draw.rect(screen,color, btn)#draw Rectangle to display on screen
    
    tx =font.render(f"{text}" , True , (255,255,255))
    screen.blit(tx , (posx+13,posy+5))
    return btn



#the button to choose the place of the number
def Button(posx,posy,text):
    

    btn= p.Rect(posx, posy, 120, 100)
    p.draw.rect(screen,(64,142,198), btn)#draw Rectangle to display on screen
    
    tx =font.render(f"{text}" , True , (255,255,255))
    screen.blit(tx , (posx+50,posy+27))
    return btn


#function which change every turn in board in teminal #helping check winner and draw
def move(x1,x2):
    board[x2] = x1
    tic_tac_toe()


#function which check winner
def winner ():

    if ((board[0]+board [1]+board[2]==15 and board[0]!= 0   and board [1]!= 0  and board [2]!= 0)  or
        (board[0]+board [3]+board[6]==15 and board[0]!= 0   and board [3]!= 0  and board [6]!= 0) or
        (board[1]+board [4]+board[7]==15 and  board[1]!= 0   and board [4]!= 0  and board [7]!= 0 )or 
        (board[3]+board [4]+board[5]==15  and board[3]!= 0   and board [4]!= 0  and board [5]!= 0  )or
        (board[2]+board [5]+board[8]==15  and board[2]!= 0   and board [5]!= 0  and board [8]!= 0 )or
        (board[6]+board [7]+board[8]==15  and board[6]!= 0   and board [7]!= 0  and board [8]!= 0 )or
        (board[2]+board [4]+board[6]==15  and board[2]!= 0   and board [4]!= 0  and board [6]!= 0 )or
        (board[0]+board [4]+board[8]==15 and board[0]!= 0   and board [4]!= 0  and board [8]!= 0) ):

        # print("winner winner chicken dinner")
        return True #To know if we need to stop the game
    else: return False


#function which check draw
def draw ():

    if (board[0]+board [1]+board[2]!=15 and
        board[0]+board [3]+board[6]!=15 and
        board[1]+board [4]+board[7]!=15 and
        board[3]+board [4]+board[5]!=15 and
        board[2]+board [5]+board[8]!=15 and
        board[6]+board [7]+board[8]!=15 and
        board[2]+board [4]+board[6]!=15 and
        board[0]+board [4]+board[8]!=15 and
        board[0]!= 0   and board [1]!= 0  and board [2]!= 0 and board [3]!= 0  and board [4]!= 0 
         and board [5]!= 0  and board [6]!= 0  and board [7]!= 0  and board [8]!= 0 ):
       
        print("draw")
        return True #To know if we need to stop the game
    else: return False


the_sign=["$","$","$","$","$","$","$","$","$"]


#function of the main game
while True:

#quit button event
    for event in p.event.get():
        if event.type==p.QUIT:
            p.quit()

# get the mouse position on the window
        if event.type == p.MOUSEBUTTONDOWN:
            mouse = p.mouse.get_pos() 
            if event.type == p.MOUSEBUTTONDOWN:
                
                #check what the cliked button 
                try:
                    for k in posbuttonlist:
                        if k.collidepoint(mouse):

                            f=posbuttonlist.index(k)
                            if thechosennum!=None:
                               the_sign[f]=thechosennum

                            thechosennum= None
                        
                    if player == 2:
                        
                        for bb in buttonslisteven :

                            if bb.collidepoint(mouse):     
                                    index1 = buttonslisteven.index(bb)
                                    #get the button index from the list
                                    thechosennum = lisst_even[index1]

                                    lisst_even[index1] = ''
                                    buttonslisteven.remove(bb)

                                    # print(thechosennum)
                                    if thechosennum!=None and thechosennum != '':
                                        the_sign[f]=thechosennum
                                        x1=thechosennum
                                        x2=f
                                        print(x1,x2)
                                        move(x1,x2)
                                        player = 1
                                        
                                    
                                    thechosennum= None
                    else:
                        for bb2 in buttonslistodd:
                            if bb2.collidepoint(mouse):
                                index2 = buttonslistodd.index(bb2)
                                            #get the button index from the list
                                thechosennum = lisst_odd[index2]
                                lisst_odd[index2] = ''
                                buttonslistodd.remove(bb2)

                                # print(thechosennum)
                                if thechosennum!=None and thechosennum != '':
                                    the_sign[f]=thechosennum
                                    x1=thechosennum
                                    x2=f
                                    print(x1,x2)
                                    move(x1,x2)    
                                    player = 2              
                                # if winner():
                                #     p.time.delay(5000)   
                                thechosennum= None   
                    
                except:
                    pass  
                            

    
# objects will display on the screen
    wallpaper_screen = p.Rect(0,0,1000,750)
    p.draw.rect(screen,(13,18,51),wallpaper_screen)
    btn1=numButton(900,150,1)
    btn2= numButton(900,250,3)
    btn3= numButton(900,350,5)
    btn4= numButton(900,450,7)
    btn5= numButton(900,550,9)


    btn6= numButton(50,150,0)
    btn7= numButton(50,250,2)
    btn8= numButton(50,350,4)
    btn9= numButton(50,450,6)
    btn10= numButton(50,550,8)

    

    buttonslistodd=[btn1,btn2,btn3,btn4,btn5]
    
    buttonslisteven=[btn6,btn7,btn8,btn9,btn10]

    listnum = []



    x=[180,450,720]
    y=[140,320,520]
    i=0
    posbuttonlist=[]
    
    for posy in y :
        for posx in x :
            # index=x.index(posx)+y.index(posy)
            btn= Button(posx,posy,the_sign[i])
            posbuttonlist.append(btn)
            i+=1
    
    #player1 text
    player1text = midfont.render('Player 2', True , (122,32,72))
    screen.blit(player1text , (20,100)) 

    #player 2 text
    player2text = midfont.render('Player 1', True , (122,32,72))
    screen.blit(player2text , (860,100))

    #player turn text
    playertextt = midfont.render(f'Player{player} turn ', True , (122,32,72))
    screen.blit(playertextt , (425,35))  
    playertextt = midfont.render(f'"choose the place first then the number"', True , (122,32,72))
    screen.blit(playertextt , (260,75))  


    background= p.image.load("C:\\fcai\PROGRAMMING\ASSINMENT1\\tic-tac-toe-lines1.png")
    h = p.transform.scale(background,(750,550))
    screen.blit(h,(120,120))

    if winner():
        # p.time.delay(5000)
        background_winner= p.image.load("C:\\fcai\PROGRAMMING\ASSINMENT1\\kindpng_1164846.png")
        h = p.transform.scale(background_winner,(550,300))
        screen.blit(h,(200,150))
        # exit()
    # please put code file with the image
    # and if put them in folder write folder name in the code before 'background.png'
    # as if folder name is (assignment 1) edit code to (BACKGROUND = pygame.image.load(os.path.join('assignment 1', 'background.png')) )


    if draw():
      p.time.delay(5000)
      exit()


    clock.tick(120)
    p.display.update()