from block import *
from blockchain import *

# membuat chain baru dan membuat genesis block
# BLOCK 0
catatan = BlockChain()
print(catatan.chain)

# persiapan membuat BLOCK 1
last_block = catatan.get_last_block
last_proof = last_block.proof
proof = catatan.create_proof_of_work(last_proof)

catatan.create_new_transaction(
    sender="0",
    recipient="address_x",
    amount=1,
)

last_hash = last_block.get_block_hash

# MEMBUAT BLOCK 1
block = catatan.create_new_block(proof, last_hash)
print(catatan.chain)


### BLOCK 2

