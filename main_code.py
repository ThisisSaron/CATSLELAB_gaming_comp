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
mouth = ["faces/9mouth.PNG","faces/11mouth.PNG","faces/12mouth.PNG","faces/13mouth.PNG" ]
pumpkin = "Images/pumpkin2.png"
clients = [("sprites/dracula1.PNG","sprites/dracula2.PNG","sprites/dracula3.PNG"),
            ("sprites/frankenstein1.PNG","sprites/frankenstein2.PNG","sprites/frankenstein3.PNG"),
                ("sprites/medusa1.PNG","sprites/medusa2.PNG","sprites/medusa3.PNG")]
trash_cans = []

#pumpkins = ["Images/pumpkin1.png", "Images/pumpkin2.png", "Images/pumpkin3.png", "Images/pumpkin4.png" ]

# sound and bg music
background_music = arcade.load_sound("sound/background_music.mp3")
carving_sound = Sound("sound/saw.mp3")
correct_sound = Sound("sound/correct.mp3")

def gen_random_pumpkins():
    eye = random.randint(0,3)
    nose = random.randint(0,2)
    mouth = random.randint(0,2)

    return [eye,nose,mouth]


class MyGameWindow(arcade.Window):
    def __init__(self,width,height,title,resizable = True):
        super().__init__(width,height,title,resizable=resizable)
        #self.set_location(400,200)
        self.held_sprite = None
        self.collision = [False,(None,None)]
        self.submit = False
        self.lst = []
        self.start = time.time()
        self.lost = False
        self.timer = 10
        self.timer_start = 0
        self.i = None
        self.client_sprites = arcade.SpriteList()

        self.score_count = 0
        #HOW TO CHANGE THE FONT
        self.score_text = arcade.Text(f"${self.score_count}",x=1850,y=950,color =arcade.color.YELLOW,font_size=30,align="right", font_name='Kenney Pixel')
        window = arcade.get_window()
        self.screen_width = window.width
        self.screen_height = window.height
        self.eyespos = [(self.screen_width-90,5),(self.screen_width-105,70),(self.screen_width-110,110),(self.screen_width-120,130)]
        self.nosepos = [(self.screen_width-220,20),(self.screen_width-220,100),(self.screen_width-225,120)]
        self.mouthpos = [(self.screen_width-410,70),(self.screen_width-410,137),(self.screen_width-410,190)]
        self.curr_sprites = arcade.SpriteList()
        self.current_ob = []

        self.gen_pumpkin = arcade.SpriteList()

        print(self.screen_width,self.screen_height)

        self.background = arcade.load_texture("Images/BackGround.png")
        self.background = arcade.load_texture("Images/BackGround.png")
        self.table =  arcade.load_texture("Images/table.jpeg")
        self.sprite_list = arcade.SpriteList()
        self.pumpkin = arcade.Sprite(pumpkin,scale=0.3)
        self.pumpkin.position = 320,180
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


    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        #ADD BACKGROUND MUSIC
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
                        self.carving_playback = carving_sound.play()
                else:
                    self.eye_sprite_list[i].position = self.eyespos[i]
            elif self.collision[1][0] == "nose":
                if i+5 not in self.current_ob: 
                        self.nose_sprite_list[i].position = self.nosepos[i]
                        self.nose_sprite_curr = arcade.Sprite(nose[i],scale=0.3)
                        self.nose_sprite_curr.position = self.pumpkin.position[0],self.pumpkin.position[1]
                        self.curr_sprites.append(self.nose_sprite_curr)
                        self.current_ob.append(i+5) #CHANGE THIS IF YOU ADD MORE EYES
                        self.carving_playback = carving_sound.play()
                else:
                    self.nose_sprite_list[i].position = self.nosepos[i]
            elif self.collision[1][0] == "mouth":
                if i+9 not in self.current_ob: 
                        self.mouth_sprite_list[i].position = self.mouthpos[i]
                        self.mouth_sprite_curr = arcade.Sprite(mouth[i],scale=0.3)
                        self.mouth_sprite_curr.position = self.pumpkin.position
                        self.curr_sprites.append(self.mouth_sprite_curr)
                        self.current_ob.append(i+9) #CHANGE THIS IF YOU ADD MORE EYES
                        self.carving_playback = carving_sound.play()
                else:
                    self.mouth_sprite_list[i].position = self.mouthpos[i]
            self.collision = (False,(None,None))

        if not self.gen_pumpkin and time.time() - self.start > 10:
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
            if time.time() - self.timer_start < 7:
                self.client1 = arcade.Sprite(clients[self.i][0],scale=0.3)
                self.client1.position = 880,350
                self.client_sprites.append(self.client1)
            elif time.time() - self.timer_start < 10:
                self.client_sprites = arcade.SpriteList()
                self.client1 = arcade.Sprite(clients[self.i][1],scale=0.3)
                self.client1.position = 880,350
                self.client_sprites.append(self.client1)
            else:
                self.client_sprites = arcade.SpriteList()
                self.client1 = arcade.Sprite(clients[self.i][2],scale=0.3)
                self.client1.position = 880,350
                self.client_sprites.append(self.client1)


        if self.submit:
            self.start = time.time()
            self.gen_pumpkin = arcade.SpriteList()
            self.curr_sprites = arcade.SpriteList()
            self.pumpkin.position = 300,180
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
                    self.score_count += 50
                    self.score_text.text = f"${self.score_count}"
                    self.current_ob = []
                    self.client_sprites = arcade.SpriteList()
                    self.client1 = None
                    self.timer_start = None
            self.though_bubble_sprite = arcade.SpriteList()
                    self.correct_playback = correct_sound.play()
            self.submit = False

        if self.lost: #DECIDE IF WE WANT TO END THE GAME OR DECREMENT MONEY
            arcade.draw_text("GAME OVER",600,500,arcade.color.WHITE,24,width=400,align="center")
            self.sprite_list= arcade.SpriteList()
            self.curr_sprites= arcade.SpriteList()
            self.gen_pumpkin= arcade.SpriteList()
            self.eye_sprite_list= arcade.SpriteList()
            self.nose_sprite_list= arcade.SpriteList()
            self.mouth_sprite_list= arcade.SpriteList()
            self.though_bubble_sprite = arcade.SpriteList()


        self.sprite_list.draw()
        self.curr_sprites.draw()
        self.though_bubble_sprite.draw()
        self.gen_pumpkin.draw()
        self.eye_sprite_list.draw()
        self.nose_sprite_list.draw()
        self.mouth_sprite_list.draw()
        self.score_text.draw()

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




MyGameWindow(screen_width,screen_height,"Pumpkin Parlor")
arcade.play_sound(background_music, volume=0.5, loop=True)
arcade.run()
