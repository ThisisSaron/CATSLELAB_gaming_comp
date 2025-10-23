import arcade

window = arcade.Window(title = "Running sprite")
window.center_window()

class Player(arcade.Sprite):
    def __init__(self, texture_list: list[arcade.Texture]):
        super().__init__(texture_list[0])
        self.time_elapsed = 0

        self.textures = texture_list

    def update(self, delta_time, float = 1/60, *args, **kwargs) -> None:
        self.time_elapsed += delta_time
        
        if self.time_elapsed > 1: # change this to make it last longer
            if self.cur_texture_index < len(self.textures):
                self.set_texture(self.cur_texture_index)
                self.cur_texture_index += 1
            self.time_elapsed = 0

        if self.cur_texture_index == 3:
            self.cur_texture_index = 0

class GameView(arcade.View):
    def __init__(self) -> None:
        super().__init__()

        self.sprite_list = arcade.SpriteList()

        dracula_sheet = arcade.load_spritesheet("sprites/spritesheets/frankenstein.png")
        texture_list = dracula_sheet.get_texture_grid(size=(1024,1536), columns=3, count=3)

        self.player = Player(texture_list)
        self.player.position = 640, 360
        self.sprite_list.append(self.player)

    def on_draw(self) -> None:
        self.clear()
        self.sprite_list.draw()

    def on_update(self, delta_time: float) -> None:
        self.sprite_list.update()

game = GameView()
window.show_view(game)
arcade.run()