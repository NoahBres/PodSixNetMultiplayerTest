from PodSixNet.Channel import Channel


class ClientChannel(Channel):
    def __init__(self, *args, **kwargs):
        self.nickname = "anonymous"
        Channel.__init__(self, *args, **kwargs)

    def Network(self, data):
        print(data)

    def Network_myaction(self, data):
        print(data)

