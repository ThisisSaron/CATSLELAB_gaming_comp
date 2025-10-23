import arcade
import pyglet

display = pyglet.display.get_display()
screen = display.get_default_screen()

screen_width = screen.width
screen_height = screen.height

eyes = ["faces/1eyes.PNG","faces/2eyes.PNG","faces/3eyes.PNG","faces/4eyes.PNG","faces/5eyes.PNG"]
nose = ["faces/6nose.PNG","faces/7nose.PNG","faces/8nose.PNG"]
mouth = ["faces/10mouth.PNG","faces/11mouth.PNG","faces/12mouth.PNG","faces/13mouth.PNG" ]


class MyGameWindow(arcade.Window):
    def __init__(self,width,height,title,resizable = True):
        super().__init__(width,height,title,resizable=resizable)
        #self.set_location(400,200)
        window = arcade.get_window()
        self.screen_width = window.width
        self.screen_height = window.height
        print(self.screen_width,self.screen_height)

        self.background = arcade.load_texture("Images\BackGround.png")
        self.table =  arcade.load_texture("Images/table.jpeg")
        self.sprite_list = arcade.SpriteList()
                #eyes
        self.eye_sprite1 = arcade.Sprite(eyes[0],scale=0.2)
        self.eye_sprite1.position = self.screen_width-420,5
        self.sprite_list.append(self.eye_sprite1)

        self.eye_sprite2 = arcade.Sprite(eyes[1],scale=0.2)
        self.eye_sprite2.position = self.screen_width-420,70
        self.sprite_list.append(self.eye_sprite2)

        self.eye_sprite3 = arcade.Sprite(eyes[2],scale=0.2)
        self.eye_sprite3.position = self.screen_width-420,130
        self.sprite_list.append(self.eye_sprite3)

        self.eye_sprite4 = arcade.Sprite(eyes[4],scale=0.2)
        self.eye_sprite4.position = self.screen_width-420,150
        self.sprite_list.append(self.eye_sprite4)
        ###############################################
                    #nose
        self.nose_sprite6 = arcade.Sprite(nose[0],scale=0.5)
        self.nose_sprite6.position = self.screen_width-620,20
        self.sprite_list.append(self.nose_sprite6)

        self.nose_sprite7 = arcade.Sprite(nose[1],scale=0.5)
        self.nose_sprite7.position = self.screen_width-620,120
        self.sprite_list.append(self.nose_sprite7)

        self.nose_sprite8 = arcade.Sprite(nose[2],scale=0.5)
        self.nose_sprite8.position = self.screen_width-620,160
        self.sprite_list.append(self.nose_sprite8)



    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        #background render
        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(-10, -1, self.screen_width-250,self.screen_height),
        )

        arcade.draw_texture_rect(
            self.table,
            arcade.LBWH(-200,-700, self.screen_width+190,self.screen_height),
        )

        self.sprite_list.draw()


MyGameWindow(screen_width,screen_height,"Pumpkin Parlor")
arcade.run()