from PodSixNet.Connection import connection, ConnectionListener


class Client(ConnectionListener):
    def __init__(self):
        self.Connect(("localhost", 1234))

        connection.Send({"action": "myaction", "blah": "Test", "things": [1, 3, 4]})

    def Loop(self):
        connection.Pump()
        self.Pump()

    def Network_connected(self, data):
        print("connected")
