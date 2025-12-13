import arcade
import Player


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Управление WASD - РАБОЧАЯ ВЕРСИЯ"

class GameWindow(arcade.Window):
    """Главное окно игры"""
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.DARK_GREEN)
        
        # СОЗДАЕМ игрока здесь!
        self.player = Player.Player()
    
    def on_draw(self):
        """Отрисовка кадра"""
        self.clear()  # Важно: используем clear(), а не start_render()
        self.player.draw()
    
    def on_key_press(self, key, modifiers):
        """Нажатие клавиш"""
        if key == arcade.key.W:
            self.player.change_y = self.player.speed
        elif key == arcade.key.S:
            self.player.change_y = -self.player.speed
        elif key == arcade.key.A:
            self.player.change_x = -self.player.speed
        elif key == arcade.key.D:
            self.player.change_x = self.player.speed
    
    def on_key_release(self, key, modifiers):
        """Отпускание клавиш"""
        # Останавливаем движение при отпускании WASD
        if key == arcade.key.W or key == arcade.key.S:
            self.player.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player.change_x = 0
    
    def update(self, delta_time):
        """Обновление логики игры"""
        self.player.update()