# import argparse
from .backend import Backend
from time import sleep

# parser = argparse.ArgumentParser()

# parser.add_argument("--host", dest="host", help="Host to connect to")
# parser.add_argument("--port", dest="port", help="Port to connect to")

# args = parser.parse_args()

if __name__ == "__main__":
    # server = Server(args.host, args.port)
    print("test")
    backend = Backend(localaddr=("localhost", 1234))
    backend.run()
