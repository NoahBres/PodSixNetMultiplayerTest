from sys import exit
import pygame
from pygame import locals

from .player import Player
from .client import Client
from .network_entity import NetworkEntity

(width, height) = (400, 300)
background = (0, 0, 0)

clock = pygame.time.Clock()
ticks_per_second = 60


class Game:
    def __init__(self):
        self.player = None
        self.running = None
        self.client = None
        self.network_clients = {}

    def run(self):
        self.player = Player()
        self.client = Client(self)

        pygame.init()

        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(f"Python Multiplayer Test")

        self.running = True

        try:
            while self.running:
                clock.tick(ticks_per_second)

                self.client.loop()

                self.poll_events()
                self.update()
                self.draw(screen)

            pygame.quit()
            exit(0)
        except SystemExit:
            pygame.quit()
            exit(0)

    def poll_events(self):
        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        # Check for quit
        for event in events:
            if event.type == locals.QUIT:
                self.running = False
                return
            if event.type == locals.KEYDOWN:
                if event.key == locals.K_ESCAPE:
                    self.running = False
                    return

        if keys[locals.K_w]:
            self.player.move(0, -6)
        if keys[locals.K_a]:
            self.player.move(-6, 0)
        if keys[locals.K_s]:
            self.player.move(0, 6)
        if keys[locals.K_d]:
            self.player.move(6, 0)

    def update(self):
        self.player.update()

        for identifier, client in self.network_clients.items():
            client.update()

        player_updates = self.player.get_network_updates()
        if len(player_updates):
            self.client.send("update", player_updates)

    def draw(self, screen):
        screen.fill(background)

        self.player.draw(screen)

        for identifier, client in self.network_clients.items():
            client.draw(screen)

        pygame.display.flip()

    ### Functions accessed by the client
    def set_client_id(self, id):
        pygame.display.set_caption(f"Python Multiplayer Test - {id}")

    def set_players(self, players):
        new_items = set(players) - self.network_clients.keys()

        for item in new_items:
            if item != self.client.id:
                self.network_clients[item] = NetworkEntity(item)

        print(self.network_clients)

    def del_player(self, player):
        del self.network_clients[player]

    def move_players(self, data):
        for m in data["data"]:
            self.network_clients[data["origin"]].move(m[1][0], m[1][1])
        print(data)
