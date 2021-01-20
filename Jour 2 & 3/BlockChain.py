from Block import Block
from datetime import datetime
from hashlib import sha256
from os import path
import json
import random
import string
import pprint
import re 

class BlockChain: 
    def __init__(self):
        self.chain = []
        self.fileWritten = "data.json"
    
    def add(self, body):
        """
        Add a block to the blockchain by command input
        """
        previousHash = None if len(self.chain) == 0 else self.chain[-1].hash
        block = Block(len(self.chain), previousHash, body)
        if self.checkIntegrity(block) == "":
            self.chain.append(block)
            self.writeJsonFile(False, block)
            return self
        else: 
            print(self.checkIntegrity(block))
    
    def addFromFile(self, identifier, previousHash, body, nonce, timestamp, generateHash):
        """
        Add a block to the blockchain by using a Json file, serialized by loadFromJson()
        """
        previousHash = None if identifier == 0 else previousHash
        block = Block(identifier, previousHash, body, nonce=nonce, timestamp=timestamp, generateHash=generateHash)
        if self.checkIntegrity(block) == "":
            self.chain.append(block)
            self.writeJsonFile(True, block)
            return self
        else: 
            print(self.checkIntegrity(block))

    def getFormattedBlock(self, index):
        """
        Format the block selected using its index to be human readable (for debug purposes)
        """
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
        """
        Get the block object using its index
        """
        return self.chain[index] if len(self.chain)  > index else False
    
    def get_all(self):
        """
        Get all the block objects currently in the blockchain
        """
        i = 0
        buffer = []
        while i < len(self.chain):
            buffer.append(self.chain[i].__dict__)
            i = i + 1
        return buffer

    def getCompleteData(self):
        """
        Get all blockchain in the form of json objects
        """
        i = 0   
        buffer = ""
        while i < len(self.chain):
            buffer += json.dumps(self.chain[i].__dict__) 
            buffer += "\n"
            i += 1
        return buffer

    def writeJsonFile(self, destructive, block):
        """
        Write a json snapshot of the blockchain with or without overwriting the one already existing (overwirting uses getCompleteData)
        """
        if destructive == False:
            if block.identifier == 0:
                f = open(self.fileWritten, "w")
            else:
                f = open(self.fileWritten, "a")
            temp = json.dumps(block.__dict__) + "\n"
            f.write(temp)
            f.close()
        else:
            open(self.fileWritten, "w").close()
            f = open(self.fileWritten, "w")
            temp = self.getCompleteData()
            f.write(temp)
            f.close()
    
    def loadFromJson(self, file):
        """
        Read the json file to load and parse it for addFromFile()
        """
        if path.exists(file):
            blockList = []
            print("Started Reading JSON file which contains multiple blocks")
            with open(file) as f:
                file = f.readlines()
                for jsonObj in file:
                    blockDict = json.loads(jsonObj)
                    blockList.append(blockDict)
            for block in blockList:
                print("Writing block number :" + str(block["identifier"]))
                self.addFromFile(block["identifier"], block["previousHash"], block["body"], block["nonce"], block["timestamp"], block["hash"])
        else:
            return "Fichier " + file + " non trouvé"

    def findContent(self, needle):
        """
        Check for all BLocks for the occurence of a string
        """
        i = 0
        needle = str(needle)
        while i < len(self.chain):
            temp = str(self.chain[i].body)
            count = temp.count(needle)
            if count >= 1:
                return self.getFormattedBlock(i)
            i += 1
        return "Occurences de : '" + needle  + "' non trouvées dans les blocs"
    
    def checkIntegrity(self, blockToCheck):
        """
        Check if a block is functional related to the block before
        """
        currentBlock = blockToCheck
        previousBlock = self.get_block(blockToCheck.identifier - 1) if blockToCheck.identifier != 0 else False
        message = ""
        if previousBlock != False:
            if currentBlock.previousHash != previousBlock.hash:
                 message += "The blockchain integrity is compromised - previous hash not matching at index : " + str(currentBlock.identifier) + "\n"
            if currentBlock.identifier - 1 != previousBlock.identifier:
                message += "The blockchain integrity is compromised - indexes are messed up at hash : " + str(currentBlock.hash) + "\n"
        else:
            if currentBlock.previousHash != None:
                message += "The blockchain integrity is compromised : genesis block possess a previous hash \n"
        return message
    
    def fullCheck(self):
        """
        Make a full check of the blockchain
        """
        i = 0
        buffer = ""
        while i < len(self.chain):
            buffer += self.checkIntegrity(self.chain[i])
            i += 1
        return buffer
    
    def deleteLastBlock(self):
        """
        Delete the last block
        """
        chain = self.get_all()
        deleted = chain.pop()
        return deleted
