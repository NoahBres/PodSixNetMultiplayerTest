from PodSixNet.Channel import Channel


class ClientChannel(Channel):
    def __init__(self, *args, **kwargs):
        self.nickname = "anonymous"
        Channel.__init__(self, *args, **kwargs)
        self.id = str(self._server.get_unique_id())
        # intid = int(self.id)
        # self.color = [(intid + 1) % 3 * 84, (intid + 2) % 3 * 84, (intid + 3) % 3 * 84]

    def Network(self, data):
        print(data)
        pass

    def Close(self):
        self._server.delete_player(self)

    # def Network_myaction(self, data):
    #     print(data)

    def Network_update(self, data):
        self._server.move_player(data)

