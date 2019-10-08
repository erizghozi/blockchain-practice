from block import Block

class BlockChain(object):
    def __init__(self):
        print("Instantiating")
        self.chain = []
        self.current_node_transactions = []
        self.create_genesis_block()

    def create_new_block(self, proof, previous_hash):
        block = Block(
            index = len(self.chain),
            proof = proof,
            previous_hash = previous_hash,
            transactions = self.current_node_transactions
        )
        self.current_node_transactions = []
        self.chain.append(block)
        print("Block #",len(self.chain)-1," has been added to the Blockchain!")
        print("Hash: ",block.get_block_hash)
        print("Prev: ",block.previous_hash)
        print("\n")
        return block

    def create_genesis_block(self):
        print("Creating genesis block")
        self.create_new_block(proof=0, previous_hash=0) 

    def create_new_transaction(self, sender, recipient, amount):
        self.current_node_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.get_last_block.index + 1

    @staticmethod
    def create_proof_of_work(previous_proof):
        proof = previous_proof + 1
        while (proof + previous_proof) % 7 != 0:
            proof += 1
        return proof

    @property
    def get_last_block(self):
        return self.chain[-1]
