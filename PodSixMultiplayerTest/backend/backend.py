from PodSixNet.Server import Server
from .client_channel import ClientChannel


class Backend(Server):

    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        print("Testetstest")

    def Connected(self, channel, addr):
        print("New connection: ")
        print(channel)
