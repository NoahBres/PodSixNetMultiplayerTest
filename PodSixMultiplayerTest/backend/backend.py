from PodSixNet.Server import Server
from .client_channel import ClientChannel
from weakref import WeakKeyDictionary
from time import sleep, time
import hashlib


class Backend(Server):

    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.players = WeakKeyDictionary()

        print("Server launched")

    def Connected(self, channel, addr):
        print("New connection: ")
        print(channel)
        self.add_player(channel)

    def add_player(self, player):
        print("New Player: " + str(player.addr))
        player.Send({"action": "set_id", "data": player.id})
        self.players[player] = True
        self.send_players()

    def delete_player(self, player):
        print("Deleting Player " + str(player.addr))
        self.send_to_all({"action": "del_player", "data": player.id})
        del self.players[player]
        # self.send_players()

    def send_players(self):
        self.send_to_all({"action": "players", "players": [p.id for p in self.players]})

    def send_to_all(self, data):
        [p.Send(data) for p in self.players]

    def send_to_all_origin(self, data, origin):
        [p.Send(data) for p in self.players if p.id != origin]

    def get_unique_id(self):
        hash = hashlib.sha1()
        hash.update(str(time()).encode("utf-8"))
        return hash.hexdigest()[
            :10
        ]  # just to shorten the id. hopefully won't get collisions but if so just don't shorten it

    def move_player(self, data):
        self.send_to_all_origin(data, data["origin"])

    def run(self):
        while True:
            self.Pump()
            sleep(0.0001)
