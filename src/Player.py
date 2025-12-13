import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player:
    """Класс игрока"""
    def __init__(self):
        self.radius = 30
        self.speed = 5
        
        self.player = None
        self.keys_pressed = set()

        
        # Переменные для движения
        self.change_x = 0
        self.change_y = 0
    
    def update(self):
        """Обновление позиции игрока"""
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        # Ограничение движения по краям экрана
        if self.center_x < self.radius:
            self.center_x = self.radius
        if self.center_x > SCREEN_WIDTH - self.radius:
            self.center_x = SCREEN_WIDTH - self.radius
        if self.center_y < self.radius:
            self.center_y = self.radius
        if self.center_y > SCREEN_HEIGHT - self.radius:
            self.center_y = SCREEN_HEIGHT - self.radius
    
    def draw(self):
        """Отрисовка игрока"""
        arcade.draw_circle_filled(
            self.center_x, 
            self.center_y, 
            self.radius, 
            self.color
        )

    def setup(self):
        # Игрок.
        self.player = {
            'x': SCREEN_WIDTH // 2,
            'y': SCREEN_HEIGHT // 2,
            'radius': 20,
            'color': arcade.color.BLUE,
            'speed': 300
        }
        
        
    def on_update(self, delta_time):
        # Движение игрока
        dx, dy = 0, 0
        if arcade.key.LEFT in self.keys_pressed or arcade.key.A in self.keys_pressed:
            dx -= self.player['speed'] * delta_time
        if arcade.key.RIGHT in self.keys_pressed or arcade.key.D in self.keys_pressed:
            dx += self.player['speed'] * delta_time
        if arcade.key.UP in self.keys_pressed or arcade.key.W in self.keys_pressed:
            dy += self.player['speed'] * delta_time
        if arcade.key.DOWN in self.keys_pressed or arcade.key.S in self.keys_pressed:
            dy -= self.player['speed'] * delta_time

        if dx != 0 and dy != 0:
            factor = 0.7071
            dx *= factor
            dy *= factor

        self.player['x'] += dx
        self.player['y'] += dy

        # Ограничение в пределах экрана
        r = self.player['radius']
        self.player['x'] = max(r, min(Player.SCREEN_WIDTH - r, self.player['x']))
        self.player['y'] = max(r, min(Player.SCREEN_HEIGHT - r, self.player['y']))
    

    def on_draw(self):
        self.clear()

        # Рисуем игрока
        arcade.draw_circle_filled(self.player['x'], self.player['y'],
                                  self.player['radius'], self.player['color'])
