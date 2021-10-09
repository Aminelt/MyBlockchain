import sys
import hashlib
import json
from time import time
from uuid import uuid4
from Flask import flask, jsonify, request
import requests
from urllib.parse import urlparse

class BlockChain(object):
    difficulty_target= "0000"
    def hash_block(self, block):
        block_encoded = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_encoded).hexdigest()
    def __init__(self):
        #stores all the blocks in the entire blockchain
        self.chain
        #stores the transactions for the
        #current block
        self.current_transactions = []
        #create the genesis block with a specific fixed hash
        #of previous block genesis starts with index 0
        genesis_hash = self.hash_block("genesis_block")
        self.append_block(
            hash_of_previsous_block = genesis_hash,
            nonce = self.proof_of_work(0,genesis_hash,[])
        )
    def proof_of_work(self, index,hash_of_previous_block,transactions):
        #try with nonce
        nonce = 0
        #try hashing then nonce together with the hqsh of the previous block until it4s valid
        while self.valid_proof(index, hash_of_previous_block,transactions,nonce) is False:
            nonce += 1
        return nonce
      #Appending the block to the block chain
      #creates a new block and adds it to the blockchain
    def append_block(self,nonce,hash_of_previous_block):
        block = {
            'index': len(self.chain),
            'timestamp': time(),
            'transactions': self.current_transactions,
            'nonce': nonce,
            'hash_of_previous_block': hash_of_previous_block
        }
        self.current_transactions = []
        #Add the new block to the blockchain
        self.chain.append(block)
        return block
    def add_transaction(self,sender,recipient,amount):
        self.current_transactions.append({
            'amount': amount,
            'recipient': recipient,
            'sender': sender,
        })
        return  self.last_block['index'] + 1
    @property
    def last_block(self):
        #return the last block in the block chain
        return self.chain[-1]
#Exposing the blockchain class to REST API
 app = Flask(__name__)
 #geneate a unique adress
 node_identifier = str(uuid4()).replace('-',")
 #instanciate the blockchain
blockchain = BlockChain
#Obtaining the full blockchain
@app.route('/blockchain',methods=['GET'])
def full_chain():
    response = {
        'chain':blockchain.chain,
        'length':len(blockchain.chain)
    }
    return jsonify(response),200
#Performing Mining
@app.route('/mine',methods=['GET'])
def mine_block():
    blockchain.add_transaction(
        sender = "o",
        recipient= node_identifier,
        amount=1,
    )
    #obtain the last block hash
    last_block_hash = blockchain.hash_block(blockchain.last_block)
    #using Pow get the nince for the new block to be added to the blockchain
    index = len(blockchain.chain)
    nonce = blockchain.proof_of_work(index,last_block_hash,blockchain.current_transactions)
    #add the new block to the block chain using the last block
    #hash and the current nonce
    block = blockchain.append_block(nonce,last_block_hash)
    response = {
        'message' :"New Block Mined",
        'index' : block['index'],
        'hash of previous block': block['transactions'],
    }
    return jsonify(response), 200
#rewards for the miner
#Adding tansactions
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    #get the value from client
    values = request.get_json()
    #check that the required fiels are POSTed
    required_fields = ['sender','recipient','amount']
    if not all(k in values for k in required_fields):
       return 'Missing fields', 400
 # create a new transaction
    index = blockchain.add_transaction(
    values['sender'],
    values['recipient'],
    values['amount']
 )
    response = {'message':'Transaction will be added to Block {index}'}
    return jsonify(response), 201


#testing
 if __name__ == '__main__':
     app.run(host='0.0.0.0', port=int(sys.argv[1]))
print('test done successfully')


