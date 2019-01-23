from .client import Client
from time import sleep

if __name__ == "__main__":
    print("Test")
    client = Client()
    while 1:
        client.Loop()
        sleep(0.001)
