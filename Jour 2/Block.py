from datetime import datetime
from hashlib import sha256
import random
import string
import pprint

class Block:
    def __init__(self, identifier, previousHash, body, **kwargs):
        self.identifier = identifier
        self.previousHash = previousHash
        self.body = body
        self.nonce = 0 if 'nonce' not in kwargs else kwargs.get('nonce')
        self.timestamp = self.getTimestamp() if 'timestamp' not in kwargs else kwargs.get('timestamp')
        self.hash = self.generateHash() if 'generateHash' not in kwargs else kwargs.get('generateHash')

    def generateHash(self):
        # Ajout d'une fonction prenant 3 lettres au hasard pour mitiger les risques de collision
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(3))
        hash = ""
        while not hash.startswith('cafe'):
            bloc = result_str + str(self.identifier) + str(self.previousHash) + str(self.timestamp) + str(self.body) + str(self.nonce)
            encoded = bloc.encode('UTF-8', 'strict')
            self.nonce = self.nonce + 1
            hash = sha256(encoded).hexdigest()
        return hash

    def getTimestamp(self):
        return datetime.now().strftime("%Y-%m-%d, %H:%M:%S.%f")

