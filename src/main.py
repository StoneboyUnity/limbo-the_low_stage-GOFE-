import arcade
import GameWindow
import Player


 
def __init__(self):
    Player.Player.setup(self)
    Player.Player.on_draw(self)
    Player.Player.on_update(self)

    
def main():
    """Главная функция"""
   
    window = GameWindow.GameWindow()
    arcade.run()


if __name__ == "__main__":
    main()