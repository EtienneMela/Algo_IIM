from BlockChain import BlockChain

def startBlockchain(*args):
    blockchain = BlockChain()
    [blockchain.add(arg) for arg in args]
    return blockchain

def printBlocks(blockchain):
    i = 0
    while i < len(blockchain.chain):
        print(blockchain.getFormattedBlock(i))
        i += 1

# -- Start the blockchain --
myblockchain = startBlockchain()
# -- Print all the blocks in human-readable format
# printBlocks(blockchain)
# -- Add a block with its body --
myblockchain.add('test 1')
myblockchain.add('test 2')
# -- Add block from a file --
#myblockchain.loadFromJson()
# -- Delete the last block
#myblockchain.deleteLastBlock()
# -- Find an occurence of a string in the body of all the blocks --
#myblockchain.findContent('salut')
# -- Make a full sanity check of the blockchain --
#myblockchain.fullCheck()


