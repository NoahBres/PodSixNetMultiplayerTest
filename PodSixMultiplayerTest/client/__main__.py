from .client import Client
from .game import Game
from time import sleep

if __name__ == "__main__":
    print("Test")
    game = Game()
    game.run()
    # client = Client()
    # while 1:
    #     client.Loop()
    #     sleep(0.001)
