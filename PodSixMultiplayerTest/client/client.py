from PodSixNet.Connection import connection, ConnectionListener
from sys import exit


class Client(ConnectionListener):
    def __init__(self, game):
        self.Connect(("localhost", 1234))

        self.game = game
        self.id = None

    def loop(self):
        connection.Pump()
        self.Pump()

    def Network(self, data):
        print(data)

    def Network_connected(self, data):
        print("connected")

    def Network_disconnected(self, data):
        print("Server disconnected")
        # exit()

    def Network_error(self, data):
        print(f"Error: {data['error'][1]}")

    def Network_set_id(self, data):
        print(f"Setting id: {data['data']}")
        self.game.set_client_id(data["data"])
        self.id = data["data"]

    def Network_players(self, data):
        print("Players update: " + ", ".join(p for p in data["players"]))
        self.game.set_players(data["players"])

    def Network_del_player(self, data):
        self.game.del_player(data)

    def Network_update(self, data):
        self.game.move_players(data)

    def send(self, action, data):
        connection.Send({"action": action, "origin": self.id, "data": data})
