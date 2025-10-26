import arcade
import pyglet
import random
import time
from arcade import Sound

display = pyglet.display.get_display()
screen = display.get_default_screen()

screen_width = screen.width
screen_height = screen.height

eyes = ["faces/1eyes.PNG","faces/2eyes.PNG","faces/3eyes.PNG","faces/4eyes.PNG","faces/5eyes.PNG"]
nose = ["faces/6nose.PNG","faces/7nose.PNG","faces/8nose.PNG"]
mouth = ["faces/9mouth.PNG","faces/13mouth.PNG","faces/12mouth.PNG","faces/13mouth.PNG" ]
pumpkin = "Images/pumpkin2.png"
clients = [("sprites/dracula1.PNG","sprites/dracula2.PNG","sprites/dracula3.PNG"),
            ("sprites/frankenstein1.PNG","sprites/frankenstein2.PNG","sprites/frankenstein3.PNG"),
                ("sprites/medusa1.PNG","sprites/medusa2.PNG","sprites/medusa3.PNG")]
trash_can = "trashcan.png"

#pumpkin = ["Images/pumpkin1.png", "Images/pumpkin2.png", "Images/pumpkin3.png", "Images/pumpkin4.png" ]

# sound and bg music
background_music = arcade.load_sound("sound/background_music.mp3")
correct_sound = Sound("sound/correct.mp3")
error_sound = Sound("sound/error.mp3")

carving1 = Sound("sound/saw.mp3")
carving2 = Sound("sound/saw2.m4a")
carving3 = Sound("sound/saw3.m4a")
carvings = [carving1, carving2, carving3]

# custom fonts
arcade.load_font("fonts/Halloweendy.otf")
arcade.load_font("fonts/melted_monster.ttf")
arcade.load_font("fonts/Halloween Fright.ttf")

def gen_random_pumpkins():
    eye = random.randint(0,3)
    nose = random.randint(0,2)
    mouth = random.randint(0,2)

    return [eye,nose,mouth]


class MyGameWindow(arcade.Window):
    def __init__(self,width,height,title,resizable = True):
        super().__init__(width,height,title,resizable=resizable)
        #self.set_location(400,200)
        self.time_begin = 0
        self.total_time = 60
        self.time_text = arcade.Text(f"${self.time_begin}",x=175,y=860,color =arcade.color.CARNELIAN,font_size=30,align="right", font_name="Halloween Fright")
        self.welcome_page = True
        self.held_sprite = None
        self.collision = [False,(None,None)]
        self.submit = False
        self.lst = []
        self.start = time.time()
        self.lost = False
        self.timer = 5
        self.timer_start = 0
        self.i = None
        self.client_sprites = arcade.SpriteList()

        self.score_count = 0
        self.pay = 50
        #HOW TO CHANGE THE FONT
        self.score_text = arcade.Text(f"${self.score_count}",x=1700,y=860,color =arcade.color.BROWN_NOSE,font_size=30,align="right", font_name='Halloween Fright')
        #self.score_text = arcade.Text(f"${self.score_count}",x=500,y=500,color =arcade.color.YELLOW,font_size=30,align="right", font_name="SCOREBOARD")
        window = arcade.get_window()
        self.screen_width = window.width
        self.screen_height = window.height
        self.eyespos = [(self.screen_width-90,5),(self.screen_width-100,70),(self.screen_width-110,95),(self.screen_width-120,135)]
        self.nosepos = [(self.screen_width-220,20),(self.screen_width-220,100),(self.screen_width-225,120)]
        self.mouthpos = [(self.screen_width-410,70),(self.screen_width-410,137),(self.screen_width-410,190)]
        self.pumkinpos = [(340,180),[500,180],(340,320),(500,320)]
        self.curr_sprites = arcade.SpriteList()
        self.current_ob = []

        self.gen_pumpkin = arcade.SpriteList()

        print(self.screen_width,self.screen_height)
        self.welcome = arcade.load_texture("Images/welcomepage.png")
        self.background = arcade.load_texture("Images/bg2.JPG")
        self.table =  arcade.load_texture("Images/table.jpeg")
        self.sprite_list = arcade.SpriteList()
        self.pumpkin = arcade.Sprite(pumpkin,scale=0.3)
        self.pumpkin.position = 850,130
        self.sprite_list.append(self.pumpkin)

        self.though_bubble_sprite = arcade.SpriteList()

                #eyes
        self.eye_sprite_list = arcade.SpriteList()
        self.eye_sprite1 = arcade.Sprite(eyes[0],scale=0.2)
        self.eye_sprite1.position = self.eyespos[0]
        self.eye_sprite_list.append(self.eye_sprite1)

        self.eye_sprite2 = arcade.Sprite(eyes[1],scale=0.2)
        self.eye_sprite2.position = self.eyespos[1]
        self.eye_sprite_list.append(self.eye_sprite2)

        self.eye_sprite3 = arcade.Sprite(eyes[2],scale=0.2)
        self.eye_sprite3.position = self.eyespos[2]
        self.eye_sprite_list.append(self.eye_sprite3)

        self.eye_sprite4 = arcade.Sprite(eyes[3],scale=0.2)
        self.eye_sprite4.position = self.eyespos[3]
        self.eye_sprite_list.append(self.eye_sprite4)
        ###############################################
                    #nose
        self.nose_sprite_list = arcade.SpriteList()
        self.nose_sprite6 = arcade.Sprite(nose[0],scale=0.4)
        self.nose_sprite6.position = self.nosepos[0]
        self.nose_sprite_list.append(self.nose_sprite6)

        self.nose_sprite7 = arcade.Sprite(nose[1],scale=0.4)
        self.nose_sprite7.position = self.nosepos[1]
        self.nose_sprite_list.append(self.nose_sprite7)

        self.nose_sprite8 = arcade.Sprite(nose[2],scale=0.4)
        self.nose_sprite8.position = self.nosepos[2]
        self.nose_sprite_list.append(self.nose_sprite8)
                   # MOUTH
        self.mouth_sprite_list = arcade.SpriteList()
        self.mouth_sprite9 = arcade.Sprite(mouth[0],scale=0.3)
        self.mouth_sprite9.position = self.mouthpos[0]
        self.mouth_sprite_list.append(self.mouth_sprite9)

        self.mouth_sprite10 = arcade.Sprite(mouth[1],scale=0.3)
        self.mouth_sprite10.position = self.mouthpos[1]
        self.mouth_sprite_list.append(self.mouth_sprite10)

        self.mouth_sprite11 = arcade.Sprite(mouth[2],scale=0.3)
        self.mouth_sprite11.position = self.mouthpos[2]
        self.mouth_sprite_list.append(self.mouth_sprite11)

        self.trashcan_sprite = arcade.SpriteList()
        self.trash_can = arcade.Sprite("Images/trashcan.png",scale=0.2)
        self.trash_can.position = 70,50
        self.trashcan_sprite.append(self.trash_can)



    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        if not self.welcome_page:
            arcade.draw_texture_rect(
                self.background,
                arcade.LBWH(-10, -1, self.screen_width + 10,self.screen_height),
            )

            self.client_sprites.draw()

            arcade.draw_texture_rect(
                self.table,
                arcade.LBWH(35,-660, self.screen_width+150,self.screen_height),
            )

            if self.collision[0]:
                i = self.collision[1][1]
                if self.collision[1][0] == "eye":
                    if i+1 not in self.current_ob: 
                            self.eye_sprite_list[i].position = self.eyespos[i]
                            self.eye_sprite_curr = arcade.Sprite(eyes[i],scale=0.2)
                            self.eye_sprite_curr.position = self.pumpkin.position
                            self.curr_sprites.append(self.eye_sprite_curr)
                            self.current_ob.append(i+1)
                            self.carving_playback = random.choice(carvings).play()
                    else:
                        self.eye_sprite_list[i].position = self.eyespos[i]
                elif self.collision[1][0] == "nose":
                    if i+5 not in self.current_ob: 
                            self.nose_sprite_list[i].position = self.nosepos[i]
                            self.nose_sprite_curr = arcade.Sprite(nose[i],scale=0.3)
                            self.nose_sprite_curr.position = self.pumpkin.position[0],self.pumpkin.position[1]
                            self.curr_sprites.append(self.nose_sprite_curr)
                            self.current_ob.append(i+5) #CHANGE THIS IF YOU ADD MORE EYES
                            self.carving_playback = random.choice(carvings).play()
                    else:
                        self.nose_sprite_list[i].position = self.nosepos[i]
                elif self.collision[1][0] == "mouth":
                    if i+9 not in self.current_ob: 
                            self.mouth_sprite_list[i].position = self.mouthpos[i]
                            self.mouth_sprite_curr = arcade.Sprite(mouth[i],scale=0.3)
                            self.mouth_sprite_curr.position = self.pumpkin.position
                            self.curr_sprites.append(self.mouth_sprite_curr)
                            self.current_ob.append(i+9) #CHANGE THIS IF YOU ADD MORE EYES
                            self.carving_playback = random.choice(carvings).play()
                    else:
                        self.mouth_sprite_list[i].position = self.mouthpos[i]
                self.collision = (False,(None,None))

            if not self.gen_pumpkin and time.time() - self.start > self.timer:
                self.i = random.randint(0,2)
                self.timer_start = time.time()
                self.lst = gen_random_pumpkins()
                self.p = arcade.Sprite(pumpkin,scale=0.2)
                self.p.position = 1180,600
                self.gen_pumpkin.append(self.p)
                self.e = arcade.Sprite(eyes[self.lst[0]],scale=0.1)
                self.e.position = self.p.position
                self.gen_pumpkin.append(self.e)
                self.n = arcade.Sprite(nose[self.lst[1]],scale=0.15)
                self.n.position = self.p.position
                self.gen_pumpkin.append(self.n)
                self.m = arcade.Sprite(mouth[self.lst[2]],scale=0.15)
                self.m.position = self.p.position
                self.gen_pumpkin.append(self.m)
                self.TB = arcade.Sprite("Images/thought_bubble.png",scale=0.4)
                self.TB.position = self.p.position[0] , self.p.position[1]-25
                self.though_bubble_sprite.append(self.TB)

                
            if self.timer_start:
                if time.time() - self.timer_start < self.timer:
                    self.client1 = arcade.Sprite(clients[self.i][0],scale=0.3)
                    self.client1.position = 880,350
                    self.client_sprites.append(self.client1)
                elif time.time() - self.timer_start < self.timer+2:
                    self.client_sprites = arcade.SpriteList()
                    self.client1 = arcade.Sprite(clients[self.i][1],scale=0.3)
                    self.client1.position = 880,350
                    self.client_sprites.append(self.client1)
                    self.pay = 35
                elif time.time() - self.timer_start < self.timer+5:
                    self.client_sprites = arcade.SpriteList()
                    self.client1 = arcade.Sprite(clients[self.i][2],scale=0.3)
                    self.client1.position = 880,350
                    self.client_sprites.append(self.client1)
                    self.pay = 20
                else:
                    self.score_count -= 10
                    self.score_text.text = f"${self.score_count}"
                    #MAD SOUND HEREEEEEEEE
                    self.start = time.time()
                    self.gen_pumpkin = arcade.SpriteList()
                    self.though_bubble_sprite = arcade.SpriteList()
                    self.client_sprites = arcade.SpriteList()
                    self.client1 = None
                    self.timer_start = None


            if self.submit:
                self.start = time.time()
                self.gen_pumpkin = arcade.SpriteList()
                self.curr_sprites = arcade.SpriteList()
                self.pumpkin.position = 850,130
                self.lst[0] += 1
                self.lst[1] += 5
                self.lst[2] += 9
                if len(self.lst) != len(self.current_ob):
                    self.lost = True
                else:
                    for obj in self.lst:
                        print(self.lst,self.current_ob)
                        if obj == 12 and 11 in self.current_ob:
                            continue
                        if obj not in self.current_ob:
                            self.lost = True
                    if not self.lost:
                        self.score_count += self.pay
                        self.score_text.text = f"${self.score_count}"
                        self.current_ob = []
                        self.client_sprites = arcade.SpriteList()
                        self.client1 = None
                        self.pay = 50
                        self.timer_start = None
                        self.correct_playback = correct_sound.play()
                self.though_bubble_sprite = arcade.SpriteList()
                self.submit = False

            if self.lost: #DECIDE IF WE WANT TO END THE GAME OR DECREMENT MONEY
                self.current_ob = []
                self.client_sprites = arcade.SpriteList()
                self.client1 = None
                self.pay = 50
                self.timer_start = None
                self.lost = False
                #ERROR SOUND HEREEEEEE
                self.error_playback = error_sound.play()   


            self.time_text.text = f"{int(self.total_time - (time.time() - self.time_begin)//1)}"
            if int(self.time_text.text) > 50:
                self.timer = 5
            elif int(self.time_text.text) > 40:
                self.timer = 4
            elif int(self.time_text.text) > 30:
                self.timer = 3
            elif int(self.time_text.text) > 20:
                self.timer = 2

            if int(self.time_text.text) <= 0:
                arcade.draw_text("GAME OVER",700,500,arcade.color.WHITE,24,width=600,align="center")
                arcade.draw_text(f"Your score was: {self.score_text.text}",700,470,arcade.color.WHITE,24,width=600,align="center")
                self.time_text.text = ""
                self.sprite_list= arcade.SpriteList()
                self.curr_sprites= arcade.SpriteList()
                self.gen_pumpkin= arcade.SpriteList()
                self.eye_sprite_list= arcade.SpriteList()
                self.nose_sprite_list= arcade.SpriteList()
                self.mouth_sprite_list= arcade.SpriteList()
                self.client_sprites = arcade.SpriteList()
                self.though_bubble_sprite = arcade.SpriteList()


            self.sprite_list.draw()
            self.curr_sprites.draw()
            self.though_bubble_sprite.draw()
            self.gen_pumpkin.draw()
            self.trashcan_sprite.draw()
            self.trashcan_sprite.draw()
            self.eye_sprite_list.draw()
            self.nose_sprite_list.draw()
            self.mouth_sprite_list.draw()
            self.score_text.draw()
            self.time_text.draw()

            print(self.timer)
        else:
            self.time_begin = time.time()
            arcade.draw_texture_rect(
                self.welcome,
                arcade.LBWH(-10, -1, self.screen_width + 10,self.screen_height),
            )

            arcade.draw_text(f"YOU HAVE 60 SECONDS TO CARVE PUMPKINS THAT CUSTOMERS REQUEST",475,100,arcade.color.BUFF,24,width=600,align="center",font_name="Halloween Fright")
            arcade.draw_text(f"Higher score for speed and accuracy (don't make them mad)",510,60,arcade.color.HANSA_YELLOW,24,width=600,align="center",font_name="Halloween Fright")

            arcade.draw_text(f" -- PRESS SPACE TO START --",650,20,arcade.color.BUFF,24,width=600,align="center", font_name = "Halloween Fright")

    def on_mouse_press(self, x, y, button, modifiers):
        self.held_sprite = None
        pum = arcade.get_sprites_at_point((x,y),self.sprite_list)
        eyes = arcade.get_sprites_at_point((x,y),self.eye_sprite_list)
        nose = arcade.get_sprites_at_point((x,y),self.nose_sprite_list)
        mouth = arcade.get_sprites_at_point((x,y),self.mouth_sprite_list)

        if pum:
            self.held_sprite = pum[-1]
        if eyes:
            self.held_sprite = eyes[-1]
        if nose:
            self.held_sprite = nose[-1]
        if mouth:
            self.held_sprite = mouth[-1]

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """

        # If we are holding cards, move them with the mouse
        if not self.held_sprite:
            return
        if self.held_sprite == self.pumpkin:
            for spr in self.curr_sprites:
                spr.position = x,y
        self.held_sprite.position = x,y

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """
        if not self.held_sprite:
            return
        self.held_sprite = None

    def on_update(self, delta_time):
        for i in range(len(self.eye_sprite_list)):
            if arcade.check_for_collision(self.pumpkin,self.eye_sprite_list[i]):
                self.collision = (True, ("eye",i))

        for i in range(len(self.nose_sprite_list)):
            if arcade.check_for_collision(self.pumpkin,self.nose_sprite_list[i]):
                self.collision = (True, ("nose",i))

        for i in range(len(self.mouth_sprite_list)):
            if arcade.check_for_collision(self.pumpkin,self.mouth_sprite_list[i]):
                self.collision = (True, ("mouth",i))
        if self.gen_pumpkin:
            if arcade.check_for_collision(self.pumpkin,self.gen_pumpkin[0]):
                self.sprite_list = arcade.SpriteList()
                self.pumpkin = arcade.Sprite(pumpkin,scale=0.3)
                self.sprite_list.append(self.pumpkin)
                self.submit = True

        if not self.submit and arcade.check_for_collision(self.pumpkin,self.trash_can):
            print(True)
            self.sprite_list = arcade.SpriteList()
            self.pumpkin = arcade.Sprite(pumpkin,scale=0.3)
            self.pumpkin.position = 850,130
            self.sprite_list.append(self.pumpkin)
            self.current_ob=[]
            self.curr_sprites = arcade.SpriteList()
            self.score_count -= 15
            self.score_text.text = f"${self.score_count}"


    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            self.welcome_page = False


MyGameWindow(screen_width,screen_height,"Pumpkin Parlor")
arcade.play_sound(background_music, volume=0.5, loop=True)
arcade.run()
