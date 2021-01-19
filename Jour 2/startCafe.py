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

myblockchain = startBlockchain('coucou', 'bonsoir')
myblockchain.add('salut')
printBlocks(myblockchain)
