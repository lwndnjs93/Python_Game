# MyPong의 주된 파일을 만듭니다.

import table, ball, bat, random, pygame
import tkinter as tk
from tkinter import *
from pygame import mixer

mixer.init()
mixer.music.load('eichenwalde.wav')

window = Tk(mixer.music.play(-1,0.0))
window.title("아이헨발데로 떠납니다")
my_table = table.Table(window)

#배경화면 불러오기


starry_night_image = PhotoImage(file = "eichen.gif")
my_table.canvas.create_image(0, 0, anchor=NW, image = starry_night_image, tags="bg_img")
my_table.canvas.lower("bg_img")

# 전역 변수 초기화
x_velocity = 11
y_velocity = 11
first_serve = True
life = 4

#윈도우 창 종료하면 음악 종
def on_close():
    mixer.music.stop()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_close)


# Ball 공장으로부터 볼을 주문합니다
"""
x_start y_start 공 위치 정하는 부분
width, height 공 크기 정하는 부분
colour 공 색 정하는 부분
"""
my_ball = ball.Ball(table = my_table, x_speed=x_velocity, y_speed=y_velocity,
                    width=24, height=24, colour="red", x_start=610, y_start=650)

 
# Bat 공장으로부터 배트를 주문합니다
"""
a_posn, y_posn은 막대의 위치 정하는 부분
width, height는 막대 크기 정하는 부분
color은 막대 색 정하는 부분

"""
bat_B = bat.Bat(table = my_table, width=100, height=10,
                x_posn=570, y_posn=700, colour="blue")   
    
#벽돌을 만드는 함수
def make_brick():
    global bricks
    bricks = []
    b = 0
    gap  = 30

    colour = ("green", "orange", "yellow", "purple")
    while b < 12:
        n = 1
        while n < 15:
            x = random.randrange(1,11)

            i=80

            if x == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10):
                brick = bat.Bat(table = my_table, width=78, height=20, x_posn=(n*i), y_posn=120+(b*gap), colour="red")
            else:
                brick = bat.Bat(table = my_table, width=78, height=20, x_posn=(n*i), y_posn=120+(b*gap), colour=(colour[(b-1) %4]))

            bricks.append(brick)
            n = n+1
        b = b+1

make_brick()
#### 함수:
def game_flow():
    global first_serve
    global life
    global bricks

    

    # 첫번째 서브를 기다립니다:
    if(first_serve==True):
        my_ball.stop_ball()
        first_serve = False
    
    # 배트에 공이 충돌하는지 감지
    bat_B.detect_collision(my_ball, sides_sweet_spot=False, topnbottom_sweet_spot=True)

    # 벽돌에 공이 충돌하는지 감지
    for a in bricks:
        if(a.detect_collision(my_ball, sides_sweet_spot=False) != None):
            my_table.remove_item(a.rectangle)
            bricks.remove(a)
        if(len(bricks) == 0):
            my_ball.stop_ball()
            my_ball.start_position()
            make_brick()
            my_table.draw_score("", "              승리!!")
            
            
            
    # 아래쪽 벽에 공이 충돌하는지 감지
    if(my_ball.y_posn >= my_table.height - my_ball.height):
        
        my_ball.stop_ball()
        my_ball.start_position()

        bat_B.start_position()
        
        first_serve = True
        life = life-1
        my_table.draw_score("", "              남은 목숨%d" %life)

    #목숨이 0이 되면 패배&리셋
        
    if(life == 0):
        my_ball.stop_ball()
        my_ball.start_position()

        bat_B.start_position()
        
        first_serve = True
        life = 4
        #이전에 생서된 벽돌 삭제
        for b in bricks:
            my_table.remove_item(b.rectangle)
            bricks.remove(b)
        for n in bricks:
            my_table.remove_item(n.rectangle)
            bricks.remove(n)
        for i in bricks:
            my_table.remove_item(i.rectangle)
            bricks.remove(i)
        for gap in bricks:
            my_table.remove_item(gap.rectangle)
            bricks.remove(gap)
        for x in bricks:
            my_table.remove_item(x.rectangle)
            bricks.remove(x)
        for brick in bricks:
            my_table.remove_item(brick.rectangle)
            bricks.remove(brick)
        for colour in bricks:
            my_table.remove_item(colour.rectangle)
            bricks.remove(colour)
        for a in bricks:
            my_table.remove_item(a.rectangle)
            bricks.remove(a)

        make_brick()
    
        my_table.draw_score("", "              패배!!")        
        
    my_ball.move_next()
    window.after(50, game_flow)

#게임 재시작 하는 메소드
def restart_game(master):
    my_ball.start_ball(x_speed=x_velocity, y_speed=y_velocity)
    bat_B.start_position()
    my_table.draw_score("", "")
    
    
window.bind("<Left>", bat_B.move_left)
window.bind("<Right>", bat_B.move_right)
window.bind("<space>", restart_game)


game_flow()
window.mainloop()


"""
이벤트를 효율적으로 처리하기 위해 GUI는 이벤트 루프를 사용한다
이벤트 루프는 이벤트를 기다리고 있다가 특정 이벤트가 발생하면 관련 코드를 호출한다
main.loop메소드는 while루프를 대신한다
"""
