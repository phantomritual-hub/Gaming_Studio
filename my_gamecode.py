import requests as req
import random as r
import pygame as py
py.init()
screen = py.display.set_mode((1350,700))
active = 'Main'
is_running = True
def check_Button(x,y,xf,yf,p,b_no,Main =True):
    if Main == True:
        Button = py.draw.rect(screen,(1,1,255),(x,y,xf,yf))
        if (x<p[0]<(xf+x)) and (y<p[1]<(yf+y)):
            return b_no
        else:
            return None
    else:
        Button = py.draw.rect(screen,(1,255,1),(x,y,xf,yf))
        if (x<p[0]<(xf+x)) and (y<p[1]<(yf+y)):
            return b_no
        else:
            return None
def generate_number(vertical=5,horizontal=5):
    List={}
    while len(List)!=(vertical*horizontal):
        List[r.randint(1,vertical*horizontal)] = False
    else:
        return List






best_time=['default']
#setting
rows,columns,timer,multicolour,ghostmode=5,5,1,False,False
touch_pos = (0,0)
while is_running:
    screen.fill((1,1,1))
    e=py.event.get()
    for i in e:
        if i.type == py.QUIT:
            is_running = False
            break
        if i.type ==py.MOUSEBUTTONDOWN:
            if i.button==1:
                touch_pos = (i.pos[0],i.pos[1])
    if active=='Main':
        for num in range(1,6):
            b=check_Button(660,60*(num-1) + 250,100,40,touch_pos,num)
            if b ==num:
                match b:
                    case 1:
                        print(1)
                        active,touch_pos='Leaderboard',(0,0)
                    case 2:
                        print(2)
                        active,touch_pos='Play',(0,0)
                    case 3:
                        print(3)
                        active,touch_pos='Settings',(0,0)
                    case 4:
                        print(4)
                        active,touch_pos='Create Room',(0,0)
                    case 5:
                        print(5)
                        active,touch_pos='Daily tasks',(0,0)
    elif active == 'Leaderboard':
        b=check_Button(10,10,100,40,touch_pos,0,False)
        if best_time == ['default']:
            lists = req.get('https://gaming-studio-cb2a.onrender.com/leaderboard').json()
            
            best_time=[]
            for i in lists.values():
                best_time.append(i)
            best_time.sort()
            for sorting in range(len(lists)):
                for k,v in lists.items():
                    if v==best_time[0]:
                        best_time.remove(v)
                        print(k,':',v)
                        break
        if b==0:
            print('w')
            best_time=['default']
            active ='Main'
    
    py.display.update()
py.quit()


##import requests
##with open("test.py", "r", encoding="utf-8") as f:
##    code = f.read()
##
##requests.post(
##    "https://gaming-studio-cb2a.onrender.com/change",
##    data=code
##)
