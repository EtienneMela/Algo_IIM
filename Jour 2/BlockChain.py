from Block import Block
from datetime import datetime
from hashlib import sha256
import json
import random
import string
import pprint

class BlockChain: 
    def __init__(self):
        self.chain = []
        self.fileWritten = "data.json"
        print(self)
    
    def add(self, body):
        """
        Add a block to the blockchain
        """
        previousHash = None if len(self.chain) == 0 else self.chain[-1].hash
        block = Block(len(self.chain), previousHash, body)
        self.chain.append(block)
        self.writeJsonFile()
        return self
    
    def getFormattedBlock(self, index):
        block = self.chain[index]
        readable = "[\n" + ",\n ".join(x for x in [
          str("previousHash: " + str(block.previousHash)),
          str("body: " + str(block.body)),
          str("timestamp: " + str(block.timestamp)),
          str("nonce: " + str(block.nonce)),
          str("hash: " + str(block.hash)),
        ]) + "\n]"
        return readable

    def get_block(self, index):
        return self.chain[index]

    def writeJsonFile(self):
        f = open(self.fileWritten, "w")
        temp = self.getCompleteData()
        f.write(temp)
        f.close()
    
    def getCompleteData(self):
        i = 0
        buffer = "[\n"
        while i < len(self.chain):
            buffer += json.dumps(self.chain[i].__dict__) 
            if i == len(self.chain) - 1:
                buffer += "\n"
            else:
                buffer += ",\n"
            i += 1
        buffer += "]"
        return buffer
