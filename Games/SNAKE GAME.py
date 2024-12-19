#importing modules
import pygame as p
import random as r
import os

# initializers
p.init()
#p.mixer.init()
screen_width = 1200
screen_height= 600
a = p.display.set_mode((screen_width,screen_height))

p.display.set_caption("saksham's snake")
p.display.update()
clock = p.time.Clock()
font = p.font.SysFont(None,55)


def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    a.blit(screen_text,[x,y])


def plot_snake(a,color,snake_list,snake_size):
    for x,y in snake_list:
        p.draw.rect(a,color,[x,y,snake_size,snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        a.fill((233,220,229))
        text_screen('WELCOME TO SNAKES','black',383,232)
        text_screen('PRESS SPACEBAR TO CONTINUE','black',290,275)
        for event in p.event.get():
            if event.type==p.QUIT:
                exit_game = True
            elif event.type == p.KEYDOWN:
                if event.key == p.K_SPACE:
                    gameloop()
        p.display.update()
        clock.tick(60)

def gameloop():
    exit_game = False
    game_over = False
    snake_x= 45
    snake_y= 55
    velocity_x = 0
    velocity_y= 0
    food_x = r.randint(20,screen_width/2)
    food_y = r.randint(20,screen_height/2)
    snake_size= 20
    score = 0
    fps = 50
    snake_list = []
    snake_len = 1
    if (not os.path.exists("hiscore.txt")):
        with open ("hiscore.txt","w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    while not exit_game:
        if game_over :
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            a.fill('white')
            text_screen('GAME OVER PRESS ENTER TO CONTINUE','red',200,235)

            for event in p.event.get():
                if event.type == p.QUIT:
                    exit_game = True

                if event.type == p.KEYDOWN:
                    if event.key == p.K_KP_ENTER:
                        gameloop()
                    if event.type == p.K_r:
                        f = open('hiscore.txt',"w")
                        cl = "0"
                        f.write(cl)
                        f.close()
        else:

            for event in p.event.get():
                if event.type ==p.QUIT:
                    exit_game =  True

                if event.type == p.KEYDOWN:
                    if event.key == p.K_RIGHT or event.key== p.K_d:
                        velocity_x = 5
                        velocity_y = 0

                    if event.key == p.K_LEFT or event.key == p.K_a:
                        velocity_x = -5
                        velocity_y = 0

                    if event.key == p.K_UP or event.key == p.K_w:
                        velocity_y = -5
                        velocity_x = 0  


                    if event.key == p.K_DOWN or event.key == p.K_s:
                        velocity_y = 5
                        velocity_x = 0  
                    if event.key == p.K_q:
                        score+=50
                    

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score+= 10
                fps+=7
                food_x = r.randint(20,screen_width/2)
                food_y = r.randint(20,screen_height/2)
                snake_len+=10
                if score>int(hiscore):
                    hiscore = score

            a.fill('white')
            p.draw.rect(a,'red',[food_x , food_y , snake_size , snake_size])
            text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), 'red', 5, 5)


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)


            if len(snake_list)>snake_len:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                game_over = True

            plot_snake(a,'black',snake_list,snake_size)
        p.display.update()
        clock.tick(fps)

    p.quit()
    quit()
welcome()
