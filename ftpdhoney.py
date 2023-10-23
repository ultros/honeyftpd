import logging

import pyftpdlib.authorizers
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class DummyAuthorizerCollectCreds(DummyAuthorizer):

    def validate_authentication(self, username, password, handler):
        with open("/opt/ftpdhoney/ftpdhoney-credentials.txt", 'a') as file_obj:
            file_obj.write(f"{handler.addr[0]}:{username}:{password}\n")
        raise pyftpdlib.authorizers.AuthenticationFailed


def main():
    logging.basicConfig(level=logging.FATAL)
    authorizer = DummyAuthorizerCollectCreds()
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "vsFTPD 2.3.4"
    address = ('', 21)
    server = FTPServer(address, handler)
    server.serve_forever()


if __name__ == '__main__':
    main()
